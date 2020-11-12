import requests

# 画像ファイルを取得する
image_url = 'https://www.ymori.com/books/python2nen/sample1.png'
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split('/')[-1]

# 画像データをファイルに書き出す
with open(filename, mode='wb') as f:
    f.write(imgdata.content)
