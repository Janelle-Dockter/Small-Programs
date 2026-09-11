# jdockter17@georgefox.edu
# Program 6
# 2017-10-11

# Print greeting
print("Welcome to my Change Program")

# Get input
# Ask user for amount due and amount tendered
price = float(input("Please enter the sales price (xx.xx): $"))
tendered = float(input("Please enter the amount tendered (xx.xx): $"))

# Do calculations
# Find total amount of change needed
change = tendered - price

# Show results
# Print separator between input and output
print("")
# Print original change amount
print("Your change is: $", format(change, ".2f"), sep = "")
print("You will receive:")
# Create a for loop for each denomination
for x in [100, 50, 20, 10, 5, 1, .25, .10, .05, .01] :
    # Find how many of each denomination will go into the change amount
    denomination = int(change / x)
    # Enter singular labels for all denominations except the penny
    if x != .01 :
        if x == 100 :
            label = " - Hundred Dollar Bill"
        elif x == 50 :
            label = " - Fifty Dollar Bill"
        elif x == 20 :
            label = " - Twenty Dollar Bill"
        elif x == 10 :
            label = " - Ten Dollar Bill"
        elif x == 5 :
            label = " - Five Dollar Bill"
        elif x == 1 :
            label = " - Dollar Bill"
        elif x == .25 :
            label = " - Quarter"
        elif x == .10 :
            label = " - Dime"
        else :
            label = " - Nickel"
        # Print the label if the amount is singular
        if denomination == 1 :
            print(denomination, label, sep = "")
        # Print the label with an s if amount is plural
        elif denomination >= 2 :
            print(denomination, label, "s", sep = "")
        # Do not print anything if change is not divisible by denomination
        else :
            pass
    # For pennies, repeat print statements with singular and plural forms
    else :
        if denomination == 1 :
            print(denomination, " - Penny", sep = "")
        elif denomination >= 2 :
            print(denomination, " - Pennies", sep = "")
    # Find new change amount by subtracting the most recent denomination
    change = change - (x * denomination)