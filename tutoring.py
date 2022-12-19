#Program: Math Tutoring Game
#Author:  Amir Akbari
#Date: 3/24/2022
"""
Problem: We want to create a math tutoring game where a student can choose between addition, subtraction, and multiplication and do math problems accrodingly so.
Input: Menu selection, user answer
Processing: Use random number to generate 2 numbers between 10 and 50, Generate math problem from 2 random numbers and user selected operation, 
Prompt for user answer and check user answer for correctness, Repeat the process until user select, exit the program.
Output: Display message about user's answer
Variables: menu_selection, number1, number2, user_answer, correct_answer
Constants: NONE
Python Module: import random

Detailed Pseudocode:
1. Start a looping structure  
2. Display menu (See above menu display) 
3. Prompt user to enter menu selection: (1-4) 
4. Validate menu selection 
5. Display proper message for invalid selection or Exit the Game selection 
6. Generate random numbers between 10-50 inclusive 
7. Display problem (See above problem display) 
8. Prompt user to enter answer 
9. Check user answer to see if it is correct and display proper message 
10. Repeat the same process until user selects (4) exit the program 
"""
import random
# Display menu
print('Math Tutoring Game\n')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Exit the Game\n')
# Input
def generate_two_digit_number():
  number = randint.random(10,50)
  return number
operation = input("Type '1' for add, '2' for subt, '3' for multi, '4' to exit game:")
while operation != '4':
  if operation == '1':
      num1 = generate_two_digit_number()
      num2 = generate_two_digit_numbert()
      solution = num1 + num2
      answer = int(input(f"{num1}\n+              {num2}\n---\nEnter your answer: "))
      if answer == solution:
          print(f"Correct! answer:                    {solution}")
      else:
          print(f"Incorrect! answer:                {solution}")




