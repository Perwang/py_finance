# =============================================================================
# 7.3.2 相关系数分析 by 王宇韬&肖金鑫  代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import pandas as pd
from scipy.stats import pearsonr

# 读取数据
data = pd.read_excel('data.xlsx')
# 相关性分析
corr = pearsonr(data['score'], data['price'])
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]))
