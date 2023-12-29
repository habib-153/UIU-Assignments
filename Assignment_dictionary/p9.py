company_hr_register = {
    101: {'name': 'Alice', 'age': 35, 'performance': 90, 'salary': 50000},
    102: {'name': 'Bob', 'age': 58, 'performance': 98, 'salary': 70000},
    103: {'name': 'Charlie', 'age': 45, 'performance': 85, 'salary': 60000},
    104: {'name': 'David', 'age': 60, 'performance': 75, 'salary': 55000},
    105: {'name': 'Eve', 'age': 28, 'performance': 92, 'salary': 48000},
    106: {'name': 'Frank', 'age': 50, 'performance': 55, 'salary': 52000},
    107: {'name': 'Grace', 'age': 62, 'performance': 97, 'salary': 75000},
}
updated_company_hr_register = {}
total_employees = 0
bonus = 0
ages = [ values['age'] for values in company_hr_register.values()]
performances = [ values['performance'] for values in company_hr_register.values()]
# print(ages)
for i in range(len(ages)):
    if ages[i] > 55:
        total_employees += 1
        bonus += 10000
        if performances[i] > 95:
            bonus += 5000
        for key, value in company_hr_register.items():
            if value['age'] == ages[i]:
                updated_company_hr_register[key] = {'name': value['name']}

print(f"total_employees = {total_employees}")
print(f"total_bonus_amount = {bonus}")
print(f"updated_company_hr_register = \n{updated_company_hr_register}")