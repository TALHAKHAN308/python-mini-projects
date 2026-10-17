print("=" * 40)
print("---------- class room manager ----------")
print("=" * 40)

names = []
marks = []
grades = []
rolls = []

total_student = int(input("how many students :- "))

print("fill the student details")

for i in range(total_student):
    print(f"------ student {i + 1} ------")
    name = input("Name   :- ")
    roll = int(input("roll n. :- "))
    mark = float(input("marks   :- "))

    names.append(name)
    rolls.append(roll)
    marks.append(mark)

    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 40:
        grade = "C"
    else:
        grade = "F"

    grades.append(grade)
    print(f"grades :- {grades}\n")

    total_marks = sum(marks)
    average = total_marks / total_student
    best_marks = max(marks)
    worst_marks = min(marks)

    best_index = marks.index(best_marks)
    worst_index = marks.index(worst_marks)

    even_roll = 0
    odd_roll = 0
    for roll in rolls:
        if roll % 2 == 0:
            even_roll = even_roll + 1
        else:
            odd_roll = odd_roll + 1

print("=" * 40)
print("------------ final report ------------")
print("=" * 40)
print(f"{'name':<12} {'roll' :>4} {'mark':>6} {'grade' :>6}")
print("-" * 40)

for i in range(total_student):
    print(f"{names[i]:<12} {rolls[i]:>4} {marks[i]:>6.1f} {grades[i]:>6}")

print("=" * 40)
print(f"total student:      {total_student}")
print(f"total marks:        {total_marks:.2f}")
print(f"class average:      {average:.2f}")
print(f"best student:       {names[best_index]} ({best_marks} marks)")
print(f"worst student:      {names[worst_index]} ({worst_marks} marks)")
print(f"even roll no:       {even_roll}")
print(f"odd roll no:        {odd_roll}")

print("=" * 40)