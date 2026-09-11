# jdockter17@georgefox.edu
# Program 10
# 2017-11-15

from random import randint

ROCK = 1
PAPER = 2
SCISSORS = 3


def main():
    """
    Play rock, paper, scissors if user chooses to in the menu
    Take user and computer choice from functions and determine the winner
    Add the game result to the running tally of wins, losses, and ties
    If the user chooses to not play again, display the running record of games
    """
    wins = 0
    losses = 0
    ties = 0
    
    done = False
    
    while not done:
        menuChoice = getMenuChoice()
        if menuChoice == 1:
            computerChoice = getComputerChoice()
            userChoice = getUserChoice()
            gameResult = determineWinner(computerChoice, userChoice)
            if gameResult == "win":
                wins += 1
            elif gameResult == "lose":
                losses += 1
            else:
                ties += 1
            done = False
        else:
            showFinalRecord(wins, losses, ties)
            done = True
        
    
def getMenuChoice():
    """
    Give the user the option to play the game (1) or quit (2)
    If user enters a non-integer or number that isn't 1 or 2, ask to try again
    Return the integer value of their input
    """
    done = False
    
    while not done:
        menuChoiceString = input("Enter 1 to play game or 2 to quit: ")
        if menuChoiceString == "1" or menuChoiceString == "2":
            menuChoice = int(menuChoiceString)
            done = True
        else:
            print("Error! Please enter a valid option!")
            done = False
    
    print("")
    return menuChoice
    
    
def getComputerChoice():
    """
    Return computer's random choice between 1 and 3 (Rock, paper, or scissors)
    """
    return randint(1,3)

    
def getUserChoice():
    """
    Ask user for rock paper or scissors, convert choice to global variable
    If they do not enter rock, paper, or scissors, ask user to try again
    Return the integer value of the user's choice
    """
    done = False
    
    while not done:
        userChoiceString = input("Rock, Paper, or Scissors? ")
        if userChoiceString == "Rock" or userChoiceString == "rock":
            userChoice = ROCK
            done = True
        elif userChoiceString == "Paper" or userChoiceString == "paper":
            userChoice = PAPER
            done = True
        elif userChoiceString == "Scissors" or userChoiceString == "scissors":
            userChoice = SCISSORS
            done = True
        else:
            print("Error! Please enter a valid option!")
            done = False
    
    print("")
    return userChoice    

    
def determineWinner(computerChoice, userChoice):
    """
    Compare user's and computer's choice and find who won the match
    Print the result of the match
    Save the result as gameResult and return that value
    """
    
    # If computer choice is rock, calculate and display possible results
    if computerChoice == ROCK:
        print("The computer chose rock!")
        if userChoice == PAPER:
            print("Paper wraps rock! You win :)")
            gameResult = "win"
        elif userChoice == SCISSORS:
            print("Rock smashes scissors! You lose :(")
            gameResult = "lose"
        else:
            print("You both chose rock! It's a tie!")
            gameResult = "tie"
    
    # If computer choice is paper, calculate and display possible results
    elif computerChoice == PAPER:
        print("The computer chose paper!")
        if userChoice == SCISSORS:
            print("Scissors cuts paper! You win :)")
            gameResult = "win"
        elif userChoice == ROCK:
            print("Paper wraps rock! You lose :(")
            gameResult = "lose"
        else:
            print("You both chose paper! It's a tie!")
            gameResult = "tie"
    
    # If computer choice is scissors, calculate and display possible results
    else:
        print("The computer chose scissors!")
        if userChoice == ROCK:
            print("Rock smashes scissors! You win :)")
            gameResult = "win"
        elif userChoice == PAPER:
            print("Scissors cuts paper! You lose :(")
            gameResult = "lose"
        else:
            print("You both chose scissors! It's a tie!")
            gameResult = "tie"
    
    print("")
    return gameResult

    

def showFinalRecord(wins, losses, ties):
    """
    If user chooses to quit,  us the running score kept in main 
    Display final results of all matches
    """
    print("Human: ", wins, ", ", "Computer: ", losses, ", ",
          "Tie(s): ", ties, sep = "")
    
    
main()