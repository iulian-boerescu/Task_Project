import json
from employer import list_employers
from departments import list_departments


def apply_bonus(employee):
    new_employee = employee.copy()
    total_salary = int(employee['salary'] + employee['bonus'])
    new_employee['total_salary'] = total_salary
    return new_employee


def apply_bonus_for_department(employee, department_name):
    new_employee = employee.copy()
    for index in employee:
        if department_name == 'IT' and 'Programmer' in index['job']:
            total_salary = int(employee['salary'] + employee['bonus'])
            new_employee['total_salary'] = total_salary
            return new_employee


def display_employers_of_the_department(department):
    for index in list_departments:
        print(f'Members of the {department} Department are: {index[department]}')


def display_department_of_employee(employee_name):
    for index in list_employers:
        if index['first_name'] in str(employee_name):
            if 'Programmer' in index['job']:
                print('Is a member of It Department')
            else:
                print('Is a member of HR Department')


def add_employee(employee, employers):
    employers.append(employee)
    return employers


if __name__ == '__main__':

    new_employee = {
        'first_name': 'Mihaiu',
        'last_name': 'Raducu',
        'age': 29,
        'job': 'Junior Programmer',
        'salary': 2300,
        'bonus': 150,
        'total_salary': 0
    }

    # list_employers.append(new_employee)
    # list_employers.pop()
    # print(list_employers)
    # print(list_departments)
    # display_department_of_employee('Laur')
    # list_employers[0]['bonus'] = 150
    # list_employers = list(map(apply_bonus, list_employers))
    # display_employers_of_the_department('HR')
    # apply_bonus_for_department(list_employers, 'IT')
    # print(list_employers)

    with open('employers.json', 'w') as json_file:
        json.dump(list_employers, json_file, indent=2)

    with open('departments.json', 'w') as json_file:
        json.dump(list_departments, json_file, indent=2)





