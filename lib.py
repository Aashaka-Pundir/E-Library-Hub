def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                print("Login successful!")
                return
    print("Invalid credentials.")

while True:
    choice = int(input("Choose 1-'register' \n 2-'login' \n 3-'exit': "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice==3:
        print("Exiting..")
        break
    else:
        print("Invalid choice.")
