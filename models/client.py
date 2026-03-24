""" 
This module contains functions for processing client data.
"""
from __future__ import annotations
from utils.utils import prompt_on_empty, clean_name, prompt_int, prompt_float, prompt_str
   
class Client:
    def __init__(self, client_id: str, client_name: str, company_name: str, company_location: str, company_rate: float, company_status: str) -> None:
        self.client_id = client_id
        self.client_name = client_name
        self.company_name = company_name
        self.company_location = company_location
        self.company_rate = company_rate
        self.company_status = company_status

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "client_name": self.client_name,
            "company_name": self.company_name,
            "company_location": self.company_location,
            "company_rate": self.company_rate,
            "company_status": self.company_status
        }

def add_client(clients: list[dict]) -> None:
    client_id = str(prompt_int("Enter client ID: "))
    client_name = clean_name(prompt_str("Enter client name: "))
    
    company_name = prompt_on_empty("Enter company name: ")
    company_location = prompt_on_empty("Enter company location: ")
    company_rate = prompt_float("Enter company rate: ", min_val=0.0)
    company_status = prompt_on_empty("Enter company status: ")

    client_obj = Client(client_id, client_name, company_name, company_location, company_rate, company_status)
    clients.append(client_obj.to_dict())