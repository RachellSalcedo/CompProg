import time

name = input("what is your name? ")

print("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#here we set the secret. select any word to play with
word = ("secret")

#creates an variable with an empty value
guesses = ''

#determine the number of turns 
turns = 10 

#check if the turns are more than zero 
while turns > 0:

# for every character in secret_word
    for char in word: 

# see if the character is in the players guess
if char in guess:

# print them out the character
print(char,end=""),

else:

# if not found, print a dash
print("_",end=""),

#and increase the failed counter with one 
failed += 1

#if failed is equal to zero

#print you won
if failed == 0:
    print("you won")
break
# ask the user go guess a character
guess = input("guess a character:")

# set the players guess to guesses 
guesses += guess

# if the guess is not found in the secret word
if guess not in word:

# turns counter decreases with 1 (now 9)
turns -= 1

print("wrong")

print("You have", + turns, 'more guesses' )

if turns == 0:
    print( "you lose" )