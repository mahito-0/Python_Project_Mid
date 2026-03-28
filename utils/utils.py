from __future__ import annotations
from rich.console import Console

console = Console()

def prompt_on_empty(prompt: str) -> str:
    while True:
        s: str = console.input(f"[bold cyan]{prompt}[/bold cyan]").strip()
        if s:
            return s
        console.print("[bold red] Input cannot be empty. Please try again.[/bold red]")


def clean_name(name: str) -> str:
    return name.strip().title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = console.input(f"[bold cyan]{prompt}[/bold cyan]").strip()
        try:
            val = int(raw)
        except ValueError:
            console.print("[bold red] Invalid input. Please enter a valid integer.[/bold red]")
            continue
        if max_val is not None and val > max_val:
            console.print(f"[bold red] Input must be less than or equal to {max_val}.[/bold red]")
            continue
        if val < min_val:
            console.print(f"[bold red] Input must be greater than or equal to {min_val}.[/bold red]")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = console.input(f"[bold cyan]{prompt}[/bold cyan]").strip()
        try:
            val = float(raw)
        except ValueError:
            console.print("[bold red] Invalid input. Please enter a valid number.[/bold red]")
            continue
        if max_val is not None and val > max_val:
            console.print(f"[bold red] Input must be less than or equal to {max_val}.[/bold red]")
            continue
        if val < min_val:
            console.print(f"[bold red] Input must be greater than or equal to {min_val}.[/bold red]")
            continue
        return val
    
def prompt_str(prompt: str) -> str:
    while True:
        raw = console.input(f"[bold cyan]{prompt}[/bold cyan]").strip()
        if not raw:
            console.print("[bold red] Input cannot be empty. Please try again.[/bold red]")
            continue
        if not raw.replace(" ", "").isalpha():
            console.print("[bold red] Only string input is allowed. Please try again.[/bold red]")
            continue
        return raw