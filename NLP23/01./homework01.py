import requests
from bs4 import BeautifulSoup
import re

def getHtml(url):
    r = requests.get(url)
    r.encoding=r.apparent_encoding
    text = r.text
    # print(text)
    return text

def getInfo(url):
    allData = []
    text = getHtml(url)
    soup = BeautifulSoup(text,'html.parser')
    list = soup.find_all('li')
    #81,167
    for i in range(81,167):
        # print(i)
        title = list[i].find('a',class_='note')
        aut = list[i].find('font')
        date = list[i].find('cite',class_="date")
        site = "http://guba.eastmoney.com"+title.attrs['href']
        # print(site)
        # print("title:",title.attrs['title'],'\n','aut:',aut.string,'\n','date:',date.text)
        data = [title.attrs['title'], aut.string, date.text,site]
        # write data to result.txt
        with open('/home/zhguo/git/NLP23/01./result.txt','a') as f:
            f.write('\n'.join(data))

        
        # get whole news according to the site
        # r = getHtml(site)
        # soup = BeautifulSoup(r,"html.parser")
        # r = soup.find('div',class_="xeditor_content editorlungo_content")
        # r = str(r)


for i in range(1,2):
    url = f'http://guba.eastmoney.com/default,99_{i}.html'
    getInfo(url)

