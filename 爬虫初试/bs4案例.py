import requests
from bs4 import BeautifulSoup

#爬取三国演义小说所有的标签和内容：https://www.shicimingju.com/book/sanguoyanyi.html

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' #解决标题乱码问题
    page_text = response.text

    # 实例化BeautifulSoup对象，将页面源码加载到该页面中
    soup = BeautifulSoup(page_text,'lxml')
    # 解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.text
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        #对详情页发起请求
        detail_response = requests.get(url=detail_url,headers=headers)
        detail_response.encoding = 'utf-8' #解决内容乱码问题
        detail_page_text = detail_response.text
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')

        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title+'爬取成功！')