age = int(input("Enter Your age: \n").strip())

if age < 13:
    print ("child")
elif age <= 17:
    print ("teen")
else:
    print("adult")