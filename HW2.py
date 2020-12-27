firstname = str(input("First Name: "))
lastname = str(input("Last Name: "))
age = int(input("Your Age: "))
dateofbirth = int((input("Date of birth(Just Year): ")))

z=list([firstname , lastname , age , dateofbirth])

for i in z:
    print(i)
if age < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")
