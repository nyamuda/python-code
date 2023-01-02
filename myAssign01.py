import random

print('Welcome to the number guessing game!')
randomSeed=input('Enter random seed: ')

random.seed(randomSeed)

numberOfGuesses=1

num=random.randint(1, 100)


def guessNumber() :
  
    global numberOfGuesses
    global num
   
    yourGuess=int(input('\nPlease enter a guess: '))
    if(yourGuess==num) :
        print(f'Congratulations. You guessed it!\nIt took you {numberOfGuesses} guesses.')
        #resetting the random number and number of guessess
        num=random.randint(1, 100)
        numberOfGuesses=1
        guessAgain=input('\nWould you like to play again (yes/no)? ')
        guessNumber() if(guessAgain=='yes') else print('Thank you. Goodbye.')
    else :
        print('Lower') if(yourGuess>num) else print('Higher')
        numberOfGuesses+=1
        guessNumber()


guessNumber()