#Author: Jason D'Souza
#Date: December 24, 2021
#File Name: convert_morse_code
#Description: Program converts text given by the user to Morse code

morsecode = { 'A':'.-', 'B':'-...', #'morsecode' is dictionary, a collection of values that translates certain values to another assigned value
              'C':'-.-.', 'D':'-..', 'E':'.', 
              'F':'..-.', 'G':'--.', 'H':'....', 
              'I':'..', 'J':'.---', 'K':'-.-', 
              'L':'.-..', 'M':'--', 'N':'-.', 
              'O':'---', 'P':'.--.', 'Q':'--.-', 
              'R':'.-.', 'S':'...', 'T':'-', 
              'U':'..-', 'V':'...-', 'W':'.--', 
              'X':'-..-', 'Y':'-.--', 'Z':'--..', 
              '1':'.----', '2':'..---', '3':'...--', 
              '4':'....-', '5':'.....', '6':'-....', 
              '7':'--...', '8':'---..', '9':'----.', 
              '0':'-----', ' ':' ' } 

def translator(): #Defines 'translator' function
    text = str(input('Enter text desired to be translated to morse code:')) #'text' variable is defined and the value is inputted from the user as a string
    for letter in text: #For loop continues for each character in the 'text' value
        if letter.isalpha() or letter.isdigit() or letter == ' ': #If statement continues if the 'letter' value is either an alphabet character, an integer, or a space
            letter = letter.upper() #Upper function converts 'letter' to uppercase for better efficiency
            print(morsecode[letter], end = ' ') #Calls the 'morsecode' dictionary when printing 'letter' to translate it before being printed for the user, then uses the end parameter to print a space at the end of 'letter' so that the next character being translated can be printed on the same line with a space between to reduce confusion
    print('') #Prints a blank line for organization
    
def keepgoing(): #Defines 'keepgoing' function
    stop = str(input('Type Q to quit or C to continue:')) #'stop' variable asks the user if they would like to end the program or continue, accepting the user input as a string value
    while True: #While loop keeps looping until either the user tells the program to quit or the user breaks the loop with the break function 
        stop = stop.upper() #Upper function converts the user input to uppercase for efficiency
        if stop == 'Q': #If the user types 'Q' for the 'stop' variable, the program quits
            quit()
        elif stop == 'C': #If the user types 'C' for the 'stop' variable, the while loop in the function breaks and the program continues
            break
        else: #If the user types neither 'Q' or 'C' for the 'stop' variable, the else statement prints that the user input was invalid and asks for the 'stop' variable again to determine to quit or continue the program 
            print('')
            print('Input invalid')
            stop = str(input('Type Q to quit or C to continue:'))
            
action = str('') #Defines the 'action' variable as a string
while action != 'S': #While loop keeps looping until the 'action' variable is 'S'
    action = str(input('Print S to start, H for help, or Q to quit:')) #'action' variable acts as a menu, accepting user input as a string for either starting the program, help menu, or to close the program
    action = action.upper() #Upper function converts all string from the 'action' variable to uppercase to ensure least errors and improve efficiency
    print('')#Prints a blank line for organization

    if action == 'H': #Help menu, starts if user types 'H' for the 'action' variable
        print('This is the morse code translator program') #Prints online instructions about the program functions/utilisation for the user
        print('This program will translate any given text to morse code')
        print('When prompted, print some text that you would like to be converted')
        print('')

    while action == 'S': #If the user types 'S' for the 'action' variable, the while loop will start and keep the morse code translation part of the program running until the user decides to quit when prompted
        translator() #Runs 'translator' function to translate user inputted text to morsecode
        print('')
        keepgoing() #Runs 'keepgoing' function to determine whether to continue or quit the program
        print('')

    if action == 'Q': #If statement continues if the user types 'Q' for the 'action' variable
        quit() #Quits the program
