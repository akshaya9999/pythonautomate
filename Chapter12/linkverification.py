import requests,bs4

res=requests.get('https://10fastfingers.com/')
res.raise_for_status()

parse=bs4.BeautifulSoup(res.text,'html.parser')
links=parse.select('a')

for i in links:
    # print(i['href'])
    href=i['href']
    ress=requests.get(f'https://10fastfingers.com{href}')
    if res.status_code==404:
        print(f"error in link https://10fastfingers.com{href}")
    else:
        print(f"link https://10fastfingers.com{href} is ok")

