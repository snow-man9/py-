import requests
from lxml import etree
import os
#爬取图片
if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    list = tree.xpath('//div[@class="slist"]/ul/li')
    #创建一个文件夹
    if not os.path.exists('./picLabs'):
        os.mkdir('./picLabs')
    for li in list :
        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        #解决图片名乱码问题
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'picLabs/' + img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)

            print(img_name + '下载成功！')