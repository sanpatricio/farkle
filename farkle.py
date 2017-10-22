#!/usr/bin/python

import sys
import random
from collections import Counter

numDice = input("How many dice? ")

score = 0;
setArray = [];

def rollEm(dice):
    """ Roll the dice! """
    for i in range (0,dice):
        roll = random.randrange(1,dice,1)
        setArray.append(roll)
        print 'Roll %s: %s' % (i, roll)

    return setArray

def countPips(pips):
    """ Itemize the rolls and count the groupings to 
    help determine scoring. """
    c = Counter(pips)

    """ Scoring:
    1 = 10
    5 = 50
    3 x 2..6 = 2..6 x 100
    3 x 1 = 1000
    3 x Pairs = 500
    1..6 Straight = 1000
    No score = Farkle
    3 x Farkle = -1000 """

    for result in c:
        tallyScore(result)

    return c

def tallyScore(score):
    print "%s appeared %s times" % (score, score[score])

print countPips(rollEm(numDice))
