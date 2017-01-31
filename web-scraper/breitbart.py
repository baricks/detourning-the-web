import bs4
import urllib

url = "http://www.breitbart.com/"

html = urllib.urlopen(url).read()

# Make beautiful soup object
soup = bs4.BeautifulSoup(html, "html.parser")

# Grab the titles
titles = soup.select('h2.title')

for title in titles:
    print title.text.strip()
