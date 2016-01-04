import datetime

datetoday = datetime.datetime.now()
rhymeDBFilePath = '/home/deanmcclure/poems/rhymedata/rhymeDB.txt'
limerickDBFilePath = '/home/deanmcclure/poems/rhymedata/limerickDB.txt'
archivedHeadlineFilePath = '/home/deanmcclure/poems/rssdata/data_' #+datetoday.isoformat()+'.txt'
archivedHeadlinePath  = '/home/deanmcclure/poems/rssdata/'
archivedPoemFilePath = '/home/deanmcclure/poems/poems_'+datetoday.isoformat()+'.csv'
PoemFilePath = '/home/deanmcclure/poems/poemsNow.csv'
UserPoemFilePath_Limericks = '/home/deanmcclure/poems/UserPoems_Limerick.csv'

rssTimeWindowSec = (7*24*60*60)

urlListSport = ['http://www.abc.net.au/news/feed/45924/rss.xml'
               ]

urlListPolitics = ['http://www.crikey.com.au/politics/feed/', 'http://www.telegraph.co.uk/news/politics/rss',
                    'http://www.smh.com.au/rssheadlines/political-news/article/rss.xml'
                  ]

urlListEntertainment = ['http://www.abc.net.au/news/feed/46800/rss.xml', 'http://www.crikey.com.au/media/feed/',
                        'http://www.crikey.com.au/life/feed/', 'http://feeds.news.com.au/public/rss/2.0/news_ent_3169.xml',
                        'http://feeds.news.com.au/public/rss/2.0/aus_media_57.xml'
                       ]

urlListBusiness = ['http://www.abc.net.au/news/feed/51892/rss.xml', 'http://www.crikey.com.au/business/feed/'
                  ]

urlListEvents = ['http://www.abc.net.au/news/feed/51120/rss.xml', 'http://www.abc.net.au/news/feed/45910/rss.xml',
                 'http://www.abc.net.au/news/feed/52278/rss.xml'
                ]

urlListAustralia = ['http://www.abc.net.au/news/feed/46182/rss.xml', 'http://feeds.news.com.au/public/rss/2.0/news_national_3354.xml',
                    'http://feeds.news.com.au/public/rss/2.0/aus_arts_51.xml', 'http://sbs.feedsportal.com/c/34692/f/637524/index.rss',
                    'http://www.smh.com.au/rssheadlines/national/article/rss.xml'
                   ]

urlListMisc = ['http://www.abc.net.au/news/feed/1054578/rss.xml', 'http://www.crikey.com.au/feed/',
                'http://www.aljazeera.com/xml/rss/all.xml', 'http://feeds.news.com.au/public/rss/2.0/news_lifestyle_3171.xml',
                'http://sbs.feedsportal.com/c/34692/f/637528/index.rss', 'http://www.smh.com.au/rssheadlines/comment/article/rss.xml',
                'http://www.jw.org/en/news/rss/FullNewsRSS/feed.xml', 'http://english.pravda.ru/export.xml', 'http://english.pravda.ru/health/export.xml',
                'http://www.globalresearch.ca/feed'
              ]

urlLists = {'sports': urlListSport, 'politics': urlListPolitics, 'entertainment': urlListEntertainment, 'business': urlListBusiness, 'events': urlListEvents, 'australia': urlListAustralia, 'misc': urlListMisc}
