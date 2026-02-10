"""
Task:
Write a simple Python program to evaluate a student's result using conditional statements.

Requirements:
Ask the user to enter:

Student name
Marks in Maths, Science, and English
Validate the marks:
    If any mark is less than 0 or greater than 100, print Invalid marks entered and stop the program.

Calculate:

Total marks
Average percentage
Determine Pass / Fail:

If any subject mark is below 40, the student fails
Otherwise, the student passes
If the student passes, assign a grade:

A → Average ≥ 75
B → Average ≥ 60 and < 75
C → Average ≥ 40 and < 60
Display:

Student name
Total marks
Average percentage (2 decimal places)
Pass/Fail status
Grade (only if passed)

Expected Interaction:
Enter student name: Rahul

Enter Maths marks: 78

Enter Science marks: 65

Enter English marks: 82

Student Name: Rahul

Total Marks: 225

Percentage: 75.00

Status: PASS

Grade: A
"""
# Taking input from the user:
student_name=input("Enter student name: ")

math_marks=float(input("Enter Maths marks: "))
# Validating the Marks:
if math_marks >100 or math_marks<0:
    print("Invalid marks entered")
    exit()
science_marks=float(input("Enter Science marks: "))
# Validating the Marks:
if science_marks >100 or science_marks<0:
    print("Invalid marks entered")
    exit()
english_marks=float(input("Enter English marks: "))
# Validating the Marks:
if english_marks >100 or english_marks<0:
    print("Invalid marks entered")
    exit()

# calculating marks:
#Total Marks:
total_marks_obtained = math_marks+science_marks+english_marks
# Average:
average_percentage = (total_marks_obtained/300)*100
#print(f"{total_marks_obtained}, {average_percentage}")
#Determinig Pass/Fail:
if(math_marks <40 or science_marks <40  or english_marks <40 ):
    Passed=False
else:
    # Assigning Grade:
    if average_percentage>=75:
        grade='A'
        Passed=True
    elif average_percentage>=60:
        grade='B'
        Passed=True
    else:
        grade='C'
        Passed=True

print(f"Student name: {student_name}")
print(f"Total marks: {total_marks_obtained}")
print(f"Average percentage: {average_percentage:.2f}")
if Passed==True:
    print("Status: PASS")
    #Grade (only if passed)
    print(f"Grade: {grade}")
else:
    print(f"Status: FAIL")