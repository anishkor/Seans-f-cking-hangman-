import random

# Sean You moron. You know what Random Is! You wanted comments You're getting them
# ITS A LIBRARY! WOO HOO!@

name = input("What is your name? ")
# This code explains the meaning of cricket and how Shaw is hella underrated. No it asks for the name and takes the input.

print("Good Luck ! ", name)
#Good Luck Bud It says good luck

words = ['Mallinga', 'Powell', 'Rashid', "Rahul",
         'Bumrah', 'Virat', 'Kohli', 'Cricket',
         'Sean', 'Is', 'an', 'Idiot' , "and" , "An" , "annoyance" ,
         "for" , "making" , "me" , "do" , "comments"]

# Dese are my words. Like em?
word = random.choice(words)

print("Guess Douche")

Rhajapashkas = '6'

# Like change Iyers if you want to change the turns. Wow. Impressive.
Iyers = 12

while Iyers > 0:

    # Counts the times you take an L
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # Comparing Rhajapashka to the inferior one
        if char in Rhajapashkas:
            print(char)

        else:
            print("_")

            # for every failure 1 will be added to the Ls you take nerd

            failed += 1

    if failed == 0:
        # You will win the game if Ls are zero
        print("Wicket!")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then You gotta do it again Frickoid
    guess = input("guess a character:")

    # every input character will be stored in guesses
    Rhajapashkas += guess

    # check input with the character in word
    if guess not in word:

        Iyers -= 1

    # You get wrong
     # You get wide
        print("Idiot no. Wide.")

        # PRInts how much time you have left.
        print("You have", + Iyers, 'more Rhajapakshas')

        if Iyers == 0:
            print("Goddamn It Sean Do something better with your life. Go watch the IPL!")