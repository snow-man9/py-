
from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open('./bilibili.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup.a) #soup.tagName返回的是html中第一次出现的tagName
    # print(soup.find('a'))
    # print(soup.find_all('a'))
    print(soup.select('.biliMainFooter'))