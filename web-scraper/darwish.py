import bs4
import urllib2
import html2text
from random import randint

# Create baseUrl

baseUrl = "http://www.azquotes.com/author/3659-Mahmoud_Darwish?page="

# Interate through various pages

for i in range(1,3):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="title")
    for quote in quotes:
        if len(quote.text) < 140:
            quote_final = quote.text.encode("utf-8")
            print "\""+quote_final+"\""
