print("=" * 40)
print("student markes analyzer")
print("=" * 40)

total_makrs = 0
even_roll = 0
odd_roll = 0
best_marks = 0
best_student = ""

student = int(input("how many student? :-"))

for i in range(1,student + 1):
    print(f"_____student {i}_____")
    name = input("name:- ")
    roll_number = int(input("roll number "))
    marks = float(input("marks:- 100/"))

    if roll_number % 2 == 0:
        even_roll = even_roll + 1
    else:
        odd_roll = odd_roll + 1

    total_makrs = total_makrs + marks

    if marks > best_marks:
        best_marks = marks
        best_student = name

        if marks >= 80:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            garde = "f"

        print(f"garde : {grade}\n")

averange = total_makrs / student
print("=" * 40)
print("                 final report             ")
print("=" * 40)
print(f"total student    :{student}")
print(f"even roll number :{even_roll}")
print(f"odd roll number  :{odd_roll}")
print(f"total makrs      :{total_makrs:.2f}")
print(f"class averange   :{averange:.2f}")
print(f"best student     :{best_student}({best_marks} marks)")
print("=" * 40)



