'''
This is a CLI version of Shobkaaj.
'''
from __future__ import annotations
from models.worker import add_worker


def print_menu() -> None:
    print("\n=== Shobkaaj Platform ===")
    print("1. Register as Worker")
    print("2. Register as Client")
    print("3. Post a Job")
    print("4. View Open Jobs")
    print("5. Apply to a Job")
    print("6. Exit")
    
def main() -> None:
    students: list[dict] = [] #List to contain student
    while True:
        print_menu()
        choice: str = input("Chose an option (1-6): ").strip()
        #Match-case is only available in Python 3.10 
        match choice:
            case "1":
                register_worker(students)
            case "2":
                print("Listing students and results...")
            case "3":
                print("Searching student by id...")
            case "4":
                print("Deleting student by id...")
            case "5":
                print("Exporting results to CSV...")
            case "6":
                print("Exiting the program. Goodbye!")    
                break
            case _:
                print("Invalid option. Please choose a number between 1 and 6.")
        
        
if __name__ == "__main__":
    main()