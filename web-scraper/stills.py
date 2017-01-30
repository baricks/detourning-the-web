import urllib
from bs4 import BeautifulSoup

url = "https://film-grab.com/category/1969/"
html = urllib.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

articles = soup.findAll("article")

# get all the urls
for i in range(0, len(articles)):
    imgURL = articles[i].img['src']
    urllib.urlretrieve(imgURL, "images/1969/%s.jpg" % (i))
