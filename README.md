# Cake Tracker Backend

This represents the backend of the Cake Tracker, an application focused on storing employee information and display keeping track of everyone's birthday.

## Implementation

The application is implemented using the FastAPI framework, alongside SQLAlchemy ORM. The database used is SQLite for its ease to set up.

I packaged the application by layers, with the following structure:
- Model: Contains the database models, including the engine and session setup to interact with the database.
- DTOs: Contains the data transfer objects used to interact with the API, represented as Pydantic models, used for validation and serialization, alongside the mappers to convert between the database models and the DTOs.
- Repository: Contains the repository class used to interact with the database, primarily the CRUD operations.
- Service: Contains the service class used to interact with the repository and perform the business logic.
- Controller: Represented by the main.py file, it contains the FastAPI application and the API endpoints.

## Features

- Add a new member to the database. 
  - Required fields: first & last name, birthdate, country, city (with an ID autogenerated as primary key).
  - Ensure that a member is at least 18 years old.
  - Ensure that no two members have the same first and last name, country, and city all at once. (Integrity constraint on the 4 columns)
- Ensure that a member is at least 18 years old.
- Get all members in the database.
- Get all members in the database sorted by closest birthday.

## Requirements

Check the requirements.txt file for the required packages.

## Setup

I generally run the application through the PyCharm IDE, but it can run through the terminal as follows:

1. **Clone the repository**:

   ```bash
   https://github.com/suciubogdansb/CakeTrackerBackend.git
   cd CakeTrackerBackend
   ```

2. **Activate the virtual environment and install packages**:

   ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r ./requirements.txt
   ```

3. **Run the application**:

   ```bash
   fastapi dev main.py
   ```
   
    The application should run on localhost:8000.
