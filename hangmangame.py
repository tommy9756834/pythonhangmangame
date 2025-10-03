'''
To play the handman game just run the code and input the word you want the computer to guess and it will try to guess it in 10 attempt
'''

import random
import re
import string
random.seed()

def blender(word):
    '''
    This function takss a list of word and turn every letter into a set
    parameter is a string with one or more word
    return a set with all the letter appeared in the string
    '''
    tempList = []   #list to store all the letter
    wordlist = word.split(" ") # split the list into seprate word
    for i in wordlist: # loop word in the list
        for j in i: # loop letter of the word
            tempList.append(j.lower()) #put it into temp list
    wordset = set(tempList) #turn temp list into a set
    return wordset

def guessing(word, correct, previous):
    '''
    This function is for the computer to randomly guessing without repeating the guesses
    parameter: the word the computer is guessing, the list of letter that is guessed before and is correct,
    the list of all letter from previous attempt 
    return previous attempt and the correct guesses
    '''
    allLetter = list(string.ascii_lowercase)    #make a list of all the lowercase letter
    for i in previous:
        allLetter.remove(i) #loop to remove the letter already guessed from list of all letter 
    attempt = random.choice(allLetter) #chose the random letter
    previous.append(attempt) #add the letter chosen to the list of previous attempt
    print("The computer is going to guess:", attempt)
    if attempt in word: #check if the attemp is correct
        print("Looks like ["+ attempt +"] is in the word!")
        correct.append(attempt) #add the correct letter to correctguess list
        return correct, previous
    else:
        print("Looks like it is a wrong guess")
        return correct, previous

def guessDisplay(correct, realWord):
    '''
    This function replace the letter that is not correctly guessed yet with
    parameter: a list of corrected letter, the word for guessing
    return the string replaced
    '''
    correctstring = "".join(correct) #Sperate the correct list into 1 string
    display = re.sub(rf"[^{correctstring}]","_",realWord) #replace all the not correct letter with _ and put it in display variable
    return display
    

if __name__ == "__main__":
    print("Welcome to the hangman game where the computer will try to guess your word in 10 attempt")
    while True: #Check user input loop
        answer = input("Please input the word for the computer to guess (it can 1 or more word sperated by space): ") 
        if re.findall("[^a-zA-Z ]+",answer): #Check if the input is a-z and space only without any other character
            print("Error: Please only input letter character")
        elif answer == "": #for edge case of space only 
            print("Error: Please only input letter character")
        else:
            answer = answer.lower() #make all the letter lowercase
            break
    
    wordset = blender(answer) #get all the letter appeared in the word (set does not repeat element)
    correctGuess = [" "] #list for storing correct guess, starting with a space for the display function to not replace the space with _
    previousAttempt= [] #list for storing previous attempt

    for i in range(10,0,-1): #loop for actual attempt
        correctGuess, previousAttempt = guessing(wordset,correctGuess, previousAttempt) #computer make a guess
        currentRight = guessDisplay(correctGuess, answer) #replace letter with _ if not guessed correctly
        

        if currentRight == answer: #check if all the letter are correctly guessed
            print("The computer had successfully guessed the word:",currentRight)
            print("Game ended")
            break
        print("Current word guessed:", previousAttempt) #print all the stat
        print("Current right guess:", currentRight)
        print("Number of attempt left:",i)
        input("Press enter to continue") #Allow the player to pause
        
        
        if i == 1: #it is for last attempt after pressing enter
            correctGuess, previousAttempt = guessing(wordset,correctGuess, previousAttempt) #make a guess again
            if currentRight == answer: #check if all the letter are guessed
                print("The computer had successfully guessed the word:",currentRight)
                print("Game ended")
            else: #the end of the game if the competer did not guess all the letter and game ended
                print("The computer did not guess the word:",answer)
                print("Game ended")