'''
This scraper collects quotes from the web site http://quotes.toscrape.com 
and displays one at a time. On first run one quote will be displayed and then
the user is prompted to choose whether to display more quotes.
'''

import requests                                 #importing requests module
from bs4 import BeautifulSoup                   #importing BeautifulSoup

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

get_quote(0)            #pass an integer to pick a quote, program not yet complete,
                        # once complete the integer will be passed automaticaly
