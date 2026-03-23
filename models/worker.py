""" 
This module contains functions for processing worker data.
"""
from __future__ import annotations
from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float
   
class Worker:
    def __init__(self, worker_id: str, worker_name: str, worker_skills: list[str], worker_experience: str, worker_location: str, worker_rate: float, worker_status: str) -> None:
        self.worker_id = worker_id
        self.worker_name = worker_name
        self.worker_skills = worker_skills
        self.worker_experience = worker_experience
        self.worker_location = worker_location
        self.worker_rate = worker_rate
        self.worker_status = worker_status

    def to_dict(self):
        return {
            "worker_id": self.worker_id,
            "worker_name": self.worker_name,
            "worker_skills": self.worker_skills,
            "worker_experience": self.worker_experience,
            "worker_location": self.worker_location,
            "worker_rate": self.worker_rate,
            "worker_status": self.worker_status
        }

def add_worker(workers: list[dict]) -> None:
    worker_id = prompt_on_empty("Enter worker ID: ")
    worker_name = clean_name(prompt_on_empty("Enter worker name: "))
    
    skills_input = prompt_on_empty("Enter worker skills (comma-separated): ")
    worker_skills = [s.strip() for s in skills_input.split(",") if s.strip()]
    
    worker_experience = prompt_on_empty("Enter worker experience: ")
    worker_location = prompt_on_empty("Enter worker location: ")
    worker_rate = prompt_float("Enter worker rate: ", min_val=0.0)
    worker_status = prompt_on_empty("Enter worker status: ")

    worker_obj = Worker(worker_id, worker_name, worker_skills, worker_experience, worker_location, worker_rate, worker_status)
    workers.append(worker_obj.to_dict())