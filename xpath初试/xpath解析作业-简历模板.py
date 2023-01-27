import requests
from lxml import etree
import os
import rarfile

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    # print(page_text)
    list = tree.xpath('//div[@class="main_list jl_main"]/div')

    #创建一个文件夹
    if not os.path.exists('./jlLabs'):
        os.mkdir('./jlLabs')

    for div in list:
        jl_url = div.xpath('./a/@href')[0]
        # print(jl_href)
        response = requests.get(url=jl_url,headers=headers)
        response.encoding = 'utf-8'
        jl_text = response.text
        jl_tree = etree.HTML(jl_text)
        jl_name = jl_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
        # jl_name = jl_name.encode('iso-8859-1').decode('gbk')
        download_url = jl_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li/a/@href')[0]
        jl_data = requests.get(url=url,headers=headers).content
        jl_path = 'jlLabs/' + jl_name
        print(jl_path)
        with open(jl_path,'wb') as fp:
            fp.write(jl_data)
