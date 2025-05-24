import random

def show_joke():
    try:
        with open("jokes.txt", "r") as file:
            jokes = file.readlines()
            joke = random.choice(jokes)
            print("\n😂 Here's a joke for you:\n" + joke)
    except FileNotFoundError:
        print("Oops! jokes.txt file not found!")

def main():
    while True:
        print("\nMenu:")
        print("1. See a joke")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            show_joke()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()

