import requests,bs4,os

os.makedirs('imgurcat',exist_ok=True)
url='https://imgur.com'
search=input("enter search")
res=requests.get(url+search)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'html.parser')
results=soup.select()