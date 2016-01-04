import common
import rhymeDBGenerate
import pickle
import datetime

def buildLimerickDB():
    print("Building LimcerickDB")
    starttime = datetime.datetime.now() #time how long to analyse set
    sylCountA = [9,8]
    sylCountB = [6,5]
    headlinesA = {}
    headlinesB = {}
    rhymeDB = rhymeDBGenerate.getRhymeDB()
    for sylCount in sylCountA:
        headlinesA[sylCount] = {}
        for finalSoundA in rhymeDB[sylCount]:
            if len(rhymeDB[sylCount][finalSoundA]) >= 3:
                headlinesA[sylCount][finalSoundA] = set()
                for title in rhymeDB[sylCount][finalSoundA]:
                    headlinesA[sylCount][finalSoundA].add((title))
                #Because some of the headlines are the same but you don't know until it is in a set
                if len(headlinesA[sylCount][finalSoundA]) < 3: headlinesA[sylCount].pop(finalSoundA,None)
    for sylCount in sylCountB:
        headlinesB[sylCount] = {}
        for finalSoundB in rhymeDB[sylCount]:
            if len(rhymeDB[sylCount][finalSoundB]) >= 2:
                headlinesB[sylCount][finalSoundB] = set()
                for title in rhymeDB[sylCount][finalSoundB]:
                    headlinesB[sylCount][finalSoundB].add((title))
                #Because some of the headlines are the same but you don't know until it is in a set
                if len(headlinesB[sylCount][finalSoundB]) < 2: headlinesB[sylCount].pop(finalSoundB,None)
    phrases = [headlinesA, headlinesB]
    LimerickDB = open(common.limerickDBFilePath, 'wb')
    pickle.dump(phrases, LimerickDB)
    LimerickDB.close()
    print ('Making LimerickDB from RhymeDB set took ' + str(datetime.datetime.now() - starttime) +' to run')
    return phrases

#gets the dictionary off filesystem
def getLimerickDB():
    print("Getting Rhyme DB off File")
    LimerickDB = open(common.limerickDBFilePath, 'rb')
    phrases = pickle.load(LimerickDB)
    LimerickDB.close()
    return phrases