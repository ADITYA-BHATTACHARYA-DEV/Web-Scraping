import requests
from bs4 import BeautifulSoup 
import pandas as pd

Names=[] 
Prices=[] 
for i in range(1,22):
  response=requests.get('https://www.itcstore.in/staples?page='+str(i))
  print(response)
  soup=BeautifulSoup(response.text,'lxml')
#If more things are available below the pagination bar and if you want to remoove it use
#box=soup.find("div",class_="")
#items=box.find_all('span',class_="")
#It means first you find the box where all the the data is stored as a container then from that box extract data 
  items=soup.find_all('span',class_='text-[12px] lg:text-[14px] !min-h-[38px] product_productTitle__L_JgZ')
  print(items)
  for i in items:
   name=i.text
   Names.append(name)
  print(Names)
  prices=soup.find_all('span',class_='!text-[16px] lg:text-[18px] product_pricingText__9XGb_')
  print(prices)
  for p in prices:
   pr=p.text
   Prices.append(pr)
  print(Prices)

df=pd.DataFrame({"Product Name": Names,"Prices":Prices})
print(df)
df.to_csv("Staples.csv")
