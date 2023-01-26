import requests
from lxml import etree
import os
#爬取图片
if __name__ == '__main__':
    # url = 'http://www.aqistudy.cn/historydata/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    # }
    # page_text = requests.get(url=url,headers=headers).text
    # tree = etree.HTML(page_text)
    # print(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # #解析热门城市
    # for li in host_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #
    # city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # #解析全部城市
    # for li in city_name_list:
    #     all_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(all_city_name)
    # print(all_city_names)

    url = 'http://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    #解析全部城市
    for li in li_list:
        all_city_name = li.xpath('./text()')[0]
        all_city_names.append(all_city_name)

    print(all_city_names)