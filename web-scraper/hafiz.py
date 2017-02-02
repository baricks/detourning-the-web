import bs4
import urllib2
import html2text
from random import randint

baseUrl = "https://www.goodreads.com/author/quotes/875661.Jalaluddin_Rumi?page="

for i in range(1,40):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="quoteText")
    for quote in quotes:
        if len(quote.text) < 140:
            quote_final = quote.text.encode("utf-8")
            print quote_final
