# =============================================================================
# 14.2.2 获得股票衍生变量数据 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import tushare as ts
import pandas as pd
stock_code = '000002'
stock_name = '万科A'
start_date = '2020-02-01'  # 设置起始日期，如果是太早的日期容易数据丢失，导致运行失败，所以如果运行失败，请将数据改到今年的数据
end_date = '2020-04-01'  # 设置终止日期，注意点同上

# 股票时间区间内的K线图，用于提取开盘价等有用信息
stock_k = ts.get_hist_data(stock_code, start=start_date, end=end_date)

'''1.下面开始批量获取多日的前10分钟交易数据及日线行情数据'''

# 建立一个新的DataFrame，用于存储当前股票的信息
stock_table = pd.DataFrame()

# 遍历日期索引，提取所需要的数据
for current_date in stock_k.index:
    # 通过loc选中K线图中对应current_date这天的数据
    current_k_line = stock_k.loc[current_date]

    # 提取这一天前10分钟股票信息
    df = ts.get_tick_data(stock_code, date=current_date, src='tt')
    df['time'] = pd.to_datetime(current_date + ' ' + df['time'])
    t = pd.to_datetime(current_date).replace(hour=9, minute=40)
    df_10 = df[df.time <= t]
    vol = df_10.volume.sum()  # 通过sum()函数求和

    # 将数据信息放入字典中
    current_stock_info = {
        '名称': stock_name,
        '日期': pd.to_datetime(current_date),
        '开盘价': current_k_line.open,
        '收盘价': current_k_line.close,
        '股价涨跌幅(%)': current_k_line.p_change,
        '10分钟成交量': vol
    }
    # 通过append的方式增加新的一行，忽略索引
    stock_table = stock_table.append(current_stock_info, ignore_index=True)

# 通过set_index()函数将日期那一列设置为索引
stock_table = stock_table.set_index('日期')

# 设置列的顺序
order = ['名称', '开盘价', '收盘价', '股价涨跌幅(%)', '10分钟成交量']
stock_table = stock_table[order]

'''2.下面开始获得股票衍生变量数据'''

# 通过公式1获取成交量涨跌幅
stock_table['昨日10分钟成交量'] = stock_table['10分钟成交量'].shift(-1)
stock_table['成交量涨跌幅1(%)'] = (stock_table['10分钟成交量']-stock_table['昨日10分钟成交量'])/stock_table['昨日10分钟成交量']*100

# 通过公式2获得成交量涨跌幅
ten_mean = stock_table['10分钟成交量'].sort_index().rolling(10, min_periods=1).mean()
stock_table['10分钟成交量10日均值'] = ten_mean
stock_table['成交量涨跌幅2(%)'] = (stock_table['10分钟成交量']-stock_table['10分钟成交量10日均值'])/stock_table['10分钟成交量10日均值']*100

print(stock_table)
