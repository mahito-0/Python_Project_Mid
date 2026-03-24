from __future__ import annotations


def prompt_on_empty(prompt: str) -> str:
    while True:
        s: str = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty. Please try again.")


def clean_name(name: str) -> str:
    return name.strip().title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val
    
def prompt_str(prompt: str) -> str:
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Input cannot be empty. Please try again.")
            continue
        if not raw.replace(" ", "").isalpha():
            print("Only string input is allowed. Please try again.")
            continue
        return raw