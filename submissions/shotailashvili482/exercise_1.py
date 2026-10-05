age = int(input("How old are you?\n").strip())

if age > 17:
    print("Adult")
elif 13 <= age <= 17:
    print("Teen")
else:
    print("Child")