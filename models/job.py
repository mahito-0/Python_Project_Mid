import json
import os
from typing import Any
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float, prompt_str

class Job:
    def __init__(self, job_id: str, job_title: str, job_description: str, job_location: str, job_rate: float, job_status: str) -> None:
        self.job_id = job_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.job_rate = job_rate
        self.job_status = job_status

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "job_title": self.job_title,
            "job_description": self.job_description,
            "job_location": self.job_location,
            "job_rate": self.job_rate,
            "job_status": self.job_status
        }

def add_job(jobs: list[dict]) -> None:
    job_id = str(prompt_int("Enter job ID: "))
    job_title = clean_name(prompt_str("Enter job title: "))
    job_description = prompt_on_empty("Enter job description: ")
    job_location = prompt_on_empty("Enter job location: ")
    job_rate = prompt_float("Enter job rate: ", min_val=0.0)
    job_status = "Open"

    job_obj = Job(job_id, job_title, job_description, job_location, job_rate, job_status)
    jobs.append(job_obj.to_dict())

def view_open_jobs(jobs: list[dict]) -> None:
    
    console = Console()
    table = Table(title="[bold green]Open Jobs[/bold green]", show_lines=True)

    table.add_column("Job ID", style="cyan", justify="center")
    table.add_column("Job Title", style="magenta")
    table.add_column("Description", style="white")
    table.add_column("Location", style="yellow")
    table.add_column("Rate", style="green", justify="right")
    table.add_column("Status", style="red")

    for job in jobs:
        if job["job_status"] == "Open":
            table.add_row(
                job['job_id'],
                job['job_title'],
                job['job_description'],
                job['job_location'],
                f"${job['job_rate']}",
                job['job_status']
            )
            
    if table.row_count > 0:
        console.print(table)
    else:
        console.print("\n[bold yellow]No open jobs found.[/bold yellow]")

def update_job(jobs: list[dict]) -> None:
    console = Console()
    
    job_id = str(prompt_int("Enter job ID to update: "))
    for job in jobs:
        if job["job_id"] == job_id:
            console.print(f"\n[bold green]Editing Job: {job['job_title']}[/bold green]")
            
            new_title = console.input(f"Enter new title (current: {job['job_title']}) [leave empty to keep current]: ").strip()
            if new_title:
                if not new_title.replace(" ", "").isalpha():
                    console.print("[bold red]Only string input is allowed. Kept previous value.[/bold red]")
                else:
                    job['job_title'] = clean_name(new_title)
            
            new_desc = console.input(f"Enter new description (current: {job['job_description']}) [leave empty to keep current]: ").strip()
            if new_desc:
                job['job_description'] = new_descd

            new_location = console.input(f"Enter new location (current: {job['job_location']}) [leave empty to keep current]: ").strip()
            if new_location:
                job['job_location'] = new_location

            new_rate = console.input(f"Enter new rate (current: {job['job_rate']}) [leave empty to keep current]: ").strip()
            if new_rate:
                try:
                    val = float(new_rate)
                    if val < 0.0:
                        console.print("[bold red]Rate must be >= 0. Kept previous value.[/bold red]")
                    else:
                        job['job_rate'] = val
                except ValueError:
                    console.print("[bold red]Invalid rate format. Kept previous value.[/bold red]")

            new_status = console.input(f"Enter new status (current: {job['job_status']}) [leave empty to keep current]: ").strip()
            if new_status:
                job['job_status'] = clean_name(new_status)
                
            console.print("\n[bold green]✔ Job updated successfully![/bold green]")
            return
            
    console.print("\n[bold red]Job not found.[/bold red]")

def delete_job(jobs: list[dict]) -> None:
    console = Console()
    
    job_id = str(prompt_int("Enter job ID to delete: "))
    for i, job in enumerate(jobs):
        if job["job_id"] == job_id:
            removed_job = jobs.pop(i)
            console.print(f"\n[bold green]✔ Job '{removed_job['job_title']}' deleted successfully![/bold green]")
            return
            
    console.print("\n[bold red]Job not found.[/bold red]")

def manage_jobs(jobs: list[dict]) -> None:

    from utils.file_handler import save_data
    console = Console()
    JOBS_FILE = "data/jobs.json"
    
    while True:
        menu_text = Text()
        menu_text.append("1. Post a Job\n", style="green")
        menu_text.append("2. View Open Jobs\n", style="green")
        menu_text.append("3. Update a Job\n", style="green")
        menu_text.append("4. Delete a Job\n", style="green")
        menu_text.append("5. Back to Main Menu", style="yellow")
        
        panel = Panel(menu_text, title="[bold magenta]--- Manage Jobs ---[/bold magenta]", expand=False, border_style="bold green")
        console.print()
        console.print(panel)
        
        choice = console.input("[bold cyan]Choose an option (1-5): [/bold cyan]").strip()
        match choice:
            case "1":
                add_job(jobs)
                save_data(JOBS_FILE, jobs)
                console.print("\n[bold green]✔ Job posted and saved successfully![/bold green]")
            case "2":
                view_open_jobs(jobs)
            case "3":
                update_job(jobs)
                save_data(JOBS_FILE, jobs)
            case "4":
                delete_job(jobs)
                save_data(JOBS_FILE, jobs)
            case "5":
                break
            case _:
                console.print("[bold red] Invalid option. Please choose a number between 1 and 5.[/bold red]")