from bs4 import BeautifulSoup
import requests

url = 'https://www.techolas.com/'
content=requests.get(url)
soup=BeautifulSoup(content.text,'html.parser')

# print the content of the web page 
# print(soup)

# finding all li elements with class='nav-item'
data=soup.find_all('li',class_='nav-item')

for d in data:
    print(d.text)