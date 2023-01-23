import requests

if __name__ == '__main__':
    #指定url
    url = 'https://www.bilibili.com/'
    #发起请求
    #get方法返回一个响应对象
    response = requests.get(url = url)
    #获取响应数据
    page_text = response.text
    print((page_text))
    #持久化存储
    with open('./bilibili.html','w',encoding = 'utf-8') as fp :
        fp.write(page_text)
    print('爬取结束')