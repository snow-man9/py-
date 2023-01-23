import requests


#UA user-agent：请求载体的身份标识（比如某某浏览器）
#所以就要进行UA伪装
if __name__ == '__main__':
    #指定url
    url = 'https://www.sogou.com/web'
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
    }
    #处理参数携带的url，封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #url携带参数，并在处理过程中处理了参数
    response =  requests.get(url = url, params = param, headers = headers)
    page_text = response.text
    filename = kw + '.html'
    with open(filename,'w',encoding = 'utf-8') as fp :
        fp.write(page_text)
    print(filename, '保存成功！')