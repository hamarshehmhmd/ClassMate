class Person:
    def __init__(self, name, surename, id):
        self.name = name
        self.surename = surename
        self.id = id


    def information(self, name, surename, id):
        pass


class Student(Person):
    def __init__(self, name, surename, id, gpa, PassedHrs):
        super().__init__(name, surename, id)
        self.classes = []
        self.gpa = gpa
        self.PassedHrs = PassedHrs

    def enrolled(self, course):
        self.classes.append(course)

    # I know it is not needed but it will make it easier for me in the tester class to
    # add courses for a student
    def SemesterLoad(self):
        print("Enter Course Name and Credit Hours: (Separated by a comma)")
        print("To exit, enter 'done'.")
        while True:
            input_str = input("> ")
            if input_str == "done":
                break

            parts = input_str.split(",")
            if len(parts) != 2:
                print("Invalid input, please enter course name and credit hours separated by a comma.")
                continue

            course_name, credit_hours_str = parts
            credit_hours = 0
            while credit_hours <= 0:
                try:
                    credit_hours = int(credit_hours_str)
                except ValueError:
                    print("Invalid hours, please enter a number.")
                    credit_hours_str = input("Enter Credit Hours: ")

            course = Course(course_name.strip(), credit_hours)
            self.enrolled(course)

    def GPA_calc(self, grades):
        credit_hours = 0
        grades_calc = 0
        for course in self.classes:
            credit_hours += course.credit_hours
            grade = grades[course.name]
            if grade >= 60:
                self.PassedHrs += course.credit_hours
            grades_calc += course.credit_hours * grade

        self.gpa = grades_calc / credit_hours

    def display(self):
        print("---------------------------------------------------------")
        print(f"Name: {self.name} {self.surename}")
        print(f"ID: {self.id}")
        print(f"GPA: {self.gpa}")
        print(f"Passed Hours: {self.PassedHrs}")
        print(f"Classes: {[course.name for course in self.classes]}")
        print("---------------------------------------------------------")



class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours


class Lecturer(Person):
    def __init__(self, name, surname, number):
        super().__init__(name, surname, number)
        self.classes_taught = {}

    def SemesterLoad(self):
        self.classes_taught = {}
        print("Enter Course Name and Credit Hours:(Seperated by a comma)")
        print("To exit Enter (exit)")
        while True:
            input_str = input("> ")
            if input_str == "exit":
                break

            parts = input_str.split(",")
            if len(parts) != 2:
                print("Invalid input, please enter course name and credit hours separated by a comma.")
                continue

            course_name, credit_hours_str = parts
            credit_hours = 0
            while credit_hours <= 0:
                try:
                    credit_hours = int(credit_hours_str)
                except ValueError:
                    print("Invalid hours, please enter a number.")
                    credit_hours_str = input("Enter Credit Hours: ")

            self.classes_taught[course_name.strip()] = credit_hours

    def display(self):
        print("---------------------------------------------------------")
        print(f"Name: {self.name} {self.surname}")
        print(f"ID: {self.ID}")
        print(f"Classes Taught: {self.classes_taught}")
        print("---------------------------------------------------------")





#Tester
while True:
    type = input("Are you a student or a lecturer? ")

    #Student
    if type.lower() == "student":
        name = input("Enter your First Name: ")
        surname = input("Enter your surname: ")
        ID = input("Enter your ID: ")
        gpa = 0.0
        passed_hours = 0
        s = Student(name, surname, ID, gpa, passed_hours)
        s.SemesterLoad()
        grades = {}
        for course in s.classes:
            grade = float(input(f"Enter grade for {course.name}: "))
            grades[course.name] = grade
        s.GPA_calc(grades)

        #To show Student Info
        s.display()
        break

    #Teacher/Lecturer
    elif type.lower() == "lecturer":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        ID = input("Enter your ID: ")
        l = Lecturer(name, surname, ID)
        l.SemesterLoad()

        # To show Teacher/Lecturer Info
        l.display()
        break

    else:
        print("Invalid Input, Please Try Again...")


