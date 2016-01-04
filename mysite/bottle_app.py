from bottle import default_app, route, get, request, response
import csv
import os
import random
import common
from nltk.tokenize import RegexpTokenizer
import html.parser
import rhymeDBGenerate
import limerickDBGenerate
from functools import reduce
#import binascii
#import BeautifulSoup

LatestPoemFilePath = '/home/deanmcclure/poems/poemsNow.csv'
tokenizer = RegexpTokenizer(r"[\w| |\-|\'|\‘|\’|\$]+")
html_parser = html.parser.HTMLParser()

@route('/')
def getRandPoemwithText():
    poemhtml = ""
    limerickDB = limerickDBGenerate.getLimerickDB()
    SylA = random.choice(list(limerickDB[0].keys()))
    SylB = random.choice(list(limerickDB[1].keys()))
    LinesA = random.sample(limerickDB[0][SylA][random.choice(list(limerickDB[0][SylA]))],3)
    LinesB = random.sample(limerickDB[1][SylB][random.choice(list(limerickDB[1][SylB]))],2)
    poemhtml+="<center><font size='5'><b>Why computers and journalists shouldn't write poetry</b><br></font>"
    poemhtml+="<font size='2'>Hit refresh for another random poem </font><br> <br>"
    poemhtml+="<font size='4'>"
    poemhtml+=str(html_parser.unescape(LinesA[0]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesA[1]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesB[0]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesB[1]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesA[2]))+"<br>"
    poemhtml+="</font>"
    poemhtml+="<br><font size='1'>"
    poemhtml+="<br> all poems generated from news headlines"
    #poemhtml+="<br> click <a href='custom/limerick'>here</a> to make a custom limerick"
    poemhtml+="<br> click <a href='poemonly'>here</a> for poem only"
    poemhtml+="</center></font>"
    return poemhtml

@route('/poemonly')
def getRandPoem():
    poemhtml = ""
    limerickDB = limerickDBGenerate.getLimerickDB()
    SylA = random.choice(list(limerickDB[0].keys()))
    SylB = random.choice(list(limerickDB[1].keys()))
    LinesA = random.sample(limerickDB[0][SylA][random.choice(list(limerickDB[0][SylA]))],3)
    LinesB = random.sample(limerickDB[1][SylB][random.choice(list(limerickDB[1][SylB]))],2)
    poemhtml+=str(html_parser.unescape(LinesA[0]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesA[1]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesB[0]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesB[1]))+"<br>"
    poemhtml+=str(html_parser.unescape(LinesA[2]))+"<br>"
    return poemhtml

