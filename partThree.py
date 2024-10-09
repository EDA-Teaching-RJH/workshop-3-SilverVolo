flag = True

while flag:
    number = int(input("Enter number 1-100: "))
    
    if number > 100:
        print("Too high")
    elif number < 0: 
        print("Too low")
    else:
        flag = False

if number < 60:
    print("You got a F grade")
elif number <= 69:
    print("You got a D grade")
elif number <= 79:
    print("You got a C grade")
elif number <= 89:
    print("You got a B grade")
else:
    print("You got an A grade")
