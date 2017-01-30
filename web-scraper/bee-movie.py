import bs4
import urllib

url = "http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html"

html = urllib.urlopen(url).read()

# Make beautiful soup object
soup = bs4.BeautifulSoup(html, "html.parser")

# Grab the titles
titles = soup.select('pre')

for title in titles:
    print title.text.strip()
