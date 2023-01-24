import requests
import json

if __name__ == '__main__':
    #指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'40',#从库中第几部电影去取
        'limit':'20'#一次取多少个
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'
    }
    response = requests.get(url=url, params=param,headers=headers)

    list_data = response.json();
    fp=open('./douban.json','w',encoding = 'utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!')