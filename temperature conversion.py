# Program: Temperature conversion with functions
# Author: Amir Akbari
# Date: 3/29/2022

'''
    IPO Design:
    Problem: Use function to organize the temperature conversin task
    Functions:
        1. function display_menu() - no parameter, no return value, just
            display the menu of temperature conversion
        2. function get_menu_selection()- no parameter, return menu selection
            prompt the user to enter menu selection amd return the menu selection
        3. function process_menu()- menu selection,  no return value
            process each menu selection
        4. function get_fahrenheit()- celsius, return fahrenheit
            prompt the user to enter fahrenheit
        5. function get_celsius() - no parameter, return celsius
            prompt the user to enter celsius
        6. function calc_fahrenheit()- pass in celsius, return fahrenheit
            calculate the fahrenheit based on the celsius passed in
        7. function calc_celsius() - pass in fahrenheit, return celsius
       
'''
def main():
    menu_selection = 1
    while menu_selection != 3:
        # display menu function call
        display_menu()
        # get menu selection function call
        menu_selection = get_menu_selection()
        # process the menu function call
        process_menu(menu_selection)

def display_menu():
    """ display temperature conversion menu """
    print("Temperature Conversion Program\n")
    print("1. Convert to Celsius")
    print("2. Convert to Fahrenheit")
    print("3. Exit the program")
    
def get_menu_selection():
    """ get menu selection from the user """
    selection = int(input("Enter menu selection:"))
    return selection
def process_menu(menu_selection):
    """ process each menu selection and display the temperature accordingly """
    
    # if menu selection is 1, call get fahrenheit function
    if menu_selection == 1:
        fahrenheit = get_fahrenheit()
        celsius = calc_celsius(fahrenheit)
        print("Celsius:",celsius)
    # if menu selection is 2, call get celsius function
    elif menu_selection == 2:
        celsius = get_celsius()
        fahrenheit = calc_fahrenheit(celsius)
        print("Fahrenheit:", fahrenheit)
    # if menu selection is 3, exit the program
    elif menu_selection == 3:
        print("Exit the progam")
    # if menu selection is out of 1-3, then display invalid selection
    else:
        print("Invalid selection")
def get_fahrenheit():
    fah = float(input("Enter fahrenheit:"))
    return fah
def get_celsius():
    cel = float(input("Enter celsius:"))
    return cel
def calc_fahrenheit(cel):
    return cel * 1.8 + 32
def calc_celsius(fah):
    return (fah -32) / 1.8

#call main
main()





    
        





        
