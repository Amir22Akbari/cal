
TOTAL_GRADES = 3

    

def grades_input():
    grade = int(input("Enter Grade: "))
    #grade_two = int(input("Enter Grade 2:"))
    #grade_three = int(input("Enter Grade 3:"))
    while grade < 0.0:
            grade = int(input("grade can not be negative, Enter again: "))
    return grade
    #while grade_two < 0.0:
    #        print("grade 2 can not be negative")
    #return grade_two
             
    
def average(grade_one, grade_two, grade_three):
    average_value = (grade_one + grade_two + grade_three) / 3
    average2 = (grade_two + grade_three) / 2
    average_value = (int)(average_value +0.5)
    average2 = (int)(average2+0.5)
    return average_value, average2
def get_letter_grade(average_value, average2, grade_three):
    if average_value >= 90.0:
        letter_grade = "A"
        
    elif average_value >= 70.0 and average_value <= 90.0:
      if grade_three >= 90.0:
          letter_grade = "A"
      else:
          letter_grade = "B"
    elif average_value >= 50.0 and average <= 70.0:
      if average2 >= 70.0:
          letter_grade = "C"
      else:
          letter_grade = "D"
    else:
          letter_grade = "F"
    return letter_grade


def display(average, letter_grade):
    print("average:", average)
    print("Letter grade=", letter_grade)
    
def main():

    grade_one = grades_input()
    grade_two = grades_input()
    grade_three = grades_input()
    average_value, average2 = average(grade_one, grade_two, grade_three)
    letter_grade = get_letter_grade(average_value, average2, grade_three)
    display(average_value, letter_grade)

#call main
main()
     
                    
       
