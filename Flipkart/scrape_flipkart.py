# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:01:08 2019

@author: Admin
"""
# Importing Requireed Libraries
from bs4 import BeautifulSoup 
import requests

# By using request libary feting the link of page we neeed to scrape the data  
source = requests.get("https://www.flipkart.com/search?q=elon+musk&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_0&otracker1=AS_QueryStore_HistoryAutoSuggest_1_0&as-pos=1&as-type=HISTORY")
# Parsing the page to Beautifulsoup
soup = BeautifulSoup(source.text,'html.parser')

print(soup.prettify)

# To find the list of books present in the page
books_1st = soup.findAll('div',{'class':'bhgxx2 col-12-12'})
len(books_1st)

price = soup.find('div',{'class':'_1vC4OE'})


containers = soup.findAll('div',{'class':'_3liAhj _1R0K0g'})
len(containers)
containers[0]

contain = containers[0]
container = containers[0]

# Creating a csv file with author detail,name of the book,offer price,before offer price
out_filename ="flipkart_Elonmusk.csv"

headers = 'Book_Name,Product_Author,Offer_price,Before_Offer_Price \n'

f = open(out_filename,"w")
f.write(headers)
for container in containers:
    book_name =container.find('a',{'class':'_2cLu-l'}).text.replace(",","") 

    product_author =container.find('div',{'class':'_1rcHFq'}).text.replace(",","") 
    
    offer_price = container.find('div',{'class':'_1vC4OE'}).text.replace("₹","").replace(",","")
    
    before_offer_price =container.find('div',{'class':'_3auQ3N'}).text.replace("₹","").replace(",","")
    
    print(book_name)
    print(product_author)
    print(offer_price)
    print(before_offer_price)
    
    f.write(book_name+","+product_author+","+offer_price+","+before_offer_price+"\n")
    
f.close()
















