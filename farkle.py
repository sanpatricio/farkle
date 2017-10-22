#!/usr/bin/python

import sys
import random
from collections import Counter

numDice = input("How many dice? ")

score = 0;
setArray = [];
one   = u"\u2680"
two   = u"\u2681"
three = u"\u2682"
four  = u"\u2683"
five  = u"\u2684"
sixe  = u"\u2685"

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

    for key,val in c.items():
        print tallyScore(key,val)

    #return c

def tallyScore(roll,quantity):
    print "%s appeared %s times" % (roll, quantity)

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

    return possible

countPips(rollEm(numDice))
