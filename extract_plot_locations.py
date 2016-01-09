# coding: utf-8
import nltk
from nltk.tag.stanford import StanfordNERTagger
from geopy.geocoders import Nominatim
import csv
import re
from time import sleep

st = StanfordNERTagger('stanford-ner-2015-04-20/classifiers/english.all.3class.distsim.crf.ser.gz','stanford-ner-2015-04-20/stanford-ner.jar')



def loctag(tokes):
    tagged = st.tag(tokes)
    #locations = [ x[0] for x in tagged if x[1] == 'LOCATION' ]
    locations = []
    #manually iterating to facilitate multi-word location token grouping
    counter = 0 
    while counter < len(tagged):
        allword = []
        if tagged[counter][1] == 'LOCATION':
            allword.append(tagged[counter][0])
            position = 1
            while True:
                if tagged[counter+position][1] == 'LOCATION':
                    allword.append(tagged[counter+position][0])
                    position += 1
                else:
                    break
            counter += position
            fullloc = ' '.join(allword)
            locations.append(fullloc)
        else:
            counter += 1


    return locations

def loclookup(locations):
    geocator = Nominatim(timeout=120)
    
    ### Note: no comprehension to allow for 1 sec sleep
    #coordinates = [ geocator.geocode(x) 
    #                for x in locations
    #                if geocator.geocode(x) != None ]

    coordinates = {}

    unilocs = list(set(locations))

    for location in locations:
        try:
            geo = geocator.geocode(location)
            if geo != None:
                coordinates[location] = (geo.latitude,geo.longitude)
            else:
                coordinates[location] = (0.0,0.0)
        except GeocoderTimedOut as e:
            pass
        sleep(1)

    return coordinates.items()

def write_coords(coords,textname):
    with open(textname+'_locations.csv','w') as f:
        cwrite = csv.writer(f)
        cwrite.writerow(['name','latitude','longitude'])
        for x in coords[0]:
            cwrite.writerow([x[0],x[1][0],x[1][1]])


fname = input('Input filename')

with open(fname,'r') as f:
    text = f.read()

tokens = nltk.tokenize.word_tokenize(text)
tagged = loctag(tokens)
lookup = loclookup(tagged)
write_coords(lookup,fname)

