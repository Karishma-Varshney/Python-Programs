# program based on dictionaries

student_scores = {
    "harry": 81,
    "ron": 78,
    "hermione": 99,
    "draco": 74,
    "neville": 62,
}

student_grades = {}

for key in student_scores:
    if (student_scores[key]>90):
        student_grades[key] = "outstanding"
    elif (student_scores[key]>80):
        student_grades[key] = "exceeds expectations"   
    elif (student_scores[key]>70):
        student_grades[key] = "acceptable"  
    else:
        student_grades[key] = "fail"

print(student_grades)



