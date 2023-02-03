import requests,bs4,os
from pathlib import Path

os.makedirs('imagur_images',exist_ok=True)
search=input("enter what to search")
res=requests.get(f'https://imgur.com/search?q={search}')
res.raise_for_status()
parse=bs4.BeautifulSoup(res.text,'html.parser')
individualid=parse.select('div.post>a')
for i in individualid:
    x=i['href']
    url=f'https://imgur.com{x}'
    imagur_images=Path('imagur')
    res=requests.get(url)
    res.raise_for_status()
    imagefile=open(os.path.join('imagur_images',os.path.basename(url)),'wb')
    for chunk in res.iter_content(100000):
        imagefile.write(chunk)
    imagefile.close()
