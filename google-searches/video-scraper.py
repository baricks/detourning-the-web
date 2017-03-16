import bs4
import urllib2
import time
import re
import youtube_dl
from subprocess import call
from selenium import webdriver

driver = webdriver.PhantomJS()

# Create an array from the .txt file
with open("2014-howto.txt") as f:
    queryArray = []
    for line in f:
        search = line.rstrip('\n') + ' tutorial'
        wordArray = re.sub("[^\w]", " ",  search).split()
        query = '+'.join(wordArray)
        queryArray.append(query)
# print array

def get_video():
    time.sleep(1);
    print 'getting video'
    # returns a list of elements
    # videoURL = driver.find_elements_by_css_selector()
    title = driver.find_elements_by_css_selector('h3.yt-lockup-title')[0]
    print title.text
    videoURL = driver.find_element_by_css_selector('a.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link').get_attribute('href')
    print videoURL
    command = "youtube-dl -f 22 " + videoURL +" -c"
    call(command.split(), shell=False)
    # for video in titles:
    #     print title.text

for query in queryArray:
    url = 'http://www.youtube.com/results?search_query=' + query + '&sp=EgIYAQ%253D%253D'
    print url
    driver.get(url)
    get_video()

driver.quit()
print "quit"
