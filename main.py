'''
This is a CLI version of Shobkaaj.
'''
from __future__ import annotations
from models.worker import add_worker
from utils.file_handler import load_data, save_data

WORKERS_FILE = "data/workers.json"

def print_menu() -> None:
    print("\n=== Shobkaaj Platform ===")
    print("1. Register as Worker")
    print("2. Register as Client")
    print("3. Post a Job")
    print("4. View Open Jobs")
    print("5. Apply to a Job")
    print("6. Exit")
    
def main() -> None:
    workers: list[dict] = load_data(WORKERS_FILE, []) #List to contain worker
    while True:
        print_menu()
        choice: str = input("Chose an option (1-6): ").strip()
        #Match-case is only available in Python 3.10 
        match choice:
            case "1":
                add_worker(workers)
                save_data(WORKERS_FILE, workers)
                print("\nWorker registered and saved successfully!")
            case "2":
                print("Register as Client")
            case "3":
                print("Post a Job")
            case "4":
                print("View Open Jobs")
            case "5":
                print("Apply to a Job")
            case "6":
                print("Exiting the program. Goodbye!")    
                break
            case _:
                print("Invalid option. Please choose a number between 1 and 6.")
        
        
if __name__ == "__main__":
    main()