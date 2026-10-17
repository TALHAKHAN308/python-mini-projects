# smart school system

# functions
def show_header(title):
    print("=" * 50)
    print(f"         {title}")
    print("=" * 50)

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

def get_status(marks):
    if marks >= 40:
        return "PASS"
    return "FAIL"

def calculate_average(*marks):
    return sum(marks) / len(marks)

def show_student(student, number):
    print(f"\n-----student{number}-----")
    print(f"NAME:      {student['name']}")
    print(f"ROLL NO.:  {student['roll']}")
    print(f"MATH:      {student['math']}")
    print(f"ENGLISH:   {student['english']}")
    print(f"SICENCE:   {student['sicence']}")
    print(f"AVERAGE:   {student['average']:.2f}")
    print(f"GRADE:     {student['grade']}")
    print(f"STATUS:    {student['status']}")

def show_table(students):
    print(f"\n{'#':<4} {'name' :<12} {'roll' :<6} {'average' :<8} {'grade' :<6} {'status'}")
    print("-" * 50)
    for i, s in  enumerate(students,1):
        print(f"{i :<4} {s['name']:<12} {s['roll']:<6} {s['average']:<8.2f} {s['grade']:<6} {s['status']}")

# Main program

show_header("SMART SCHOOL SYSTEM")

sections = ("A","B","C","D")

students = []

total = int(input("HOW MANY STUDENTS YOU ENTER :-  "))

show_header("ENTER STUDENTS DATA")

for i in range(total):
    print(f"\n---- Students {i + 1} ----")

    name = input("ENTER NAME :- ")
    roll = int(input("ENTER ROLL NO. :- "))

    print("CHOOSE THE SECTION")
    for j, sec in enumerate(sections,1):
        print(f"{j}. Section {sec}")
    choice = int(input("CHOOSE :- "))
    section = sections[choice - 1]

    math = float(input("ENTER MATH MARKS :- "))
    english = float(input("ENTER ENGLISH MARKS :- "))
    science = float(input("ENTER SICENCE MARKS :- "))

    avg = calculate_average(math, english,science)
    grade = get_grade(avg)
    status = get_status(avg)

    student = {
        "name": name,
        "roll": roll,
        "section": section,
        "math": math,
        "english": english,
        "science": science,
        "average":avg,
        "grade": grade,
        "status": status
    }
    students.append(student)
    print(f"{name} Addad.... ")

show_header("FULL REPORT")
show_table(students)

show_header("CLASS RANKING")
sorted_students = sorted(students,key=lambda x : x["average"],reverse=True)

for i, s in enumerate(sorted_students,1):
    print(f"{i}. {s['name']:<12} avg.{s['average']:.2f} - {s['grade']}")

show_header("SEARCH STUDENTS")
search = input("Enter Student Name Or Roll No. :-  ")

found = False
for i, s in enumerate(students, 1):
    if search.lower() in s["name"] or search == str(s["roll"]):
        show_student(s,i)
        found = True
        if not found:
            print(f"{search} epmty")

pass_count = 0
fail_count = 0
total_avg = 0
