import json

import requests

if __name__ == '__main__':
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    dic_doj = response.json()
    print(dic_doj)
    filename = word + '.json'
    fp = open(filename,'w',encoding = 'utf-8')
    json.dump(dic_doj, fp=fp,ensure_ascii=False)
    print('over')