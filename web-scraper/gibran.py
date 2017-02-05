import bs4
import urllib2
import unicodedata as ud

latin_letters= {}

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
           for uchr in unistr
           if uchr.isalpha())

baseUrl = "https://www.goodreads.com/author/quotes/6466154.Kahlil_Gibran?page="

# Interate through various pages

for i in range(1,66):
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
# python gibran.py > gibran.txt
# sed -i.bak '/Kahlil Gibran/d' ./gibran.txt
# sed -i.bak '/    ―/d' ./gibran.txt
# sed -i.bak '/^$/d' ./gibran.txt
# sed -i.bak 's/^[ \t]*//' ./gibran.txt
# sed -i.bak 's/$/ -Kahlil Ghibran/ ./gibran.txt
