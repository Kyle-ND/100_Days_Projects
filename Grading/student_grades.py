student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

students = student_scores.keys()
student_grades = {}

for student in students:
    if 91 <= student_scores[student] <= 100:
        student_grades[student] = "Outstanding"

    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"

    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
        
    else:
        student_grades[student] = "Fail"

print(student_scores)
print(student_grades)