'''
This scraper collects quotes from the web site http://quotes.toscrape.com 
and displays one at a time. On first run one quote will be displayed and then
the user is prompted to choose whether to display more quotes.
'''

import requests                                 #importing requests module
from bs4 import BeautifulSoup                   #importing BeautifulSoup

i = 0                                           #variable for indexing the quotes list generated after scraping

r = requests.get('http://quotes.toscrape.com')          #get the website contents into a request object
soup = BeautifulSoup(r.content, 'lxml')                 #Parse the r object using the lxml parser

#function to etract all quotes and return one quote at a time. The function expects and integer ar argument which 
#is used as the index of the quotes list created with all extracted quotes
def get_quote(i):
    #for i in range(len(soup.find_all("span",{"class":"text"}))):
    quote = (list(zip(soup.find_all("span", {"class":"text"})[i], soup.find_all("small", {"class":"author"})[i] )))
   # print(quote)
    for text,author in quote:
        print(text + " by " + author)

get_quote(i)                        #call function to diplay first quote i.e. by indexing quotes array with 0

while True:                         #infinite loop for user input and terminated by user
    more = input("Get more quote? (Y/N)\n")
    if more == 'Y' or more == 'y':
        i+=1
        get_quote(i)
    else:
        break
