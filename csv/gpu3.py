from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.thevaluestore.in/graphic-cards-online-india"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
details = soup.select('#content > div > div.products-list.row.nopadding-xs')
#print(details)
content = str(details[0])
soup = BeautifulSoup(content, "html.parser")
table_rows = soup.findAll("div",{"class":"price"})
stars=soup.findAll("div",{"class":"rating-box"})
number=soup.findAll("a",{"class":"rating-num"})
final_list=[]
for i in table_rows:
     list=[]
     soup = BeautifulSoup(str(i), "html.parser")
     data = soup.findAll("span",{"class":"price-new"})
     a=str(data[0].text[1:])
     #print(int(a.replace(',','')))
     list.append(int(a.replace(',','')))
     final_list.append(list)
#print(final_list)
#print(len(final_list))
# print(len(final_list))
l=[]
for k in stars :
     soup=BeautifulSoup(str(k),"html.parser")
     ratings=soup.findAll("i",{"class":"fa fa-star fa-stack-1x"})
     #print(len(ratings))
     l.append(len(ratings))
#print(l)
s=0
for i in final_list:
     i.append(l[s])
     s+=1
#print(final_list)
num=[]
for i in number:
    a=i.text[1]
    num.append(int((a)))
c=0
for i in final_list:
    i.append(num[c])
#print(final_list)
print(final_list)
with open('data.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(final_list)
