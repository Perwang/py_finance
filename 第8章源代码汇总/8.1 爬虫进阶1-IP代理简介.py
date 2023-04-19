# =============================================================================
# 8.1 爬虫进阶1-IP代理简介 by 王宇韬  代码更新：www.huaxiaozhi.com 资料下载区
# =============================================================================

import requests  # 讯代理官网：http://www.xdaili.cn/；教程见书第8章
proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=b030195e2075469299bca6b661c913ff&orderno=YZ201810262456rdpAb0&returnType=1&count=1').text
proxy = proxy.strip()  # 这一步非常重要，因为要把看不见的换行符等给清除掉
print(proxy)
proxies = {"http": "http://"+proxy, "https": "https://"+proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, proxies=proxies).text
print(res)


# selenium库使用IP代理
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()
# 设置代理
chromeOptions.add_argument("--proxy-server=http://" + proxy)
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(options=chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)

# 退出，清除浏览器缓存
browser.quit()




# 查看本机ip，查看代理是否起作用
# url = 'http://hrnext.cn/7fV6n1'
# browser.get(url)
# browser.find_element_by_css_selector('/html/body/div[2]/div[2]/div[5]/div/img').click()

# print(browser.page_source)

# 退出，清除浏览器缓存
# browser.quit()