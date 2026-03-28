import json
from typing import Any
from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float, prompt_str

class Application:
    def __init__(self, application_id: str, job_id: str, worker_id: str, application_status: str) -> None:
        self.application_id = application_id
        self.job_id = job_id
        self.worker_id = worker_id
        self.application_status = application_status

    def to_dict(self):
        return {
            "application_id": self.application_id,
            "job_id": self.job_id,
            "worker_id": self.worker_id,
            "application_status": self.application_status
        }

def add_application(applications: list[dict]) -> None:
    application_id = str(prompt_int("Enter application ID: "))
    job_id = str(prompt_int("Enter job ID: "))
    worker_id = str(prompt_int("Enter worker ID: "))
    application_status = prompt_on_empty("Enter application status: ")

    application_obj = Application(application_id, job_id, worker_id, application_status)
    applications.append(application_obj.to_dict())

def view_applications(applications: list[dict]) -> None:
    from rich.console import Console
    from rich.table import Table

    console = Console()
    table = Table(title="[bold blue]Applications[/bold blue]", show_lines=True)

    table.add_column("App ID", style="cyan", justify="center")
    table.add_column("Job ID", style="magenta", justify="center")
    table.add_column("Worker ID", style="yellow", justify="center")
    table.add_column("Status", style="green")

    for application in applications:
        table.add_row(
            application['application_id'],
            application['job_id'],
            application['worker_id'],
            application['application_status']
        )
        
    if table.row_count > 0:
        console.print(table)
    else:
        console.print("\n[bold yellow]No applications found.[/bold yellow]")