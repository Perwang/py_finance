# =============================================================================
# 14.2.1 获得股票基本信息数据 by 王宇韬 代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

# 1.获取一天10分钟成交量信息
import tushare as ts
import pandas as pd
stock_code = '000002'  # 设置股票代码
current_date = '2019-04-12'  # 设置日期
df = ts.get_tick_data(stock_code, date=current_date, src='tt')
print(df)

# 提取前10分钟信息
df['time'] = pd.to_datetime(current_date + ' ' + df['time'])
t = pd.to_datetime(current_date).replace(hour=9, minute=40)
df_10 = df[df.time <= t]

# 统计前十分钟成交量信息
vol = df_10.volume.sum()
print(vol)

