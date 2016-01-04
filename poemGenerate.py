import rhymeDBGenerate

def makelimericks(sylCountA,sylCountB,phrases):
    poemcountA = 0
    poemcountB = 0
    #print('sylA ')
    #print(phrases[sylCountA])
    #print('sylB ')
    #print(phrases[sylCountB])
    limerick = ['']*5
    limericks = []
    try:
        print("making limericks with A" + str(sylCountA) + " and B" + str(sylCountA))
        #Iterate through the titles in each final syllable key (list of rhying headlines)
        for finalSoundA in phrases[sylCountA]:
            #Don't bother trying if you can't make it
            if len(phrases[sylCountA][finalSoundA]) < 3:
                continue
            else:
                poemcountA = poemcountA+1
            for titlesA1 in phrases[sylCountA][finalSoundA]:
                limerick[0] = titlesA1
                for titlesA2 in phrases[sylCountA][finalSoundA]:
                    limerick[1] = titlesA2
                    for finalSoundB in phrases[sylCountB]:
                        #Don't bother trying if you can't make it
                        if len(phrases[sylCountB][finalSoundB]) < 2:
                            continue
                        else:
                            poemcountB = poemcountB+1
                        for titlesB1 in phrases[sylCountB][finalSoundB]:
                            limerick[2] = titlesB1
                            for titlesB2 in phrases[sylCountB][finalSoundB]:
                                limerick[3] = titlesB2
                                for titlesA3 in phrases[sylCountA][finalSoundA]:
                                    limerick[4] = titlesA3
                                    if islimerick(limerick) == True:
                                        limericks.append(limerick[:])
    except:
        print("no phrases for A=" + str(sylCountA) + " or B=" + str(sylCountA))
    if poemcountA == 0:
        print ("not enough phrases with " + str(sylCountA) + " syllables")
    if poemcountB == 0:
        print ("not enough phrases with " + str(sylCountB) + " syllables")
    return limericks

#just a sanity check
def islimerick(limerick):
    #ensure the same lines aren't used multiple times
    if limerick[0] == limerick[1]:
        #print('0 1 same')
        #print(limerick)
        return False
    if limerick[0] == limerick[4]:
        #print(limerick)
        #print('0 4 same')
        return False
    if limerick[1] == limerick[4]:
        #print(limerick)
        #print('1 4 same')
        return False
    if limerick[2] == limerick[3]:
        #print(limerick)
        #print('2 3 same')
        return False
    A1 = rhymeDBGenerate.syllableCount(limerick[0])
    A2 = rhymeDBGenerate.syllableCount(limerick[1])
    A3 = rhymeDBGenerate.syllableCount(limerick[4])
    B1 = rhymeDBGenerate.syllableCount(limerick[2])
    B2 = rhymeDBGenerate.syllableCount(limerick[3])
    #print(A1[1] + " and " + B1[1])
    #check not same rhyme
    if A1[1] == B1[1]:
        return False
    #Check they are not the same last words
    if A1[2] == A2[2]:
        return False
    if A1[2] == A3[2]:
        return False
    if A2[2] == A3[2]:
        return False
    if B1[2] == B2[2]:
        return False
    #ensure the lines rhyme
    if A1[1] == A2[1] == A3[1]:
        if B1[1] == B2[1]:
            #print(limerick)
            return True
    return False