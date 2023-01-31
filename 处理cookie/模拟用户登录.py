import requests
from lxml import etree
import os
import rarfile

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    session = requests.session()
    url = 'https://passport.17k.com/ck/user/login'

    data = {
        'loginName' : '19170639359',
        'password' : 'c13970501259'
    }
    session.post(url=url,data=data,headers=headers)
    # print(resq.text)
    # print(resq.cookies)

    resp = session.get('https://user.17k.com/ck/book/search/merge?_versions=990&appKey=2406394919')

    print(resp.json())