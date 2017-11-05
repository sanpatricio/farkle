#!/usr/bin/python

import sys
import random
from collections import Counter

numDice = input("How many dice? ")
currCount = numDice

score = 0
setArray = []


def rollEm(dice):
    """ Roll the dice! """
    for i in range (0,dice):
        roll = int(random.randrange(1,dice,1))
        setArray.append(roll)

    if currCount > 0:
        return offerChoice(setArray)
    else:
        return "Game over!"

def offerChoice(rollSet):
    """ Offer the decisions to the player """
    print "You rolled:"
    n = 1
    for i in rollSet:
        print "Roll %i : %s" % (n,transToPips(i))
        n+=1

    return processChoice(raw_input("Which rolls are you keeping (Separate them by commas.  0 for none)? ").split(','),rollSet)

def processChoice(selection,values):
    """ Collect values of the player's choice and packages
    them in an array for the next function """

    selection_array = []

    for i in selection:
        i = int(i)
        i -= 1
        selection_array.append(values[i])

    print "You chose %s" % selection_array
    return countPips(selection_array)


def countPips(pips):
    """ Itemize the rolls and count the groupings to
    help determine scoring. """
    c = Counter(pips)
    score = 0

    for key,val in c.items():
        score = score + tallyScore(key,val)

    print "Total points: %s" % score

def tallyScore(roll,quantity):
    print "%s x %s" % (transToPips(roll), quantity)

    """ Scoring:
    1 = 10
    5 = 50
    3 x 1 = 1000
    3 x 2..6 = 2..6 x 100

    3 x Pairs = 500
    1..6 Straight = 1000
    No score = Farkle
    3 x Farkle = -1000 """

    poss1 = poss2 = poss3 = poss4 = 0

    if roll == 1 and quantity < 3:
        poss1 = roll * quantity * 10
    elif roll == 5 and quantity < 3:
        poss2 = roll * quantity * 10
    elif roll == 1 and quantity == 3:
        poss3 = 1000
    elif (roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6) and quantity == 3:
        poss4 = roll * 100
    else:
        pass

    possible = poss1+poss2+poss3+poss4
    print "This grouping is worth %s" % possible
    return possible

def diceLeft(origRoll,currCount,thisRoll):
    if origRoll - currCount != 0:
        message = currCount - thisRoll
    else:
        message = "Game over"

    return message

def transToPips(num):
    one   = u"\u2680"
    two   = u"\u2681"
    three = u"\u2682"
    four  = u"\u2683"
    five  = u"\u2684"
    six   = u"\u2685"

    I   = "[ I ]"
    II  = "[II ]"
    III = "[III]"
    IV  = "[IV ]"
    V   = "[ V ]"
    VI  = "[VI ]"

    if num == 1:
        return I
    elif num == 2:
        return II
    elif num == 3:
        return III
    elif num == 4:
        return IV
    elif num == 5:
        return V
    elif num == 6:
        return VI
    else:
        return "Wha happen?"

rollEm(numDice)
