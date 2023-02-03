import requests,bs4
from twilio.rest import Client

accountSID='**********************************'      #I have obtained the accountsid,authtoken and twilio no but will not be showing as it can be misused
authToken='********************************'

twilioCli=Client(accountSID,authToken)
mytwiliono='************'                               
myno='*************'
res=requests.get('https://weather.com/en-GB/weather/tenday/l/81cc0aa50e5a2f8287fd6848b8a6940233a43352ee461cf19c0dbd775515a51d')
res.raise_for_status()
parse=bs4.BeautifulSoup(res.text,'html.parser')
rain=parse.select('#detailIndex0 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2)')
#getting the rain chance percentage
rainper=str(rain[0].getText())
rainperno=rainper[:-1]
# print(rainperno)
if int(rainperno)>70:
    twilioCli.messages.create(body='Akshaya it might rain today,make sure to take an umbrlla',from_=mytwiliono,to=myno)


