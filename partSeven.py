flag = True
while flag:
    num1 = int(input("Please input the first number: "))
    num2 = int(input("Please input the second number: "))
    operation = input("Enter the operation or type quit: ")

    if operation == "quit":
        print("Now quitting")
        break
    else:
        match operation:
            case "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            case "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            case "*":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            case "^":
                result = num1 ** num2
                print(f"{num1} ^ {num2} = {result}")
            case "%":
                if num2 == 0:
                    print ("You use modulus with 0 as your second number")
                else:
                    result = num1 % num2
                    print(f"{num1} % {num2} = {result}")
            case "/":
                if num2 == 0:
                    print ("You cannot divide by 0")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            case _:
                print("Error")