import requests
from bs4 import BeautifulSoup

keyword = 'coffee'
page_number="1"

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

for i in range(10):
    #r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword, headers=headers)
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+page_number, headers=headers)
    print('r.status_code=',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    #items = soup.select('.a-text-normal.a-color-base.a-size-base-plus')
    '''
    items = soup.select('.s-item__link > .s-item__title')
    for item in items:
        print('item=',item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    '''
    results = []
    boxes= soup.select('.clearfix.s-item__wrapper')
    for box in boxes:
        print('---')
        result = {}
        titles = box.select('.s-item__link > .s-item__title')
        for title in titles:
            print('title=',title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            print('price=',price.text)
            result['price'] = price.text
        statuses = box.select('.s-item__subtitle > .SECONDARY_INFO')
        for status in statuses:
            print('status=',status.text)
            result['status'] = status.text
        results.append(result)
        print('result=',result)
    print('len(results)=',len(results))

#import to json file

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
