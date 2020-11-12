import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# すべてのaタグを検索し、リンクを絶対URLで表示する
for element in soup.find_all('a'):
    print(element.text)
    url = element.get('href')
    link_url = urllib.parse.urljoin(load_url, url)
    print(link_url)

    

    
