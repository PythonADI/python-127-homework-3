score = int(input("Enter your score:\n").strip())

if score >= 90:
    print(f"Grade: A")
elif 80 <= score <= 89:
    print(f"Grade: B")
elif 70 <= score <= 79:
    print(f"Grade: C")
else:
    print(f"Grade: F")