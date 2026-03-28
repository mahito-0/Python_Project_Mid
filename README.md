# Shobkaaj - CLI Freelance & Job Platform

## 📖 Overview
Shobkaaj is a Python-based Command-Line Interface (CLI) application that connects workers and clients. It acts as a lightweight platform where clients can post jobs, and workers can browse open jobs and apply for them. The platform maintains persistent data using JSON files.

## ✨ Features and Functionalities
The application provides a fully interactive CLI menu with the following capabilities:
1. **Register as Worker:** Allows users to create a worker profile (ID, Name, Skills, Experience, Location, Rate, Status).
2. **Register as Client:** Allows users to create a client/company profile (ID, Name, Company Name, Location, Rate, Status).
3. **Post a Job:** Clients can post new jobs with titles, descriptions, locations, and rates. The job defaults to an "Open" status.
4. **View Open Jobs:** Workers can browse through all jobs currently marked as "Open".
5. **Apply to a Job:** Workers can submit an application to a specific job using their Worker ID and the Job ID. 
6. **View Applications:** Allows users to list all job applications that have been submitted.
7. **Persistent Storage:** All data (workers, clients, jobs, applications) is saved safely into the `data/` directory as JSON files, ensuring that no information is lost between sessions.

## 🛠️ Prerequisites
- **Python:** Version **3.10** or higher is strictly required due to the use of structural pattern matching (`match...case` statements) in the main menu loop.

## 🚀 How to Run

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone <repository_url>
   cd Python_Project_Mid
   ```

2. **(Optional) Install Dependencies:**
   If you are running in a fresh environment, install the prerequisites from the `requirements.txt` file (though no external dependencies are strictly needed for the core built-in functionalities):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Execute the `main.py` script directly from your terminal:
   ```bash
   python main.py
   ```

4. **Using the Platform:**
   Once running, you will be greeted by the Shobkaaj Platform menu. Type the number corresponding to the action you wish to perform and press Enter. Follow the interactive prompts for data entry.
   ```text
   === Shobkaaj Platform ===
   1. Register as Worker
   2. Register as Client
   3. Post a Job
   4. View Open Jobs
   5. Apply to a Job
   6. View Applications
   7. Exit
   ```

## 📂 Project Structure
- `main.py`: The entry point of the CLI application containing the main menu logic.
- `models/`: Contains the core data models and business logic (`client.py`, `worker.py`, `job.py`, `application.py`).
- `utils/`: Contains utility functions for data validation/input and data persistence (`utils.py`, `file_handler.py`).
- `data/`: The directory where all user and job JSON data files are persistently stored.
