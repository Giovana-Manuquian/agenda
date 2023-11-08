import os

grades = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)

def display_menu():
    print('----------------------------------------------------------------')
    print('                         Students Record                        ')
    print('----------------------------------------------------------------')
    print('1 - Register Student')
    print('2 - List Students')
    print('3 - Search Student')
    print('4 - Remove Student')
    print('5 - Exit')
    print('----------------------------------------------------------------')

def register_student():
    clear_screen()
    print('----------------------------------------------------------------')
    print('                         Students Register                      ')
    print('----------------------------------------------------------------')
    name = input("Please enter the student's name: ")
    math = float(input("Please enter the math grade: "))
    geo = float(input("Please enter the geo grade: "))
    history = float(input("Please enter the history grade: "))
    media = calculate_average([math, geo, history])
    grades[name] = {'math': math, 'geo': geo, 'history': history, 'media': media}
    print(f'Student {name} successfully registered!')

def list_students():
    clear_screen()
    print('----------------------------------------------------------------')
    print('                         List of Students                       ')
    print('----------------------------------------------------------------')
    for name, dados in grades.items():
        print(f'Name: {name}')
        print(f'Math: {dados["math"]}')
        print(f'Geo: {dados["geo"]}')
        print(f'History: {dados["history"]}')
        print(f'Media: {dados["media"]}')
        print('------------------------------------------------------------')

def search_student():
    clear_screen()
    print('----------------------------------------------------------------')
    print('                         Search Students                        ')
    print('----------------------------------------------------------------')
    name = input("Please enter the student's name: ")
    student = grades.get(name)
    if student:
        print(f'Name: {name}')
        print(f'Math: {student["math"]}')
        print(f'Geo: {student["geo"]}')
        print(f'History: {student["history"]}')
        print(f'Media: {student["media"]}')
    else:
        print(f'Student {name} not found.')

def remove_student():
    clear_screen()
    print('----------------------------------------------------------------')
    print('                         Remove Students                        ')
    print('----------------------------------------------------------------')
    name = input("Please enter the student's name you want to remove: ")
    student = grades.get(name)
    if student:
        del grades[name]
        print(f'Student {name} successfully removed!')
    else:
        print(f'Student {name} not found.')

while True:
    display_menu()
    option = int(input('Please, enter your option: '))
    
    if option == 1:
        register_student()
    elif option == 2:
        list_students()
    elif option == 3:
        search_student()
    elif option == 4:
        remove_student()
    elif option == 5:
        break
    else:
        print("Invalid option. Please choose a valid option.")
