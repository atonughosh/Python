import requests
from bs4 import BeautifulSoup

r = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(r.content, 'lxml')

def get_quote(i):
    #for i in range(len(soup.find_all("span",{"class":"text"}))):
    quote = (list(zip(soup.find_all("span", {"class":"text"})[i], soup.find_all("small", {"class":"author"})[i] )))
   # print(quote)
    for text,author in quote:
        print(text + " by " + author)

get_quote(0)            #pass an integer to pick a quote, program not yet complete,
                        # once complete the integer will be passed automaticaly
