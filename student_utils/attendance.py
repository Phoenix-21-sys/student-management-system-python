def calculate_attendance(attended, total_classes):

    if total_classes <= 0:
        return None
    if attended <=0 or attended > total_classes:
        return None
    attendance_percentage = (attended/total_classes)*100
    return attendance_percentage

def check_attendance_eligibility(percentage):
    if percentage >= 75:
        return True
    else:
        return False
    
def display_attendance_status(percentage):
    if percentage >= 75:
        print("Attendance : ",round(percentage,2),"%")
        print("status : Eligible")
    else:
        print("Attendance : ",round(percentage,2),"%")
        print("Status : Not eligible")     

   