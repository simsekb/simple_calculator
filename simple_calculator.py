# Kishan's Calculator

# Imports
import sys  

# Calculator
print("Welcome! This is Kishan's calculator.")
print('What would you like to calculate?')

previousOutcome = None
while(True):
    if previousOutcome:
        print('What else:')

    try:
        userInput = input()
        if(userInput == 'q'):
            print('Have a great day!')
            sys.exit()

        if previousOutcome:
            result = eval(previousOutcome + userInput)
        else:
            result = eval(userInput)

        print('Outcome', result);
        previousOutcome = str(result)
    except NameError:
        print('Bad input')