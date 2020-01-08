"""
Victor Wu 
Monday May 6th 2019
"""

AllDict = {} #Dictionary with all the words
#read and store each text file. Add code for all 4 files.
fp = open('animals.txt')
animals = fp.read().split(",")
AllDict['animals'] = animals

fp = open('colors.txt')
colors = fp.read().split(",")
AllDict['colors'] = colors

fp = open('shapes.txt')
shapes = fp.read().split(",")
AllDict['shapes'] = shapes

fp = open('fruits.txt')
fruits = fp.read().split(",")
AllDict['fruits'] = fruits 


HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
  |   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 /    |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |    
=========''']   #Template for the hangman

def getRandomWord(wordList):
   ''' This function returns a random word from the passed list of words'''
   import random
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]


switch = True  #Allows us to close the program later
#menu options
while switch: #keep playing game until player stops
    print ("""
    Welcome to Hangman. Here’s the list of word categories:

        1- Animals
        2- Colors
        3- Shapes
        4- Fruits
        5- Exit

    Select a category by entering its number or 5 to exit the game: 

            """)
    ans=input("Which word category do you want? ")
    while ans: #Choose category
        if ans == "1":
            secret = getRandomWord (AllDict["animals"])
        elif ans == "2":
            secret = getRandomWord (AllDict["colors"])
        elif ans == "3":
            secret = getRandomWord (AllDict["shapes"])
        elif ans == "4":
            secret = getRandomWord (AllDict["fruits"])
        elif ans == "5":    #Option to exit game
            print ("\nGoodbye! See you next time!")
            switch=False
        else:    #Forces player to enter one of the five options
            print("\nYou must enter one of the five options. Try again")
            break
         
        wordcount = "_"*len(secret)
        WordGuess = list (wordcount)   #Updates with every correct guess so that the player can keep track
        MissedLetters = []  #List of wrong guesses
        GuessList = []   #List of every guess
        numberwrong = 0   #Number of wrong guesses
        guesscount = 0     #Number of all guesses
        word_dict = {}       #Dictionary for secret word
        word= ""
        
    
        for ch in range (len(secret)): #create dictionary with letters as key and position as values
            if secret[ch] in word_dict:
                word_dict[secret[ch]].append(ch)
            else:
                word_dict[secret[ch]]=[ch]

        while switch:
            print ("Your random word has",len(secret),"letters:","_ "*len(secret)) #initialize word guess
            print (HANGMAN [numberwrong]) #print hangman postion
            guess = input ("Please select a lowercase letter from a-z or Exit to exit the game: " ) #ask user for input
            guesscount+=1
            secretlist = list(word_dict.keys()) #lists keys(letters) of word
            if guess == "Exit":     #allows player to exit game
               print("Goodbye! See you next time.")
               switch = False     #stops while loops
            elif guess in GuessList: #checks if letter guess already attempted
               print ("\nYou have already entered this letter. Please try again.")    #allow player to reenter a value
               print ("\nHere is a list of wrong letters:", MissedLetters)
               print (WordGuess)
            elif guess.isdigit():    #checks if player entered a digit
               print ("\nYou entered a number. You must enter a lowercase letter from a-z. Please try again.")    #allow player to reenter a value
               print ("\nHere is a list of wrong letters:", MissedLetters)
               print (WordGuess)
            elif guess.isupper():   #checks if player entered a capital letter
               print ("\nYou entered a capital letter. You must enter a lowercase letter from a-z. Please try again.")   #allow player to reenter a value
               print ("\nHere is a list of wrong letters:", MissedLetters)
               print (WordGuess)
            elif guess=="":   #checks if player actually entered something
               print ("\nPlease enter a lowercase letter from a-z")     #allow player to reenter a value
               print ("\nHere is a list of wrong letters:", MissedLetters)
               print (WordGuess)
            elif len(guess)>1:
               print ("\nPlease enter a single lowercase letter from a-z")
               print ("\nHere is a list of wrong letters:", MissedLetters)
               print (WordGuess)
            else:
                if guess in secretlist: #checks if guess is in list of letters of secret word
                    a = word_dict.get(guess) #finds index value from dictionarry of letter guess
                    GuessList.append (guess)
                    for i in a:
                        WordGuess[i] = guess #replace _ with letter in guess
                    print ("\nHere is a list of wrong letters:", MissedLetters)
                    print (WordGuess)
                    word = ''.join(WordGuess)
                    if word == secret: #stops execution if secret word is guessed 
                        print ("\nCongratulations! You guessed", secret, "in", guesscount, "guesses. You made", numberwrong, "wrong guesses" )
                        Exit = input("Do you want to play again (yes/no)?:")   #allows player to exit or replay
                        if Exit == "yes":
                           break   #restart with a new word
                        elif Exit == "no":
                           print ("Goodbye! See you next time.")
                           switch=False   #stops while loops
                else:
                    numberwrong +=1
                    MissedLetters.append(guess) #creates list of wrong letters
                    GuessList.append (guess)
                    print ("\nYour guess is wrong. Here is a list of wrong letters:", MissedLetters) #reveal secret word to loser
                    print (WordGuess)
                    if numberwrong == 6:
                        print (HANGMAN[6],"\nYou lost. The secret word was",secret) #stops executions after 6 failed attemps. The game is over
                        Exit = input("Do you want to play again (yes/no)?:")    #allows player to exit or restart
                        if Exit == "yes":  
                           break  #restart with a new word
                        elif Exit == "no":
                           print ("Goodbye! See you next time.")
                           switch=False    #stops while loops
