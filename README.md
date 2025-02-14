# Customer Purchases API & Streamlit App

## Overview

Build a system with two main components:

1. **Backend (FastAPI)**  
   - Manage customer purchase data in-memory.
   - Endpoints to:
     - Add a single purchase (`/purchase/`).
     - Bulk upload purchases from a CSV (`/purchase/bulk/`).
     - Retrieve filtered purchase data (by date and country).
     - Compute KPIs (mean purchases per client, clients per country, and optionally, forecast sales).

2. **Frontend (Streamlit)**  
   - Create a simple UI with two tabs:
     - **Upload Tab**: Form for a single purchase entry and CSV file upload.
     - **Analyse Tab**: Filter (by date and country) and display KPIs from the API.

3. **Dockerization**  
   - Containerize both the FastAPI and Streamlit applications.
   - Provide clear instructions to run them locally.

## Requirements

- Use the provided repository as your starting point:
  - **FastAPI code:** located at `fastapi/main.py`
  - **Sample CSV file:** `sample_purchase.csv` (CSV format only)
- Data should be stored in-memory.
- Document your work in a custom README (this file should be replaced with your own version).
- Use Git with regular, small commits (feature branches recommended).
- Write unit tests for key backend functionality.
- **Deadline:** Complete and submit your GitHub repository link within one week.

## Evaluation Criteria

- **Code Quality:** Clean, modular, and well-commented code.
- **Documentation:** A clear README explaining:
  - The system architecture.
  - Setup and running instructions.
  - Design decisions and any trade-offs.
- **Testing:** Adequate unit tests for backend endpoints.
- **Version Control:** Frequent commits and proper branching.
- **Dockerization:** Successful containerization with clear local run instructions.

## Getting Started

1. **Clone the Repository:**  
   `git clone https://github.com/merck-test/software-developer-test.git`

2. **Backend:**  
   - Review and enhance the FastAPI code in `fastapi/main.py`.

3. **Frontend:**  
   - Build a Streamlit app to interact with the FastAPI endpoints.

4. **Docker:**  
   - Create Dockerfiles for both the FastAPI and Streamlit applications.
   - Provide instructions to build and run the containers.

5. **Testing & Documentation:**  
   - Write unit tests for backend functionality.
   - Update this README with your explanations and setup instructions.

## Submission

Submit your GitHub repository link once completed. Ensure your repo includes:
- Your updated README.
- Enhanced FastAPI and Streamlit code.
- Dockerfiles and clear run instructions.
- Unit tests for the backend.

Good luck and happy coding!