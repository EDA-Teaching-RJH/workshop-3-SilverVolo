age = int(input("Please input age: "))
student = input("Are you a student (y/n): ")

if age < 12 or age >= 65:
    print("£5")
elif student == "y":
    print("£8")
else:
    print("£5") 
