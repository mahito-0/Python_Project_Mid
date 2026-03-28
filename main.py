'''
This is a CLI version of Shobkaaj.
'''
from __future__ import annotations
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from models.worker import add_worker
from models.client import add_client
from models.job import manage_jobs
from models.application import add_application, view_applications
from utils.file_handler import load_data, save_data

WORKERS_FILE = "data/workers.json"
CLIENTS_FILE = "data/clients.json"
JOBS_FILE = "data/jobs.json"
APPLICATIONS_FILE = "data/applications.json"

console = Console()

def print_menu() -> None:
    menu_text = Text()
    menu_text.append("1. Register as Worker\n", style="cyan")
    menu_text.append("2. Register as Client\n", style="cyan")
    menu_text.append("3. Manage Jobs\n", style="green")
    menu_text.append("4. Apply to a Job\n", style="yellow")
    menu_text.append("5. View Applications\n", style="yellow")
    menu_text.append("6. Exit", style="red")
    
    panel = Panel(menu_text, title="[bold magenta]=== Shobkaaj Platform ===[/bold magenta]", expand=False, border_style="bold blue")
    console.print()
    console.print(panel)
    
def main() -> None:
    workers: list[dict] = load_data(WORKERS_FILE, []) #List of worker
    clients: list[dict] = load_data(CLIENTS_FILE, []) #List of client
    jobs: list[dict] = load_data(JOBS_FILE, []) #List of job
    applications: list[dict] = load_data(APPLICATIONS_FILE, []) #List of applications
    while True:
        print_menu()
        choice: str = console.input("[bold cyan]Choose an option (1-6): [/bold cyan]").strip()
        #Match-case is only available in Python 3.10 
        match choice:
            case "1":
                add_worker(workers)
                save_data(WORKERS_FILE, workers)
                console.print("\n[bold green]✔ Worker registered and saved successfully![/bold green]")
            case "2":
                add_client(clients)
                save_data(CLIENTS_FILE, clients)
                console.print("\n[bold green]✔ Client registered and saved successfully![/bold green]")
            case "3":
                manage_jobs(jobs)
                save_data(JOBS_FILE, jobs)
            case "4":
                add_application(applications)
                save_data(APPLICATIONS_FILE, applications)
                console.print("\n[bold green]✔ Application submitted and saved successfully![/bold green]")
            case "5":
                view_applications(applications)
            case "6":
                console.print("[bold red]Exiting the program. Goodbye![/bold red]")    
                break
            case _:
                console.print("[bold red] Invalid option. Please choose a number between 1 and 6.[/bold red]")
        
        
if __name__ == "__main__":
    main()