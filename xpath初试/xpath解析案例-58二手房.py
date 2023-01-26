from lxml import etree
import requests
#爬取58二手房的房源信息
if __name__ == '__main__':
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    print(page_text)
    list =  tree.xpath('/section[@class="list"]')
    print(list)
    for div in list :
        title = div.xpath('./a/div[2]//h3/text()')[0]
        # print(title)
