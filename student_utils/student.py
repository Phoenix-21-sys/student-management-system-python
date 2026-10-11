def add_student(students):
     student_id = int(input("Enter the student ID : "))
     name = str(input("Enter the student Name : "))
     age = int(input("Enter the student Age : "))
     marks = list(map(int,input("Enter marks for 3 subject: ").split(",")))
     attendance = float(input("Enter attendance percentage : "))
     student = {
          "id" : student_id,
          "name" : name,
          "age" : age,   
          "marks" :  marks,
          "attendance" : attendance
     }
     students.append(student)
     print("student added successfully!")    

def display_students(students):
     if not  students:
          print("No Student Found") 
     else:
          for student in students:
               print("ID : ", student["id"])
               print("Name : ", student["name"])
               print("Age : ", student["age"])
               print("Marks : ", student["marks"])
               print("Attendance : ", student["attendance"],"%") 
def search_student(students):
     searchid = int(input("Enter the student ID : "))
     for student in students:
          if student["id"] == searchid:
               print("student found!")
               print("ID : ", student["id"])
               print("Name : ", student["name"])
               print("Age : ", student["age"]) 
               print("marks : ", student["marks"])
               print("attendance : ", student["attendance"],"%") 
               break
          else:
               print("student not found!")

def check_exam_eligibility(students):
                    search_id = int(input("Enter Student ID : "))
                    for student in students:
                           if student["id"] == search_id:
                                  if student["attendance"] >= 75:
                                        if all (marks>= 40 for marks in student["marks"]):
                                         print("student eligible for exam")
                                        else:
                                              print("student not eligible for exam : Failed in subject") 

                                  else:
                                        print("student not eligible : Low attendance")  
                                  return 
                           print("student not found!")

                                  

                 