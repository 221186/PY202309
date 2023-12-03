import os
import re
import requests
from collections import Counter
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import operator

url = 'https://quotes.toscrape.com/tag/life/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {'class': 'container'})

word_list = []
for quote in quotes:
    quote = quote.find_all('span', {'class': 'text'}) # 태그를 통해서 명언들을 모두 불러와 텍스트로 저장한다.
    for i in quote: # 명언들을 반복문을 통해 불러오고 텍스트와 소문자로 바꾸고 양 끝의 특수기호들을 공백으로 만든 후 단어들을 token화 한다.
        words = i.text.lower().replace('“', '').replace('”', '').replace('.', '').replace('-', '').split()
        word_list.extend(words) # 인용구들이 리스트 형태로 남아있으므로 extend함수를 이용해서 최종적으로 하나의 리스트 안에 token들이 들어있도록 한다.

word_count = {} # 단어들의 빈도수를 저장할 딕셔너리를 만든다.
for word in word_list:
    if word in word_count: # 만약 딕셔너리 안에 같은 단어가 있다면 1씩 추가한다
        word_count[word] += 1
    else: 
        word_count[word] = 1

# 빈도수가 상위 5개인 단어들과 그 빈도수를 저장한다.
top_five = sorted(word_count.items(), key = operator.itemgetter(1), reverse = True)

print('상위 5개의 단어')
for rank in range(1, 6): # 반복문을 통해 상위 5개의 순위를 만든다.
    word, count = top_five[rank - 1] # 현재 top_five에 저장된 첫 번째 단어의 인덱스가 0부터 시작하므로 rank - 1로 표현한다
    print(f'{rank}. {word}: {count}')

