# -*- coding: utf-8 -*-


import requests
import re
import pandas

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<div >,.*?strong*?>(\d+)</strong>',re.S)
    items = re.findall(pattern,html)
    print(items)
    for item in items:
        yield {
            'index':item[0],
        }
        
def main():
    url = 'https://masters.playgwent.com/en/rankings/pro-ladder/1'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)

if __name__ == '__main__':
    main()



