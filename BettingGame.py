# jdockter17@georgefox.edu
# Program 11
# 2017-12-06

# Assign global variables for the 3 menu options
FIELD_BET = 1
PASS_BET = 2
QUIT = 3

# Import a random integer
from random import randint


def main():
    """
    Retrieve the number of talents user has to play with
    If they choose to quit, write the number of talents left to the file
    Play feild bet or pass bet depending on their choice
    After they have played, check if they have used all of their talents or not
    """
    numberOfTalents = readTalentAmount()
    displayOpening(numberOfTalents)
    
    done = False
    
    while not done:
        menuChoice = getMenuChoice()
        if menuChoice == QUIT:
            writeNewTalentAmount(numberOfTalents)
            done = True
        else:
            wagerAmount = getWagerAmount(numberOfTalents)
            if menuChoice == FIELD_BET:
                changeInTalents = playFieldBet(wagerAmount)
            else:
                changeInTalents = playPassBet(wagerAmount)
            numberOfTalents += changeInTalents
            done = checkIfDone(numberOfTalents)
            
            
def readTalentAmount():
    """
    Read from the talents text file to find how many talents the user has
    Convert this value to an integer
    It should always be an easy conversion if set up properly
    """
    try:
        talentsFile = open('talents.txt','r') 
        numberOfTalents = int(talentsFile.read())
        talentsFile.close()
        if numberOfTalents <= 0:
            numberOfTalents = 100
    except ValueError:
        numberOfTalents = 100
    except FileNotFoundError:
        numberOfTalents = 100
    except IOError:
        numberOfTalents = 100
    
    return numberOfTalents       


def displayOpening(numberOfTalents):
    """
    Print the two lines from the program instructions
    Print a space after for readability
    """
    print("Welcome to the Lots Game")
    print("Talents you have to play with:", numberOfTalents)
    print("")


def getMenuChoice():
    """
    Get the menu choice from the user, making sure it is one of the 3 options
    If it is not one of the three menu choices, re-ask the user
    Return their final choice to main
    """
    displayMenuOptions()
    
    done = False
    
    while not done:
        try:
            strMenuChoice = input("Choice --------------------------- ")
            menuChoice = int(strMenuChoice)
            if menuChoice == QUIT:
                done = True
            elif menuChoice == FIELD_BET:
                done = True
            elif menuChoice == PASS_BET:
                done = True
            else:
                print("ERROR! Enter a valid option.")
                done = False
        except ValueError:
            print("ERROR! Enter a valid option.")
            done = False
        
    return menuChoice
            
    
def displayMenuOptions():
    """
    Display the three menu options as outlined in program instructions
    """
    print("1 - Field Bet")
    print("2 - Pass Bet")
    print("3 - Quit")
    
    
def writeNewTalentAmount(numberOfTalents):
    """
    If the user chooses to quit, write current number of talents the user has
    """
    talentsFile = open('talents.txt','w') 
    talentsFile.write(str(numberOfTalents))
    talentsFile.close()
    
    
def getWagerAmount(numberOfTalents):
    """
    Ask user for the amount of talents to wager
    Print error if choice is more than they have, negative, or not an integer
    Once they've entered something valid, return that amount
    """
    done = False
    
    while not done:
        try:
            wagerAmount = int(input("How much do you wish to wager? --- "))
            done = True
            if wagerAmount > numberOfTalents:
                print("ERROR! That is more than you have!")
                done = False
            elif wagerAmount <= 0:
                print("ERROR! Enter a positive amount.")
                done = False
            else:
                done = True
        except ValueError:
            print("ERROR! Enter a valid amount.")
            done = False
        
    return wagerAmount
            
            
def playFieldBet(wagerAmount):
    """
    Cast lots and find the result of round
    Assign the change in talents variable to a manipulated wager amount
    Return the change in talents
    """
    lotsCast = getLotsCast()
    
    if lotsCast <= 8 and lotsCast >= 5:
        print("You lost your bet.")
        changeInTalents = -wagerAmount
    elif lotsCast == 2 or lotsCast == 12:
        print("You won double your bet.")
        changeInTalents = wagerAmount * 2
    else:
        print("You won your bet.")
        changeInTalents = wagerAmount
    
    return changeInTalents


def getLotsCast():
    """
    Find the result of the cast by adding two random ints between 1 and 6
    Print the cast for user to see
    Return that cast amount for use in the games
    """
    firstCast = randint(1, 6)
    secondCast = randint(1, 6)
    lotsCast = firstCast + secondCast
    
    print("The LOTS CAST is -----------------", lotsCast)
    
    return lotsCast


def playPassBet(wagerAmount):
    """
    Find the lots cast, determine win or loss if the roll was a 7, 11, 2, or 12
    If the roll was something else, turn that roll into a point
    Call the fuction that plays a point
    Return the result of the entire pass bet, which is change in talents
    """
    lotsCast = getLotsCast()
    
    if lotsCast == 7 or lotsCast == 11:
        print("You won your bet.")
        changeInTalents = wagerAmount
    elif lotsCast == 2 or lotsCast == 12:
        print("You lost your bet.")
        changeInTalents = -wagerAmount
    else:
        changeInTalents = playPointRound(lotsCast, wagerAmount)
    
    return changeInTalents
        
        
def playPointRound(point, wagerAmount):
    """
    Continue casting lots until the cast is either 7, 11, or point
    Return the result of one of those three to playPassBet
    """
    done = False
    
    while not done:
        
        lotsCast = getLotsCast()
        
        if lotsCast == point:
            print("You won your bet.")
            changeInTalents = wagerAmount
            done = True
        elif lotsCast == 7 or lotsCast == 11:
            print("You lost your bet.")
            changeInTalents = -wagerAmount
            done = True
        else:
            done = False
    
    return changeInTalents


def checkIfDone(numberOfTalents):
    """
    Display new number of talents once bets are over
    If that number is 0, quit the game and write 100 to text file,
    If not, the user can continue playing in main
    """
    print("You now have ---------------------", numberOfTalents)
    print("")
    
    if numberOfTalents == 0:
        writeNewTalentAmount("100")
        return True
    else:
        return False
    
    
main()