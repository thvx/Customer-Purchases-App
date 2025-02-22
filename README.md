# Customer Purchases API & Streamlit App

## Overview

This project is a system composed of two main components:

1. **Backend (FastAPI):**
   - Manages customer purchase data in memory.
   - Provides endpoints to:
     - Add a single purchase (`/purchase/`).
     - Bulk upload purchases from a CSV file (`/purchase/bulk/`).
     - Retrieve filtered purchase data (by date and country).
     - Compute KPIs (mean purchases per client, clients per country, and sales forecasting).

2. **Frontend (Streamlit):**
   - A simple user interface with two tabs:
     - **Upload Tab:** Form for single purchase entry and CSV file upload.
     - **Analyse Tab:** Filters (by date and country) and visualization of KPIs from the API.

Both applications are containerized using Docker for easy local execution.

---

## API Endpoints

The following table describes the available endpoints in the FastAPI backend:

| **Endpoint**            | **Method** | **Description**                                                                 | **Parameters**                                                                                   | **Response**                                                                 |
|-------------------------|------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `/purchase/`            | `POST`     | Add a single purchase.                                                          | `customer_name: str`, `country: str`, `purchase_date: date`, `amount: float`                    | The added purchase in JSON format.                                           |
| `/purchase/bulk/`       | `POST`     | Bulk upload purchases from a CSV file.                                          | `file: UploadFile` (CSV file with columns: `customer_name`, `country`, `purchase_date`, `amount`)| JSON response with the number of purchases added.                            |
| `/purchases/`           | `GET`      | Retrieve filtered purchases by date and country.                                | `country: Optional[str]`, `start_date: Optional[date]`, `end_date: Optional[date]`               | List of filtered purchases in JSON format.                                   |
| `/kpis/`                | `GET`      | Compute KPIs (mean purchases per client and clients per country).               | None                                                                                            | JSON response with KPIs: `mean_per_client` and `clients_per_country`.        |
| `/forecast/`            | `GET`      | Generate a sales forecast for the specified number of periods (days).           | `periods: int` (default: 12)                                                                    | JSON response with forecasted sales for each date.                           |

---

## System Architecture

The system follows a client-server architecture:

1. **Backend (FastAPI):**
   - **Models:** Defines the `Purchase` entity.
   - **Schemas** Defines the validation schema (`PurchaseSchema`).
   - **Repository:** Stores data in memory (`PurchaseRepository`).
   - **Services:** Contains business logic (`PurchaseService`), such as KPI calculation and sales forecasting.
   - **Endpoints:** Exposes functionalities through a REST API.

2. **Frontend (Streamlit):**
   - **Domain (Models):** Contains the data models (`Purchase`) used in the application.
   - **Presentation:** Contains the UI components and logic for each tab in the Streamlit app.
   - **Services:** Contains the logic to interact with the API.

3. **Docker:**
   - Each component (FastAPI and Streamlit) runs in a separate container.
   - Docker Compose is used to orchestrate the execution of both containers.

---

## Setup and Running Instructions

### Prerequisites

- Docker installed.
- Git (optional, for cloning the repository).

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/thvx/Customer-Purchases-App.git
   cd customer-purchases-app

2. **Build and run the containers**
   ```bash
   docker-compose up --build

3. **Access the applications**
- FastAPI (Backend): Open your browser and visit http://localhost:8000/docs.
- Streamlit (Frontend): Open your browser and visit http://localhost:8501.

---

## Unit Tests
Unit tests were implemented for key backend functionalities, such as:
- Adding a purchase.
- Loading purchases from a CSV file.
- Calculating KPIs.

### To run the tests:
```bash
cd backend/tests
pytest
