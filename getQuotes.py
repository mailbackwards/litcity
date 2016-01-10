# -*- coding: utf-8 -*-

# This is a simple python script that requests the name of a book/author 
# and prints out the top 30 relevant quotes as found on Goodreads (www.goodreads.com)

# This script uses BeautifulSoup-4 to perform the final html parsing to retrieve the quotes and
# a python wrapper for the Goodreads API to retrieve the relevant bookID from the given string raw_input

# Link to the python wrapper: https://github.com/sefakilic/goodreads

#                                       ---

# This file was borrowed from: https://github.com/mon95/Goodreads-Quotes-Extractor/blob/master/getQuotes.py

# import libraries
from goodreads import client
from goodreads import book
import re
import requests
import urllib
from bs4 import BeautifulSoup

# clean up quotes
def cleanedUpQuote(quote):       
    quote = re.sub('<.*?>','',quote)
    return quote


CONSUMER_KEY = "AL6GKEoebHFenfoDmtHuOA"
CONSUMER_SECRET ="WFelKpMYYwRTOelTyJF449HYuMadDBflYaocGQh4lqk"

gc = client.GoodreadsClient(CONSUMER_KEY,CONSUMER_SECRET)

#gc.authenticate() -- OAuth may be unneccasary

bookName = raw_input("Enter the name of your favorite book(Enter Author's name to retrive top quotes from the author): ")

print "Hold on while we retrieve the top quotes..."

r = requests.get('https://www.goodreads.com/book/title.xml?key=%s&title=%s' % (CONSUMER_KEY, bookName))
soup = BeautifulSoup(r.text)
book_id = soup.find('book').find('work').find('id').text
baseUrl = 'https://www.goodreads.com/work/quotes/'
editedBookName = bookName.replace(' ','-')
s = book_id+'-'+editedBookName
# construct the final URL that will retrieve quotes
finalUrl = str(baseUrl) + str(s);


print "..............."
print 
print 

html = urllib.urlopen(finalUrl).read()
soup = BeautifulSoup(html,"lxml")

quotesPart = soup.findAll("div",class_="quoteText")

for item in quotesPart:
    tex = str(item)

    matchQ = re.findall('“(.*)”',tex)
    print cleanedUpQuote(matchQ[0])
    print 
    print
