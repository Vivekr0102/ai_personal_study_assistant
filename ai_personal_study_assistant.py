import json
import random
import datetime
import os

# Filenames
NOTES_FILE = "notes.json"
TODO_FILE = "todo.json"
FLASHCARDS_FILE = "flashcards.json"

# Ensure files exist
def ensure_file(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)

# Create files at the start
for f in [NOTES_FILE, TODO_FILE, FLASHCARDS_FILE]:
    ensure_file(f)

# Load and save data
def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Note-taking
def take_note():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = load_data(NOTES_FILE)
    data.append({"note": note, "timestamp": timestamp})
    save_data(NOTES_FILE, data)
    print("✅ Note saved.")

# To-do list
def add_task():
    task = input("Enter task: ")
    data = load_data(TODO_FILE)
    data.append({"task": task, "done": False})
    save_data(TODO_FILE, data)
    print("✅ Task added.")

def view_tasks():
    tasks = load_data(TODO_FILE)
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {status} {t['task']}")
    print()

def mark_task_done():
    view_tasks()
    tasks = load_data(TODO_FILE)
    if not tasks:
        return
    idx = int(input("Enter task number to mark done: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_data(TODO_FILE, tasks)
        print("✅ Task marked as done.")
    else:
        print("Invalid task number.")

# Flashcards
def add_flashcard():
    question = input("Enter question: ")
    answer = input("Enter answer: ")
    cards = load_data(FLASHCARDS_FILE)
    cards.append({"q": question, "a": answer})
    save_data(FLASHCARDS_FILE, cards)
    print("✅ Flashcard added.")

def quiz_me():
    cards = load_data(FLASHCARDS_FILE)
    if not cards:
        print("No flashcards available.")
        return
    card = random.choice(cards)
    user_answer = input(f"❓ {card['q']} \nYour Answer: ")
    if user_answer.lower() == card["a"].lower():
        print("🎉 Correct!")
    else:
        print(f"❌ Incorrect. Correct answer: {card['a']}")

# Suggest resources
def suggest_resources():
    subject = input("Enter subject: ").lower()
    resources = {
        "python": ["W3Schools", "RealPython", "Python Docs"],
        "math": ["Khan Academy", "Paul's Online Notes"],
        "ai": ["DeepLearning.ai", "Google AI Blog"],
    }
    print("📚 Resources:")
    for res in resources.get(subject, ["No suggestions found."]):
        print(f"- {res}")

# Main menu
def main():
    print("🤖 Welcome to AI Personal Study Assistant")
    while True:
        print("\nChoose an option:")
        print("1. Take a Note")
        print("2. Add To-Do Task")
        print("3. View Tasks")
        print("4. Mark Task Done")
        print("5. Add Flashcard")
        print("6. Quiz Me")
        print("7. Suggest Resources")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            take_note()
        elif choice == '2':
            add_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            mark_task_done()
        elif choice == '5':
            add_flashcard()
        elif choice == '6':
            quiz_me()
        elif choice == '7':
            suggest_resources()
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
