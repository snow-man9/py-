import requests
from lxml import etree
import os
#爬取图片
if __name__ == '__main__':
    url = 'https://pearvideo.com/video_1736415'
    contId = url.split('_')[1]
    videoStatusUrl = f'https://pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.046166021220217734'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        #防盗链:溯源，请求的上一级是什么
        'Referer': url
    }
    resp = requests.get(url=videoStatusUrl,headers=headers)
    dic = resp.json()
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic['systemTime']

    # https://video.pearvideo.com/mp4/short/20210726/cont-1736415-15729193-hd.mp4
    # https://video.pearvideo.com/mp4/short/20210726/1675154604880-15729193-hd.mp4

    srcUrl = srcUrl.replace(systemTime,'cont-'+contId)
    print(srcUrl)

    with open('a.mp4', "wb") as fp:
        fp.write(requests.get(srcUrl).content)