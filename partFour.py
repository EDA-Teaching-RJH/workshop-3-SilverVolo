saved_username = "admin"
saved_password = "password123"

usernameInput = input("Please input the username: ")
passswordInput = input("Please input the password: ")

if usernameInput ==  saved_username and passswordInput == saved_password:
    print("Access granted")
else:
    print("Error \nAccess denied")
    