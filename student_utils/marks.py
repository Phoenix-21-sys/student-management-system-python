def calculate_total(marks):
    total = sum(marks)
    return total

def calculate_average(marks):
    if not marks:
        return 0
    average = sum(marks)/len(marks)
    return average

def highest_mark(marks):
    if not marks:
        return 0
    return max(marks)

def lowest_mark(marks):
    if not marks:
        return 0
    return min(marks)

def check_pass(marks):
      is_pass = lambda mark:mark >= 40
      return list(map(is_pass,marks))