from nltk.corpus import cmudict
from nltk.tokenize import RegexpTokenizer
import os.path, time
import datetime
import common
import rssNewsFetcher
import pickle

d = cmudict.dict() # get the CMU Pronouncing Dict
phrasetokenizer = RegexpTokenizer(r"[\w| |\-|\'|\‘|\’|\$]+")
wordtokenizer = RegexpTokenizer(r"[\w+|\']+")
soundtokenizer = RegexpTokenizer(r"[A-Z]+")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def nsyl(word):
    """return the max syllable count in the case of multiple pronunciations"""
    lastsound = ''
    syllables = 0
    try:
        if isinstance(d[word.lower()], list):
            word = d[word.lower()][0]
        for sound in word:
            if hasNumbers(sound):
                syllables = syllables+1
                lastsound = ''
            #append last sound
            lastsound += soundtokenizer.tokenize(sound)[0]
    #If there is no word found it waste the whole line
    except:
        return -1, None
    return syllables, lastsound

def syllableCount(text):
    """return the max syllable count in the case of multiple pronunciations"""
    syllables = 0
    try:
        for word in wordtokenizer.tokenize(text):
            syllables = syllables + nsyl(word)[0]
            if nsyl(word)[0] == -1:
                return 0, None
        return syllables, nsyl(word)[1], word
    except:
        return 0, None

#builds a dictionary for looking up rhyming data
def buildRhymeDB():
    print("Getting News Titles for Rhyme DB")
    phrases = {}
    newstitles = importTitles(common.archivedHeadlinePath)
    #break titles up into subtitles and then collect pronounciation data
    print("Building Rhyme DB")
    starttime = datetime.datetime.now() #time how long to analyse set
    for title in newstitles:
        for subtitle in (phrasetokenizer.tokenize(title)):
            subtitle = subtitle.strip().replace(u'\u2019', u'\'').encode('ascii', 'ignore').decode('ascii').lower()
            #subtitle = subtitle.strip()
            info = syllableCount(subtitle)
            try:
                phrases[info[0]][info[1]].append(subtitle)
            except:
                try:
                    phrases[info[0]][info[1]] = []
                    phrases[info[0]][info[1]].append(subtitle)
                except:
                    phrases[info[0]]={}
                    phrases[info[0]][info[1]] = []
                    phrases[info[0]][info[1]].append(subtitle)
    RhymeDB = open(common.rhymeDBFilePath, 'wb')
    pickle.dump(phrases, RhymeDB)
    RhymeDB.close()
    print ('Making rhymeDB from titles set took ' + str(datetime.datetime.now() - starttime) +' to run')
    return phrases

#goes through list of lists of RSS feeds and makes a set of all
def importTitles(dir):
    starttime = datetime.datetime.now() #time how long to make set
    titles = set()
    for file in os.listdir(dir):
        file = str(dir + "/" + file)
        #Import all RSSfeed data from the last week
        if os.path.isfile(file):
            if (os.path.getmtime(file) > (time.time() - common.rssTimeWindowSec)) and (os.path.getsize(file) > 0) :
                titles = titles.union(rssNewsFetcher.getHeadlinesFromFile(file))
    print ('Making SET from RSS title files took ' + str(datetime.datetime.now() - starttime) +' to run')
    return titles

#gets the dictionary off filesystem
def getRhymeDB():
    print("Getting Rhyme DB off File")
    RhymeDB = open(common.rhymeDBFilePath, 'rb')
    phrases = pickle.load(RhymeDB)
    RhymeDB.close()
    return phrases


#phrasetokenizer.tokenize