@route('/custom/limerick', methods=['GET'])
def customLimerick():
    response.content_type = 'text/html; charset=UTF-8'
    line1 = request.query.line1.replace("%27","'").replace("%22","\"")
    line2 = request.query.line2.replace("%27","'").replace("%22","\"")
    line3 = request.query.line3.replace("%27","'").replace("%22","\"")
    line4 = request.query.line4.replace("%27","'").replace("%22","\"")
    line5 = request.query.line5.replace("%27","'").replace("%22","\"")

    limerickDB = limerickDBGenerate.getLimerickDB()
    SylA = random.choice(list(limerickDB[0].keys()))
    SylB = random.choice(list(limerickDB[1].keys()))

    #headlinesA = map(lambda s: s.encode('ascii', 'ignore'), (limerickDB[0][SylA]))
    headlinesA = reduce(set.union, (set(soundgroups) for soundgroups in (limerickDB[0][SylA].values())))
    headlinesB = reduce(set.union, (set(soundgroups) for soundgroups in (limerickDB[1][SylB].values())))
    #(headlinesA, headlinesB) = makeLimerickRhymeList()
    poemhtml="<html><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>"
    poemhtml+= "<head><center><font size='5'><b>Make a Custom News Headline Limerick</b><br></font>"
    poemhtml+= "<script src='https://code.jquery.com/jquery-1.10.2.js'></script></head><body><br>"
    if line5 == "":
        poemhtml+= "<form action='/custom/limerick' method='get'>"
    else:
        poemhtml+= "<form action='/custom/limericksave' method='get'>"
    #poemhtml+= "<form action='/custom/limericksave' method='get'>"
    if line1 == "":
        poemhtml+= "<p>First Line:<select name='line1'>"
        for title in headlinesA:
            poemhtml+="""<option value=\""""+str(title[0])+"""\">"""+str(title[0])+"""</option>"""
        poemhtml+="</select></p>"
    else:
        poemhtml+= line1+"""<br> <input type='hidden' name='line1' value=\""""+line1+"""\">"""
        Adata = rhymeDBGenerate.syllableCount(line1)
        if line2 == "":
            poemhtml+= "<p>Second Line:<select name='line2'>"
            for title in headlinesA:
                if title[1] == Adata[1] and title[2] == Adata[0]:
                    poemhtml+="""<option value=\""""+str(title[0])+"""\">"""+str(title[0])+"""</option>"""
            poemhtml+="</select></p>"
        else:
            poemhtml+= line2+"""<br> <input type='hidden' name='line2' value=\""""+line2+"""\">"""
            if line3 == "":
                poemhtml+= "<p>Third Line:<select name='line3'>"
                for title in headlinesB:
                    poemhtml+="""<option value=\""""+str(title[0])+"""\">"""+str(title[0])+"""</option>"""
                poemhtml+="</select></p>"
            else:
                poemhtml+= line3+"""<br> <input type='hidden' name='line3' value=\""""+line3+"""\">"""
                Bdata = rhymeDBGenerate.syllableCount(line3)
                if line4 == "":
                    poemhtml+= "<p>Fourth Line:<select name='line4'>"
                    for title in headlinesB:
                        if title[1] == Bdata[1] and title[2] == Bdata[0]:
                            poemhtml+="""<option value=\""""+str(title[0])+"""\">"""+str(title[0])+"""</option>"""
                    poemhtml+="</select></p>"
                else:
                    poemhtml+= line4+"""<br> <input type='hidden' name='line4' value=\""""+line4+"""\">"""
                    if line5 == "":
                        poemhtml+= "<p>Final Line:<select name='line5'>"
                        for title in headlinesA:
                            if title[1] == Adata[1] and title[2] == Adata[0]:
                                poemhtml+="""<option value=\""""+str(title[0])+"""\">"""+str(title[0])+"""</option>"""
                        poemhtml+="</select></p>"
                    else:
                        poemhtml+= line5+"""<br> <input type='hidden' name='line5' value=\""""+line5+"""\">"""
    if line5 == "":
        poemhtml+="<input value='Next' type='submit' />"
        #pass
    else:
        poemhtml+="<br><input value='Save' type='submit' /><br>"
    poemhtml+="<br><font size='2'>"
    poemhtml+="<br><a href = 'limerick'>Start Again</a>"
    poemhtml+="</font>"
    poemhtml+="<br><font size='1'>"
    poemhtml+="<br> back to <a href='/'>random poems</a>"
    poemhtml+="</center></font>"
    poemhtml+="</form></body></html>"
    #rhymeDBGenerate.syllableCount()

    return poemhtml

    #GET https://www.example.com/login.php?user=mickey&passwd=mini
    #(headlinesA, headlinesB) = makeLimerickRhymeList()

@route('/custom/limericksave', methods=['GET'])
def savecustomLimerick():
    #make csv file to store poems

    response.content_type = 'text/html; charset=UTF-8'
    line1 = request.query.line1
    line2 = request.query.line2
    line3 = request.query.line3
    line4 = request.query.line4
    line5 = request.query.line5

    csv = line1 + "\r\n" + line2 + "\r\n" + line3  + "\r\n" + line4 + "\r\n" + line5
    response.headers["Content-Disposition"] = "attachment; filename=poem.txt"
    return csv

application = default_app()