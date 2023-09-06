from random import randint

def create_account(emp_name):
    if len(emp_name) < 5:
        emp_name = emp_name + str(randint(1000, 9999))
    return emp_name[:5]

employee_names = [["Saumel", "Gompers"], ["Laundry", "Blurshiff"]]

print(create_account(employee_names[0][1]))