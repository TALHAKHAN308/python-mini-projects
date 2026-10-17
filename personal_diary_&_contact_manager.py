# personal diary & contact manager
print("=" * 45)
print("        Personal Diary & Contact Manager        ")
print("=" * 45)

categories = ("Family","Friend","Work","Other")

contact = []

diary = []

# contact add

total = int(input("\n How Many Contacts Add A List Write...  "))

for i in range(total):
    print(f"---- Contact{i+1} ----")

    name = input("Enter Your Name:- ")
    phone = input("Enter Your Phone NO.:- ")
    city = input("Enter Your City:- ")
    score = int(input("Enter Your Score(1-10):- "))

    print("\n Categories....")
    for j in range(len(categories)):
        print(f"{j+1}. {categories[j]}")

    choice = int(input("Choose... "))

    New_contact = {
            "name": name,
            "phone": phone,
            "city": city,
            "score": score,
            "categories": categories[choice - 1]
        }
    contact.append(New_contact)
    print(f"{name} Contact Added....")

# Diary Notes

print("\n" + "=" * 45)
print("        Diary Notes        ")
print("=" * 45)

total_notes = int(input("How Many Notes?... "))

for i in range(total_notes):
    note = input(f"note {i+1}: ")
    diary.append(note)
    print(f"Note Saved suscesfully... ")

# Contact List

print("\n" + "=" * 55)
print("         Contact List          ")
print("=" * 55)
print(f"{'#' : <4} {'name' : <12} {'phone' : <15} {'city' : <10} {'score' : <6} {'category'}")
print("-" * 55)
for i in range(len(contact)):
    c = contact[i]
    print(f"{i+1:<4} {c['name']:<12} {c['phone']:<15} {c['city']:<10} {c['score']:<6} {c['categories']}")

# Ranking

