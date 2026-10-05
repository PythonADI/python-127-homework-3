age = int(input("How old are you?\n").strip()) 

status = "adult" if age >= 18 else "minor"
print(status)