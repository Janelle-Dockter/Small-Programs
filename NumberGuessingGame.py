# jdockter17@georgefox.edu
# Final Exam
# 2017-12-11

from random import randint

def main():
    """
    Play a round and keep track of the lowest number of guesses
    Ask user if they want to play again
    When they choose to quit, display the lowest number of guesses in a round
    """
    displayOpening()
    bestRound = 100
    done = False
    while not done:
        
        answer = getAnswer()
        thisRound = playRound(answer)
        if thisRound < bestRound:
            bestRound = thisRound     
        done = getMenuChoice()
    displayBestRound(bestRound)
    
    
def displayOpening():
    """
    Prints the opening according to the assignment's specifications
    """
    print("Welcome to the Guessing Game!")
    print("")
        
        
def getAnswer():
    """
    Have the computer pick a random integer between one and one hundred
    Display that answer before the round is played
    """
    answer = randint(1, 100)
    print("(answer is ", answer, ")", sep = "")
    return answer


def playRound(answer):
    """
    Each time the user guesses a valid number, add a tally to their guess count
    If they guess too low, change the smallest number they can guess
    If they guess too high, change the biggest number they can guess
    If they were correct, display how many tries it took them
    """
    low = 1
    high = 100
    numberOfGuesses = 0
    found = False
    while not found:
        guess = getGuesses(low, high)
        if guess < answer:
            print("Too low!")
            low = guess + 1
            numberOfGuesses += 1
            found = False
        elif guess > answer:
            print("Too high!")
            high = guess - 1
            numberOfGuesses += 1
            found = False
        else:
            print("You guessed it!")
            numberOfGuesses += 1
            found = True
    displayRoundResult(numberOfGuesses)
    return numberOfGuesses
            
            
def getGuesses(low, high):
    """
    Ask user for the a number between the current high and low value
    If their guess is outside the range, throw an error and re-ask
    If the guess is not an integer, tell them it's invalid and re-ask
    """
    done = False
    while not done:
        try:
            print("Guess a number between ", low, " and ", high, ": ", 
                  sep = "", end = "")
            guess = int(input(""))
            if guess < low or guess > high:
                print("Your guess must be between ", low, " and ", high,
                      ".", sep = "")
                done = False
            else:
                done = True                
        except ValueError:
            print("Your guess must be a number between ", low, " and ", 
                  high, ".", sep = "")
            done = False    
    return guess


def displayRoundResult(numberOfGuesses):
    """
    Print the result of the round (how many guesses it took)
    If user guessed right the first time, print guess singular
    If it took user more than one guess, print guesses plural
    """
    if numberOfGuesses == 1:
        print("It only took you 1 guess.")
    else:
        print("It only took you", numberOfGuesses, "guesses.")
        
        
def getMenuChoice():
    """
    Ask user if they would like to play again, validating their input
    If they choose to play again, set done as false
    If they choose to quit, set done to true
    """
    answered = False
    while not answered:
        menuChoice = input("Play again? (Y/N): ")
        if menuChoice == "Y" or menuChoice == "y":
            answered = True
            done = False
        elif menuChoice == "N" or menuChoice == "n":
            answered = True
            done = True
        else:
            print("Enter a valid menu choice.")
            answered = False
    print("")
    return done


def displayBestRound(bestRound):
    """
    If the user's bestRound was one guess, print guess singular
    If the user took more than one guess, print guesses plural
    """
    if bestRound == 1:
        print("Thanks for playing, your best round was 1 guess.")
    else:
        print("Thanks for playing, your best round was", bestRound, "guesses.")
            
    
main()