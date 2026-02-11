"""Question 1: Student Grade Calculator
Problem Statement:

Create a grade calculation system that uses *args and **kwargs to handle different scoring scenarios.

Requirements:

Create a function calculate_grade() with:

Parameters:
*scores - Variable number of test scores
**adjustments - Optional keyword arguments for bonus points (e.g., attendance=5, project=10)
Returns: Final grade percentage (float)
Logic: Average of scores + sum of all bonus adjustments
Task: Calculate grades for:

Student with scores: 85, 90, 78 (no bonus)
Student with scores: 70, 65, 80 (with attendance=5, project=10 bonus)
Example Output:

Final Grade: 84.33%
Final Grade: 86.67%"""

def calculate_grade(*scores,**adjustments):
    if not scores:
        return 0.0
    
    average_score= sum(scores)/len(scores)

    total_bonus=sum(adjustments.values())

    final_grade=average_score+total_bonus
    return round(final_grade,2)


#Case-1: Student with scores: 85, 90, 78 (no bonus)
grade1=calculate_grade(85,90,78)
print(f"Final Grade: {grade1}%")

#Case-2: Student with scores: 70, 65, 80 (with attendance=5, project=10 bonus)
grade2=calculate_grade(70,65,80, attendance=5,project=10)
print(f"Final Grade: {grade2}%")