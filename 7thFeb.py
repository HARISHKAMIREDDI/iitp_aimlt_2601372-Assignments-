"""Question: Student Grade Book
Real-World Context:
You're maintaining a simple grade book for 5 students with their marks in 3 subjects. Use Python data structures to store and analyze this data.

Your Task:
Write a Python program using Lists, Dictionaries, Tuples, and Sets to:

Store student names and marks
Calculate averages
Find top scorer
Display results
Requirements:
Use these data structures:

List - Store student names
Dictionary - Store marks for each student
Tuple - Store subject names
Set - Store unique grades
Program should:

Display all student names
Show first 3 students (using slicing)
Calculate and print each student's average
Find student with highest average
Show all unique grades
Sample Data to Use:
Students: Raj, Priya, Amit, Sneha, Karan

Marks:
Raj: Math=85, Science=78, English=90
Priya: Math=92, Science=88, English=85
Amit: Math=70, Science=75, English=68
Sneha: Math=95, Science=90, English=92
Karan: Math=80, Science=82, English=78
Grading Logic:

Average ≥ 85: Grade A
Average ≥ 70: Grade B
Average < 70: Grade C
Expected Output:
All Students: ['Raj', 'Priya', 'Amit', 'Sneha', 'Karan']
First 3 Students: ['Raj', 'Priya', 'Amit']

Raj - Average: 84.33 - Grade: B
Priya - Average: 88.33 - Grade: A
Amit - Average: 71.00 - Grade: B
Sneha - Average: 92.33 - Grade: A
Karan - Average: 80.00 - Grade: B

Top Student: Sneha
Unique Grades: {'A', 'B'}"""

subjects=("Math","Science","English")
students=['Raj', 'Priya', 'Amit', 'Sneha', 'Karan']
student_marks={
  "Raj":[85,78,90],
  "Priya":[92,88,85],
  "Amit":[70,75,68],
  "Sneha":[95,90,92],
  "Karan":[80,82,78]
}
print(f"All Students: {students}")
print(f"First Three Students: {students[:3]}\n")
unique_grades=set()
top_avg=0
top_stu=""
#calculating averages:
for name in students:
  marks=student_marks[name]
  avg=sum(marks)/len(marks)
 

  #grading:
  if avg>=85:
    grade="A"
  elif avg>=70:
    grade="B"
  else:
    grade="C"

  unique_grades.add(grade)
  print(f"{name} - Average: {avg:.2f} - Grade: {grade}")

  #check for the top scorer:
  if avg>top_avg:
    top_avg=avg
    top_stu=name

print(f"\nTop Student: {top_stu}")
print(f"Unique Grades: {unique_grades}")
