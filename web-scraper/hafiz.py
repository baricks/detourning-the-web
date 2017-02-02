import bs4
import urllib2
import html2text
from random import randint

# Run the following commands in the terminal to clean up the .txt file:
# sed -i.bak 's/$/"/' hafiz.txt

# Create baseUrl

baseUrl = "http://www.azquotes.com/author/37991-Hafez?page="

# Interate through various pages

for i in range(1,6):
    url = baseUrl + str(i)
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    quotes = soup.findAll(class_="title")
    for quote in quotes:
        if len(quote.text) < 140:
            quote_final = quote.text.encode("utf-8")
            print quote_final
