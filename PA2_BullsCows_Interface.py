#Interface Bulls and Cows Game
from PA2_Functions import (generateSecretNumb, findBulls, findCows)
print("""Welcome to the Bulls and Cows Game.
The computer generates a number and you try and guess the number.
If you guess a correct number and it is in the correct position you
recieve a Bull. If you guess the correct number but it is in the
incorrect position, you recieve a Cow. Test your skills and give it
a shot!""")
secret = generateSecretNumb()
guess = raw_input("Enter your guess. Must be 4 digits")
while guess != secret:
    bulls = findBulls(secret, guess)
    cows = findCows(secret, guess)
    print str(bulls) + "Bulls" + str(cows) + "Cows"
    guess = raw_input("Enter your guess. Must be 4 digits:")
print "Thats it!"
    
