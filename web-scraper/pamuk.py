import bs4
import urllib2
import html2text
from random import randint
import unicodedata as ud

# First run the code below for Goodreads quotes

latin_letters= {}

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
           for uchr in unistr
           if uchr.isalpha())

baseUrl = "https://www.goodreads.com/author/quotes/1728.Orhan_Pamuk?page="

# Interate through various pages

for i in range(1,23):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="quoteText")
    for quote in quotes:
        if len(quote.text) < 140:
            if only_roman_chars(quote.text) is True:
                quote_final = quote.text.encode("utf-8")
                print quote_final

# Run the following commands in the terminal to clean up the .txt file:
# python pamuk.py > pamuk.txt
# sed -i.bak '/Orhan Pamuk/d' ./pamuk.txt
# sed -i.bak '/    ―/d' ./pamuk.txt
# sed -i.bak '/^$/d' ./pamuk.txt
# sed -i.bak 's/^[ \t]*//' ./pamuk.txt


# Second, run code below for AZQuotes quotes.

# Create baseUrl

baseUrl = "http://www.azquotes.com/author/11281-Orhan_Pamuk?page="

# Interate through various pages

for i in range(1,8):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="title")
    for quote in quotes:
        if len(quote.text) < 140:
            quote_final = quote.text.encode("utf-8")
            print "\""+quote_final+"\""
