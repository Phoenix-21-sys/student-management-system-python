def calculate_grade(average):
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade

def pass_or_fail(marks):
    if all (mark >= 40 for mark in marks ):
        return "Pass"
    else:
        return "Fail"

def result_summary(name,marks):
    total = sum(marks)
    average = total/len(marks)
    grade = calculate_grade(average)
    final_result = pass_or_fail(marks)


    print(" ~~~ RESULT SUMMARY ~~~ ")
    print("Student Name : ",name)
    print("Marks : ",marks)
    print("Total Marks : ",total)
    print("Average Marks : ",round(average,2))
    print("Grade : ",grade)
    print("Result : ",final_result)    
    