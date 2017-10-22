import requests
import pandas
import json
import time
from bs4 import BeautifulSoup

def basicinfo(url):#文章内容
    article = {}
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    article['name'] = soup.select('.post-title')[0].text
    article['author'] = soup.select('.auhtor-title')[0].text
    article['url'] = url
    article['date'] = soup.select('.post-meta time')[0].text
    article['view'] = soup.select('.post-views')[0].text.lstrip('阅读 ')
    article['view'] = soup.select('.post-views')[0].text.lstrip('阅读 ')
    article['comment'] = soup.select('.post-comment-count')[0].text.lstrip('评论 ')
    article['bookmark'] = soup.select('.post-mark')[0].text.lstrip('收藏 ')
    article['content'] = ''.join([p.text.strip() for p in soup.select('.entry-content p')])
    return article

def link(url):#提取分页
    content = []
    res =requests.get(url)
    jd = json.loads(res.text)['payload']
    for ent in jd:
        content.append(basicinfo(ent['permalink']))
    return content

news_total = []
url = 'http://www.woshipm.com/__api/v1/stream-list?paged={}'

for i in range(1,5):#轮询页面，获取页面URL
    url1 =url.format(i)
    newsary = link(url1)
    news_total.extend(newsary)
    time.sleep(1)
df = pandas.DataFrame(news_total)
df.to_csv('PM 900.csv',index=False)