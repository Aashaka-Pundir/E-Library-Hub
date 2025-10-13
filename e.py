import os

def write_story():
    title = input("Enter story title: ")
    author = input("Enter your name: ")
    print("Start writing your story. Type 'END' to finish.")

    content = ""
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        content += line + "\n"

    filename = f"{title.replace(' ', '_')}.txt"
    with open(filename, "w") as file:
        file.write(f"Title: {title}\nAuthor: {author}\n\n{content}")
    print(f"Story saved as '{filename}'")

def list_stories():
    print("\n Available Stories:")
    for file in os.listdir():
        if file.endswith(".txt"):
            print(f"- {file}")

def read_story():
    list_stories()
    filename = input("\nEnter the filename to read: ")
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("\n--- Story Content ---")
            print(file.read())
    else:
        print("Story not found.")

def edit_story():
    list_stories()
    filename = input("\nEnter the filename to edit: ")
    if os.path.exists(filename):
        print("Add new content. Type 'END' to finish.")
        new_content = ""
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            new_content += line + "\n"
        with open(filename, "a") as file:
            file.write("\n--- Edited Content ---\n")
            file.write(new_content)
        print("Story updated.")
    else:
        print("Story not found.")

def delete_story():
    list_stories()
    filename = input("\nEnter the filename to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("Story deleted.")
    else:
        print("Story not found.")

while True:
    print("\nChoose an option:")
    print("1. Write a new story")
    print("2. Read a story")
    print("3. Edit a story")
    print("4. Delete a story")
    print("5. List all stories")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == "1":
        write_story()
    elif choice == "2":
        read_story()
    elif choice == "3":
        edit_story()
    elif choice == "4":
        delete_story()
    elif choice == "5":
        list_stories()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

