Classes = {}

students = []
teachers = []

student_id = 10000
teacher_id = 50000


Teacher = """ 
1. Assign Student Grades 
2. Assign Student Tasks 
3. Summary of the Assignment (completed,pending)
4. Mark Attendance
5. Get Student Profile 
"""


Student = """
1. Look up the assignments 
2. Update assignment status (mark the assignment as completed)
3. Check Attendance 
4. Display Report card (formatted report card)
"""


application_name = "Student Management"

options = """Options:
1. Sign in
2. Sign up 
"""


while True:
    print(application_name + ":")
    print(options)

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("--- Sign In ---")
            role = input("Choose your role (Student/Teacher): ").lower()

            if role == "student":
                sid = int(input("Enter Student ID: "))
                password = input("Enter Password(five digit): ")

                for student in students:
                    if student["ID"] == sid and student["Password"] == password:
                        print("Login Successful!")
                        print("Welcome", student["Name"])

                        while True:
                            print(Student)
                            option = int(input("Choose an option: "))

                            match option:
                                case 1:
                                    print("Assignments:")
                                    print(student["Assignments"])

                                case 2:
                                    print("Update Assignment Status")

                                case 3:
                                    print("Attendance:")
                                    print(student["Attendance"])

                                case 4:
                                    print("Report Card")
                                    print("Name:", student["Name"])
                                    print("Class:", student["Classes"])

                                case _:
                                    print("Invalid option")

                            again = input("Continue student menu? (y/n): ")
                            if again == "n":
                                break

                        break

                else:
                    print("Invalid Student ID or Password")


            elif role == "teacher":
                tid = int(input("Enter Teacher ID: "))
                password = input("Enter Password: ")

                for teacher in teachers:
                    if teacher["ID"] == tid and teacher["Password"] == password:
                        print("Login Successful!")
                        print("Welcome", teacher["Name"])

                        while True:
                            print(Teacher)

                            option = int(input("Choose an option: "))

                            match option:
                                case 1:
                                    print("Assign Student Grades")

                                case 2:
                                    print("Assign Student Tasks")

                                case 3:
                                    print("Summary of Assignment")

                                case 4:
                                    print("Mark Attendance")

                                case 5:
                                    print("Get Student Profile")

                                case _:
                                    print("Invalid option")

                            again = input("Continue teacher menu? (y/n): ")
                            if again == "n":
                                break

                        break

                else:
                    print("Invalid Teacher ID or Password")


        case 2:
            print("--- Sign Up ---")

            role = input("Choose your role (Student/Teacher): ").lower()

            if role == "student":

                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                dob = input("Enter Date of Birth(mm/dd/yyyy): ")
                Class = input("Enter Class: ")
                password = input("Create Password(5 digit): ")

                student = {
                    "ID": student_id,
                    "Name": name,
                    "Age": age,
                    "Date of Birth": dob,
                    "Classes": Class,
                    "Password": password,
                    "Role": "Student",
                    "Assignments": [],
                    "Attendance": []
                }

                students.append(student)

                if Class in Classes:
                    Classes[Class].append(student_id)
                else:
                    Classes[Class] = [student_id]

                print("Student account created successfully!")
                print("Your Student ID is:", student_id)

                print(Classes)

                student_id += 1


            elif role == "teacher":

                name = input("Enter Name: ")
                subject = input("Enter Subject: ")
                password = input("Create Password(5 digit): ")

                teacher = {
                    "ID": teacher_id,
                    "Name": name,
                    "Subject": subject,
                    "Password": password,
                    "Role": "Teacher"
                }

                teachers.append(teacher)

                print("Teacher account created successfully!")
                print("Your Teacher ID is:", teacher_id)

                teacher_id += 1


            c = input("Would you like to continue? (y/n): ")

            if c == "y":
                print("Continuing sign-up...")
            else:
                print("Cancelled sign-up.")


        case _:
            print("Invalid option")
