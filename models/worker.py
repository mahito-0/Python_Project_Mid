""" 
This module contains functions for processing worker data.
"""
from __future__ import annotations
from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float

def print_worker_report(workers: list[dict]) -> None:
    print("----- worker Report -----")
    print("\n" + "-" * 50)
    print(f"worker Id: {workers['worker_id']}")
    print(f"worker Name: {workers['worker_name']}")
    print(f"worker Skills: {', '.join(workers['worker_skills'])}")
    print(f"worker Experience: {workers['worker_experience']}")
    print(f"worker Location: {workers['worker_location']}")
    print(f"worker Rate: {workers['worker_rate']}")
    print(f"worker Status: {workers['worker_status']}")

    
def add_worker(workers: list[dict]) -> None:
    sid = prompt_on_empty("Enter worker ID: ")
    name = clean_name(prompt_on_empty("Enter worker name: "))
    
    n = prompt_int("Enter number of subjects: ", min_val=1)
    
    subjects: list[str] = []
    marks: list[float] = []
  
    for i in range(n):
        sub = prompt_on_empty(f"Enter subject {i+1} name: ")
        subjects.append(sub)
        
        marks.append(prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0))
        
    
    total, pct = compute_total_and_percentage(marks)
    grade = garde_from_percentage(pct)
    status = "Pass" if grade != "F" else "Fail"

    worker = {
        "worker_id": worker_id,
        "worker_name": worker_name,
        "worker_skills": worker_skills,
        "worker_experience": worker_experience,
        "worker_location": worker_location,
        "worker_rate": worker_rate,
        "worker_status": worker_status
    }
    
    workers.append(worker)
    