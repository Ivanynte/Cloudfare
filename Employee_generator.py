first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
full_name = first_name + ' ' + last_name
address = str(input('Enter your address: '))
address += str(input('Enter your city: '))
employee_age = int(input('Enter your age: '))
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = int(input('Enter your experience years: '))
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = str(input('Enter your position: '))
salary = str(input('Enter your salary: '))
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)




  

    


