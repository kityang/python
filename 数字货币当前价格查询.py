import requests
from bs4 import BeautifulSoup as bs

url = "https://coinmarketcap.com/coins/"

soup = bs(requests.get(url).text,"html.parser")

tr = soup.table.contents[3].select('tr')
print("币种\t当前价格")
for i in tr:
    td = i.select('td')
    name = td[1].attrs["data-sort"]
    price =td[3].attrs["data-sort"]
    print(name+"\t"+price)
    
