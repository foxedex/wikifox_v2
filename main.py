import requests as r
from bs4 import BeautifulSoup as bs
import os

s_title = str(input('Enter the title of the search : ')) #search title
link = f"https://en.wikipedia.org/w/index.php?go=Go&search={s_title}&title=Special%3ASearch&ns0=1"
os.system('cls')

page = r.get(link)
html = page.content
soup = bs(html, 'html.parser')
title = soup.find('title').text #title of search

if 'Search results' in title :
    lfr = [] #list of results
    cl = [] #chose list
    lfrh = soup.find_all('div', {'class': 'mw-search-result-heading'}) #list of results html
    for l in lfrh :
        html2 = str(l)
        soup2 = bs(html2, 'html.parser')
        lr = soup2.find('a').get('href') #link of result
        lfr.append('https://en.wikipedia.org'+lr)
        cl.append(l.text)  
    
    print('pleas chose from this list :\n')
    for c in range(len(cl)) :
        print(f'{c} {cl[c]}')
    print('\n')
    chosen = int(input('Select by the number : '))
    os.system('cls')
    item = lfr[chosen]
    page2 = r.get(item)
    html3 = page2.content
    soup3 = bs(html3, 'html.parser')

    titlefp = soup3.find('span', {'class': 'mw-page-title-main'}).text #title of the page
    print(titlefp)
    info = soup3.find_all('p')
    t = 0
    for p in info :
        if t > 3 :
            print("\n", p.text)
        if t == 6 :
            break
        t = t + 1

else :
    os.system('cls')
    titlefp = soup.find('span', {'class': 'mw-page-title-main'}).text #title of the page
    print(titlefp)
    info = soup.find_all('p')
    t = 0
    for p in info :
        print("\n", p.text)
        if t == 6 :
            break
        t = t + 1
    