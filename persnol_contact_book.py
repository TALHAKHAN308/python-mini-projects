print("=" * 40)
print("----- persnol contact book -----")
print("=" * 40)

names = []
phones = []
cities = []

categories = ("family","friend","work","other")

total = int(input("how many contacts are :- "))

print("\n--- enter here --- ")
for i in range(total):
    print(f"---- contact {i+1} ---- ")
    name = input("name      :- ")
    phone = input("phone no.:- ")
    city = input("city      :-")

print("\n choose a category")
for j in range(len(categories)):
    print(f"{j+1},{categories[j]}")

choice = int(input("enter number :-"))
category = categories[choice - 1]

names.append(name)
phones.append(phone)
cities.append(city)

print(f"{name} added")

# search contact

print("\n" + "=" * 40)
search = input("search your contact :- ")

found = False
for i in range(total):
    if search.lower() in names[i]:
        print(f"\n cotact are mach")
        print(f"name   : {names[i]}")
        print(f"phone  : {phones[i]}")
        print(f"city   : {cities[i]}")
        found = True

        if not found:
            print(f" {search} empty")

unique_cities = []
for city in cities:
    if city not in unique_cities:
        unique_cities.append(city)

sorted_name = sorted(names)

print("\n" + "=" * 40)
print("            STATS            ")
print("=" * 40)
print(f"Total Contacts:     {total}")
print(f"Total cities:       {len(unique_cities)}")
print(f"Cities:             {unique_cities}")
print("\n sorted contact: ")
for name in sorted_name:
    print(f"  >>  {name}")
print("=" * 40)