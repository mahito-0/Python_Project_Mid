import json
import os
from typing import Any

from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float, prompt_str

class Job:
    def _init_(self, job_id: str, job_title: str, job_description: str, job_location: str, job_rate: float, job_status: str) -> None:
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
    from rich.console import Console
    from rich.table import Table
    
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