# -*- coding: utf-8 -*-

# This is a simple python script that requests the name of a book/author 
# and prints out the top 30 relevant quotes as found on Goodreads (www.goodreads.com)

# This script uses BeautifulSoup-4 to perform the final html parsing to retrieve the quotes and
# a python wrapper for the Goodreads API to retrieve the relevant bookID from the given string raw_input

# Link to the python wrapper: https://github.com/sefakilic/goodreads 

from goodreads import client
from goodreads import book
import re
import requests
import urllib

from bs4 import BeautifulSoup


def cleanedUpQuote(quote):              # To remove stray html tags from the retrieved results
    quote = re.sub('<.*?>','',quote)
    return quote


CONSUMER_KEY = "AL6GKEoebHFenfoDmtHuOA"
CONSUMER_SECRET ="WFelKpMYYwRTOelTyJF449HYuMadDBflYaocGQh4lqk"


gc = client.GoodreadsClient(CONSUMER_KEY,CONSUMER_SECRET)

#gc.authenticate()

bookName = raw_input("Enter the name of your favorite book(Enter Author's name to retrive top quotes from the author): ")

print "Hold on while we retrieve the top quotes..."

#bookIdList = gc.search_books(bookName)
#How to declare bookName as an instance of book. bookname = book(x, x, x)
r = requests.get('https://www.goodreads.com/book/title.xml?key=%s&title=%s' % (CONSUMER_KEY, bookName))
print r
soup = BeautifulSoup(r.text)
book_id = soup.find('book').find('work').find('id').text
print book_id
baseUrl = 'https://www.goodreads.com/work/quotes/'
editedBookName = bookName.replace(' ','-')
s = book_id+'-'+editedBookName
print "s is", s
print "editedbookname is", editedBookName
finalUrl = str(baseUrl) + str(s);
#finalUrl =  "https://www.goodreads.com/work/quotes/2368224-Ulysses"
print "finalURL is: ", finalUrl


# print finalUrl

print "..............."
print 
print 

html = urllib.urlopen(finalUrl).read()
soup = BeautifulSoup(html,"lxml")

# print soup
quotesPart = soup.findAll("div",class_="quoteText")

for item in quotesPart:
    tex = str(item)

    matchQ = re.findall('“(.*)”',tex)
    print cleanedUpQuote(matchQ[0])
    print 
    print
