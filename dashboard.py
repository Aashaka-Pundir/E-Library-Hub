import os

USER_FILE = "users.txt"
STORY_FILE = "story_catalog.txt"

def view_users():
    print("\n Registered Users:")
    if not os.path.exists(USER_FILE):
        print("No users found.")
        return
    with open(USER_FILE, "r") as file:
        for line in file:
            username, _ = line.strip().split(",")
            print(f"- {username}")

def view_stories():
    print("\n Story Catalog:")
    if not os.path.exists(STORY_FILE):
        print("No stories found.")
        return
    with open(STORY_FILE, "r") as file:
        for line in file:
            title, author, genre = line.strip().split(",")
            print(f"- {title} by {author} [{genre}]")

def delete_user():
    username = input("Enter username to delete: ")
    if not os.path.exists(USER_FILE):
        print("No users found.")
        return
    lines = []
    deleted = False
    with open(USER_FILE, "r") as file:
        for line in file:
            user, _ = line.strip().split(",")
            if user != username:
                lines.append(line)
            else:
                deleted = True
    with open(USER_FILE, "w") as file:
        file.writelines(lines)
    print("User deleted." if deleted else " User not found.")

def delete_story():
    title = input("Enter story title to delete: ")
    if not os.path.exists(STORY_FILE):
        print("No stories found.")
        return
    lines = []
    deleted = False
    with open(STORY_FILE, "r") as file:
        for line in file:
            story_title, _, _ = line.strip().split(",")
            if story_title.lower() != title.lower():
                lines.append(line)
            else:
                deleted = True
    with open(STORY_FILE, "w") as file:
        file.writelines(lines)
    print("Story deleted." if deleted else "Story not found.")

def search_user():
    keyword = input("Enter username to search: ").lower()
    found = False
    with open(USER_FILE, "r") as file:
        for line in file:
            username, _ = line.strip().split(",")
            if keyword in username.lower():
                print(f" Found user: {username}")
                found = True
    if not found:
        print("User not found.")

def search_story():
    keyword = input("Enter story title or author to search: ").lower()
    found = False
    with open(STORY_FILE, "r") as file:
        for line in file:
            title, author, genre = line.strip().split(",")
            if keyword in title.lower() or keyword in author.lower():
                print(f" Found: {title} by {author} [{genre}]")
                found = True
    if not found:
        print(" Story not found.")

while True:
    print("\n️ Admin Dashboard")
    print("1. View Users")
    print("2. View Stories")
    print("3. Delete User")
    print("4. Delete Story")
    print("5. Search User")
    print("6. Search Story")
    print("7. Exit")

    choice = input("Choose an option (1–7): ")

    if choice == "1":
        view_users()
    elif choice == "2":
        view_stories()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        delete_story()
    elif choice == "5":
        search_user()
    elif choice == "6":
        search_story()
    elif choice == "7":
        print(" Exiting Admin Dashboard.")
        break
    else:
        print(" Invalid choice.")