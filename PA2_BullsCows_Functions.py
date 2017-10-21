#Functions for the Bulls and Cows Game.
from random import randint

#1Generates and stores seceret number.
def generateSecretNumb():
    secretNum = randint(0,9999)
    stringNum = str(secretNum)
    l = len(str(secretNum))
    return ((4-l)*"0" + stringNum)

#2Creats a list from var s
def findUniqueDigits(s):
    unqDigits = []
    for i in s:
        if unqDigits.count(i) == 0:
            unqDigits.append(i)
    return unqDigits

#3Finds and stores the ammount of Bulls
def findBulls(secret, guess):
    bulls = 0
    indexList = range(4)
    for i in indexList:
        if secret[i] == guess[i]:
            bulls += 1
    return bulls

#4Finds and stores the ammount of Cows
def findCows(secret, guess):
    bothBC = 0
    secretUniDigits = findUniqueDigits(secret)
    for i in secretUniDigits:
        secretCount = secret.count(i)
        guessCount = guess.count(i)
        bothBC += min(secretCount, guessCount)
    bulls = findBulls(secret, guess)
    return bothBC - bulls    
        
   
