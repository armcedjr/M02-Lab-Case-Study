# -*- coding: utf-8 -*-
"""
Armando Cedano
Dean's List/ Honor Roll Verification App
This app will accept studemt information will ZZZ is entered for the last name. Then, it will check the student credentials to verify if they qualify for the Dean's List or the Honor Roll
"""

def main():
    students = []

    while True:
        last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        students.append({
            'last_name': last_name,
            'first_name': first_name,
            'gpa': gpa
        })

    print("\nStudent Qualifications:")
    print("-----------------------")

    for student in students:
        print(f"\nName: {student['first_name']} {student['last_name']}")
        print(f"GPA: {student['gpa']}")

        if student['gpa'] >= 3.5:
            print("Dean's List: Congratulations! You made the Dean's List.")
        elif student['gpa'] >= 3.25:
            print("Honor Roll: Congratulations! You made the Honor Roll.")
        else:
            print("No special recognition this time.")

if __name__ == "__main__":
    main()
