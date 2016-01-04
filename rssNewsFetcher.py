import common
import feedparser
import pickle
import shutil
import datetime

def getTitles(url):
    titles = set()
    feed = feedparser.parse( url )
    for item in feed["items"]:
         titles.add(item['title'].replace('&#039;',"'").replace('\n', '').replace('\r', ''))
    return titles

def getNewRSSHeadlines(urlsdictionary, filePath):
    datetoday = datetime.datetime.now()
    print("Getting Headlines from Internets")
    for topic in urlsdictionary:
        print("Getting "+topic+" headlines")
        titles = set()
        rssdata = open((filePath+topic+'_'+datetoday.isoformat()+'.txt'), 'wb')
        for rss_url in urlsdictionary[topic]:
            titles = titles.union(getTitles(rss_url))
        pickle.dump(titles, rssdata)
        rssdata.close()
    return True

def getHeadlinesFromFile(filePath):
    print("Getting Headlines from File: " + filePath)
    rssprhases = open(filePath, 'rb')
    titles = pickle.load(rssprhases)
    rssprhases.close()
    return titles

def archiveRSSHeadlines():
    shutil.copy(common.headlineFilePath, common.archivedHeadlineFilePath)