from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.tpstech.in/collections/graphics-card"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
details = soup.select('#product-list')
#print(details)
content = str(details[0])
soup = BeautifulSoup(content, "html.parser")
table_rows = soup.findAll("div",{"class":"product-item__price-list price-list"})
stars=soup.findAll("div",{"class":"rating__stars"})
number=soup.findAll("span",{"class":"rating__caption"})
final_list=[]
for i in table_rows:
    list=[]
    soup = BeautifulSoup(str(i), "html.parser")
    data = soup.findAll("span")
    a=str(data[0].text)[15:]
    #print(float(a.replace(',','')))
    list.append(float(a.replace(',','')))
    final_list.append(list)
#print(final_list)
print(len(final_list))
l=[]
for k in stars :
    soup=BeautifulSoup(str(k),"html.parser")
    ratings=soup.findAll("svg",{"class":"icon icon--rating-star rating__star rating__star--full"})
    #print(len(ratings))
    l.append(len(ratings))
#print(l)
s=0
for i in final_list:
    i.append(l[s])
    s+=1
num=[]
for i in number:
    num.append(int(i.text[:2]))
c=0
for i in final_list:
    i.append(num[c])
    c+=1
print(final_list)
final_list.insert(0,["price","ratings","reviews"])
#print(final_list)
with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(final_list)


    
    