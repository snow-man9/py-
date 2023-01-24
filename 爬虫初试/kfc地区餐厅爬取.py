import requests

if __name__ == '__main__':
    #指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
    }
    word = input('enter a word:')
    param = {
        'cname': '',
        'pid': '',
        'keyword': word,
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url, params=param, headers=headers)
    filename = word + '.html'
    page_text = response.text
    print(page_text)
    with open(filename,'w',encoding = 'utf-8') as fp :
        fp.write(page_text)
    print('over!')