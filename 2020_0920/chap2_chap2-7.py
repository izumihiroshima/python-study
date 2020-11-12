import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = 'http://www.omame.com'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# classで検索し、その中のすべてのaタグを検索して表示する
topic = soup.find(class_='topicsList_main')
for element in topic.find_all('li'):
    print(element.text)
    


    



