
import requests
from bs4 import BeautifulSoup
baseurl='https://www.itcstore.in/staples'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

r=requests.get('https://www.itcstore.in/staples')
soup=BeautifulSoup(r.content,'lxml')
productlist=soup.find_all('div',class_='product-link cursor-pointer')
print(productlist)
productlinks=[]
for x in range(1,21):
  r=requests.get('https://www.itcstore.in/staples?page='+str(x))
  soup=BeautifulSoup(r.content,'lxml')
  productlist=soup.find_all('div',class_='product-link cursor-pointer')
  # print(productlist)

  for item in productlist:

    for link in item.find_all('a', href=True):
      productlinks.append(baseurl+link['href'])


print(len(productlinks))
print(productlinks)




df=pd.DataFrame({"Product Links":productlinks })
print(df)
df.to_csv("Product_Links.csv")
