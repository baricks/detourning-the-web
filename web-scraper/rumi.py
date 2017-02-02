import bs4
import urllib2
import html2text
from random import randint

# Run the following commands in the terminal to clean up the .txt file:
# python rumi.py > rumi.txt
# sed -i.bak '/Jalaluddin Rumi/d' ./rumi.txt
# sed -i.bak '/    ―/d' ./rumi.txt
# sed -i.bak '/^$/d' ./rumi.txt
# sed -i.bak 's/^[ \t]*//' ./rumi.txt

# Create baseUrl

baseUrl = "https://www.goodreads.com/author/quotes/875661.Jalaluddin_Rumi?page="

# Interate through various pages

for i in range(1,40):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="quoteText")
    for quote in quotes:
        if len(quote.text) < 140:
            quote_final = quote.text.encode("utf-8")
            print quote_final
