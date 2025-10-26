import os

CATALOG_FILE = "story_catalog.txt"

def add_story():
    title = input("Enter story title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    with open(CATALOG_FILE, "a") as file:
        file.write(f"{title},{author},{genre}\n")
    print(" Story added to catalog.")

def view_catalog():
    if not os.path.exists(CATALOG_FILE):
        print(" No stories found.")
        return
    print("\n Story Catalog:")
    with open(CATALOG_FILE, "r") as file:
        for line in file:
            title, author, genre = line.strip().split(",")
            print(f"- {title} by {author} [{genre}]")

def search_story():
    keyword = input("Enter title or author to search: ").lower()
    found = False
    with open(CATALOG_FILE, "r") as file:
        for line in file:
            title, author, genre = line.strip().split(",")
            if keyword in title.lower() or keyword in author.lower():
                print(f" Found: {title} by {author} [{genre}]")
                found = True
    if not found:
        print(" Story not found.")


while True:
    print("\n Story Catalog Menu")
    print("1. Add Story")
    print("2. View Catalog")
    print("3. Search Story")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        add_story()
    elif choice == "2":
        view_catalog()
    elif choice == "3":
        search_story()
    elif choice == "4":
        print("Exiting...!")
        break
    else:
        print(" Invalid choice.")

 
