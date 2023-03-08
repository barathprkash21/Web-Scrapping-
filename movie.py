import requests

from bs4 import BeautifulSoup

r = requests.get("https://www.ticketnew.com/online-advance-booking/Movies/C/Chennai")
c = r.content
print(c)
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
all=soup.find_all("div",{"class":"tn-movie tn-section-tile"})
print(all)
print(len(all))
print(all[0])
print(all[0].find_all("h4"))#price is defined by using tag and dimension array value
print(all[0].find_all("h4")[0].text) # to get only text
for item in all:   #to display all price value in the website
    print(item.find_all("h4")[0].text)
print(all[0].find_all("h4",{"class":"tn-single-line"}) )#price it is defined by using class name
print(all[0].find("h4",{"class":"tn-single-line"}) )
print(all[0].find("h4",{"class":"tn-single-line"}).text)
print(type(all[0].find("h4",{"class":"tn-single-line"}).text))
for item in all:   #to display all price value in the website
    print(item.find_all("h4")[0].text)
    print(item.find_all("div",{"class":"tn-inline"})[0].text)
    print(item.find_all("span",{"class":"tn-language tn-single-line"})[0].text)
    print(item.find_all("span",{"class":"genre"})[0].text)
    print("\n")
l=[]
for item in all:   #to display all price value in the website
    d={}
    d["movie_name"]=item.find_all("h4")[0].text
    #print(item.find_all("div",{"class":"tn-inline"})[0].text)
    d["movie_language"]=item.find_all("span",{"class":"tn-language tn-single-line"})[0].text
    d["movie_genre"]=item.find_all("span",{"class":"genre"})[0].text
    l.append(d)
print(l)
print(len(l))
import pandas
df=pandas.DataFrame(l)
print(df)
df.to_csv("ticket.csv")
