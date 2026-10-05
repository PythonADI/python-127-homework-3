day = input("What day is it?\n").strip().lower()

if day == "saturday" or day == "sunday":   
    print("Weekend!")
else:
    print("Not the weekend.")