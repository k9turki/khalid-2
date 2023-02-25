school = {}

def add_class():
    class_name = input("Enter the class name: ")
    school[class_name] = []

def add_student():
    class_name = input("Enter the class name: ")
    if class_name not in school:
        print("Class not found.")
        return
    student_name = input("Enter the student name: ")
    school[class_name].append(student_name)

def print_school():
    if not school:
        print("School is empty.")
        return
    for class_name, students in school.items():
        print(f"Class {class_name}: {', '.join(students)}")

def print_student():
    student_name = input("Enter the student name: ")
    for class_name, students in school.items():
        if student_name in students:
            print(f"{student_name} is in class {class_name}")
            return
    print(f"{student_name} not found in any class.")

while True:
    print("Menu:")
    print("1- Add class")
    print("2- Add student to class")
    print("3- Print the whole school")
    print("4- Print specific student")
    print("5- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_class()
    elif choice == "2":
        add_student()
    elif choice == "3":
        print_school()
    elif choice == "4":
        print_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
