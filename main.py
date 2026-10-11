from student_utils import student, marks, attendance, result

students = [
    {
        "id": 101,
        "name": "Anu",
        "age": 21,
        "marks": [85, 90, 78],
        "attendance": 92.5
    },
    {
        "id": 102,
        "name": "Naisam",
        "age": 21,
        "marks": [85, 90, 78],
        "attendance": 92.5
    },
    {
        "id": 103,
        "name": "Yoosuf",
        "age": 22,
        "marks": [65, 72, 80],
        "attendance": 80.0
    },
    {
        "id": 104,
        "name": "Dayan",
        "age": 21,
        "marks": [35, 60, 75],
        "attendance": 85.0
    },
    {
        "id": 105,
        "name": "Nuziha",
        "age": 22,
        "marks": [95, 92, 98],
        "attendance": 68.0
    },
    {
        "id": 106,
        "name": "Neharsha",
        "age": 23,
        "marks": [45, 55, 60],
        "attendance": 75.0
    },
    {
        "id": 107,
        "name": "Amina",
        "age": 21,
        "marks": [88, 76, 91],
        "attendance": 95.0
    },
    {
         "id":108,
         "name":"Nadiya",
         "age":23,
         "marks":[90,89,87],
         "attendance":76.0
    },
    {
        "id": 109,
        "name": "Rahul",
        "age": 22,
        "marks": [65, 72, 80],
        "attendance": 80.0
    },
    {
        "id": 110,
        "name": "Meera",
        "age": 21,
        "marks": [35, 60, 75],
        "attendance": 85.0
    },
    {
        "id": 111,
        "name": "Arjun",
        "age": 23,
        "marks": [95, 92, 98],
        "attendance": 68.0
    },
    {
        "id": 112,
        "name": "Diya",
        "age": 22,
        "marks": [45, 55, 60],
        "attendance": 75.0
    },
    {
         "id": 113,
         "name": "Gayathri",
         "age":22,
         "marks":[90,67,87],
         "attendance":75.6
    },
    {
    "id": 114,
    "name": "Yunus",
    "age": 22,
    "marks": [78, 85, 92],
    "attendance": 88.0
}
]

def display_menu():
    print("\n     ~~~~~~~   STUDENT MANAGEMENT SYSTEM    ~~~~~~~     \n")
    print(" 1  Add Student ")
    print(" 2  Display Student ")
    print(" 3  Calculate Marks ")
    print(" 4  Check Attendance ")
    print(" 5  Generate Results ")
    print(" 6  Search Student ")
    print(" 7  Exit ")

while True:
    display_menu()
    choice = int(input("Enter your Choice : "))

    if choice == 1:
        student.add_student(students)

    elif choice == 2:
        student.display_students(students)

    elif choice == 3:
         student_id = int(input("Enter Student ID: "))
         found = False
         for s in students:
              if s["id"] == student_id:
                   student_marks = s["marks"]
                   print("Total:", marks.calculate_total(student_marks))
                   print("Average:", round(marks.calculate_average(student_marks), 2))
                   print("Highest:", marks.highest_mark(student_marks))
                   print("Lowest:", marks.lowest_mark(student_marks))
                   print("Pass Status:", marks.check_pass(student_marks))
                   found = True
                   break
              if not found:
                   print("Student not found!")


    elif choice == 4:
         student_id = int(input("Enter Student ID: "))
         found = False
         
         for s in students:
            if s["id"] == student_id:
                 attendance.display_attendance_status(s["attendance"])
                 found = True
                 break
         if not found:
              print("Student not found!")


    elif choice == 5:
         student_id = int(input("Enter Student ID: "))
         found = False
         for s in students:
            if s["id"] == student_id:
                 result.result_summary(s["name"], s["marks"])
                 found = True
                 break
         if not found:
              print("Student not found!")
   

    elif choice == 6:
            student.search_student(students)
    elif choice == 7:
           print("Thankyou for using Student Management System!")
           break
    else:
          print("Invalid Choice! Please Try Again.")      
          break                                      
    
 
   






