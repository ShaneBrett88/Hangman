from random import randint
import os

#Clear screen at end of the game
def clear_screen_end():
    os.system("clear")
    print("Welocme to Shane's Hangman Game")
    print("")
    print(hangman(guesses))
    print("")
    print(wordLetterListHidden)
    print("")

#Clear screen during play  
def clear_screen_play():
    os.system("clear")
    print("Welocme to Shane's Hangman Game")
    print("")
    print(f'Your word has {len(wordLetterList)} letters')
    print("")
    print(f'Previous guessed letters are: {guessedLetters}')
    print(f'Guesses left: {guesses}')
    print("")
    print(hangman(guesses))
    print("")
    print(wordLetterListHidden)
    print("")

#Display of the Hangman
def hangman(lives):
    stages = [" _______\n|      |\n|      O\n|     /|\ \n|      |\n|     / \ \n|__________",
    " _______\n |      |\n |      O\n |      |\n |      |\n |     / \ \n |__________",
    " _______\n |      |\n |      O\n |      |\n |      |\n |\n |__________",
    " _______\n |      |\n |      O\n |\n |\n |\n |__________",
    " _______\n |\n |\n |\n |\n |\n |__________",
    "\n |\n |\n |\n |\n |\n |__________",
    "\n\n\n\n\n __________",
    ""]
    return stages[lives]

#Import and Select an word
def import_word():
    words = [word for word in open('word_list.txt')]
    for word in words:
        wordList = word.split()
    wordResult = wordList[randint(0,len(wordList)-1)].upper()
    return wordResult

#Import a random word
wordResult = import_word()

#Setting up the variables and empty lists
guessedLetters = []
wordLetterList = []
wordLetterListHidden = []
wordLetterListCheck = []
guesses = 7
wrongCount = 0
result = False
guessedbefore = False
rightAnswer = False
guessedTrigger = False

#Spliting word into letters / Hiding the letters
for letter in wordResult:
    wordLetterList.append(letter)
for letter in wordResult:
    wordLetterListCheck.append(letter)
for letter in wordResult:
    wordLetterListHidden.append("*")

# The main game
while guesses > 0:
    
    #Ask for player's guess
    clear_screen_play()
    if guessedTrigger == True:
        print(f'You have already guessed {playerGuess}')
        guessedTrigger = False
    playerGuess = input("Please enter your next guess: ").upper()
    
    #Condition checking playerGuess (Blank or not Alpha)
    while playerGuess == "" or not playerGuess.isalpha():
        if playerGuess == "":
            clear_screen_play()
            print("Your guess was blank")
            playerGuess = input("Please enter your next guess: ").upper()
        else:
            clear_screen_play()
            print(f'{playerGuess} is not a valid guess')
            playerGuess = input("Please enter your next guess: ").upper()
    
    #Condition checking playerGuess (Must be single letter or word guess)
    while len(playerGuess) != 1 and len(playerGuess) != len(wordLetterList):
        print("You must either guess a single letter or guess the whole word")
        playerGuess = input("Please enter your next guess: ").upper()

    #Check previous guessed letter
    if len(guessedLetters) > 0:
        for letter in guessedLetters:
            if playerGuess == letter:
                guessedbefore = True
                guessedTrigger = True
    
    #Adding playerGuess to guessedLetters            
    if guessedbefore == False:
        guessedLetters.append(playerGuess)
    
    #Looping through word to look for playerGuess
    for letter in wordLetterList:
        if playerGuess == wordResult:
            result = True
            wordLetterListHidden = wordLetterListCheck
        elif playerGuess == letter:
            numIndex = wordLetterList.index(letter)
            wordLetterList[numIndex] = "_"
            wordLetterListHidden[numIndex] = playerGuess
            rightAnswer = True
        else:
            wrongCount += 1
    
    #Checking if no more empty spaces        
    if wordLetterListHidden == wordLetterListCheck:
        result = True
    
    #Checking outcomes
    if result == True:
        clear_screen_end()
        print("Congratulations you Win!")
        print(f'Your word was {wordResult}')
        break      
    
    elif guessedbefore == True:
        guessedbefore = False
        wrongCount = 0
        continue
    
    elif wrongCount >= len(wordLetterListCheck):
        guesses -= 1
        wrongCount = 0
        
    elif rightAnswer == True:
        wrongCount = 0
        rightAnswer = False
    
    #Are they out of guesses?    
    if guesses == 0:
        clear_screen_end()
        print("You Lose!")
        print(f'Your word was {wordResult}')
        break
