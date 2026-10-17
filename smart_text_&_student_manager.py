# smart text & student manager

# function

def show_header(title):
    print("\n" "=" * 40)
    print(title.center(40))
    print("=" * 40)

def get_grade(marks):
    if marks>= 80:
        print("A  -  pass")
    elif marks >= 60:
        print("B  -  pass")
    elif marks >= 40:
        print("C  -  pass")
    else:
        print("Fail")

def get_status(marks):
    if marks >= 40:
        return "pass"
    else:
        return "fail"

def calculate_average(*marks):
    return sum(marks) / len(marks)

def analyze_text(text):
    print(f"\n{'Original : '.ljust(15)} {text}")
    print(f"{'Upper : '.ljust(15)} {text.upper()}")
    print(f"{'Lower : ' .ljust(15)} {text.lower()}")
    print(f"{'Title : '.ljust(15)} {text.title()}")
    print(f"{'Revarsed : '.ljust(15)} {text[::-1]}")
    print(f"{'Length : '.ljust(15)} {len(text)}")
    print(f"{'Word : '.ljust(15)} {len(text.split())}")

def formate_roll (roll):
    return str(roll).zfill(3)

def show_table(students):
    print(f"\n {'#' :<4} {'Roll' :<6} {'Name' :<12} {'Avg' :<8} {'Grade' :<6} {'Status'}")
    for i, s in enumerate(students,1):
        print(f"{i:<4} {formate_roll(s['roll']):<6} {s['name'].title():<12} {s['average']:<8.2f} {s['grade']:<6} {s['status']}")

# main program

show_header("SMART TEXT & STUDENT MANAGER")

sections = ("A","B","C","D")

students = []

total = int(input("HOW MANY STUDENTS ? ENTER HERE! :- "))

show_header("STUDENTS DATA")

for i in range(total):
    print(f"\n---Students{i+1}---")

name = input("ENTER NAME : ").strip().title()
roll = int(input("ENTER ROLL NO. :- "))

print("SECTION..")
for j,sec in enumerate(sections,1):
    print(f"{j}. section{sec}")
choice = int(input("Choose: "))
section = sections-[choice-1]

math = float(input("MATH :- "))
english = float(input("ENGLISH :- "))
sicence = float(input("SICENCE :-"))

avg = calculate_average(math,english,sicence)
grade = get_grade(avg)
status = get_status(avg)

email = f"{name.lower().replace(" ",".")} {formate_roll(roll)}@school.pk"

student ={
    'name' : name,
    'roll' : roll,
    'section' : sections,
    'math' : math,
    'english' : english,
    'sicence' : sicence,
    'average' : avg,
    'grade' : grade,
    'status' :  status,
    'email' : email
}

students.append(student)
print(f"{name} Aaded...")
print(f"Email :- {email}")

show_header("FULL REPORT")
show_table(students)

show_header("CLASS RANKING")
sorted_students = sorted(students,key=lambda x :x["average"],reverse=True)
for i, s in enumerate(sorted_students,1):
    rank_text = f"{i}. {s['name']:<12} roll: {formate_roll(s[roll])} avg: {s['average']:2f} -- {s['grade']}"
    print(rank_text)

