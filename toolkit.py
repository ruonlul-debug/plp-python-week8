# ====================================================
# Project Title: Personal Mini-Toolkit
# Description: A menu-driven Python program combining 
#              lists, loops, conditionals, and f-strings.
# ====================================================

# Tool 1: To-Do List Manager (Uses lists, loops, and conditionals)
def todo_list_manager():
    """Manages a dynamic to-do list where users can view, add, and remove tasks."""
    tasks = ["Review Python notes", "Complete Week 8 project"]
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is currently empty!")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
        elif choice == "2":
            new_task = input("Enter the task you want to add: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success! '{new_task}' has been added to your list.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to remove!")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
                try:
                    rem_choice = int(input("Enter the number of the task to remove: "))
                    if 1 <= rem_choice <= len(tasks):
                        removed = tasks.pop(rem_choice - 1)
                        print(f"Removed '{removed}' from your list.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")


# Tool 2: Tip & Split Calculator (Uses conditionals and arithmetic)
def tip_calculator():
    """Calculates tip amounts and splits restaurant bills evenly."""
    print("\n--- Tip & Split Calculator ---")
    try:
        bill_amount = float(input("Enter the total bill amount ($): "))
        tip_percent = float(input("Enter the tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter the number of people splitting the bill: "))
        
        if bill_amount < 0 or tip_percent < 0 or people <= 0:
            print("Amounts must be positive and number of people must be at least 1.")
            return
            
        tip_amount = bill_amount * (tip_percent / 100)
        total_bill = bill_amount + tip_amount
        per_person = total_bill / people
        
        print("\n--- Bill Summary ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill (including tip): ${total_bill:.2f}")
        print(f"Each person pays: ${per_person:.2f}")
        print("--------------------")
    except ValueError:
        print("Invalid input! Please enter valid numbers for bills and people.")


# Tool 3: Guess the Number Game (Uses loops and conditionals)
def guessing_game():
    """A mini number-guessing game with interactive feedback loops."""
    print("\n--- Guess the Number Game ---")
    secret_number = 7
    attempts = 0
    
    print("I have picked a number between 1 and 10. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess (or 0 to exit): "))
            if guess == 0:
                print("Exiting game. Thanks for playing!")
                break
            
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    """Main program loop displaying the toolkit menu."""
    print("========================================")
    print("       WELCOME TO YOUR MINI-TOOLKIT     ")
    print("========================================")
    
    while True:
        print("\nPlease select a tool from the menu below:")
        print("  1. Quick To-Do List Manager")
        print("  2. Tip & Split Calculator")
        print("  3. Guess the Number Game")
        print("  4. Quit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            todo_list_manager()
        elif choice == "2":
            tip_calculator()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
