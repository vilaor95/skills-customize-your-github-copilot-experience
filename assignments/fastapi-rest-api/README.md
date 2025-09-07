# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By completing this assignment, you will gain hands-on experience with API endpoints, request/response handling, and baBuilding REST APIs with FastAPI frameworksic data validation.

## 📝 Tasks

### 🛠️	Basic FastAPI Setup

#### Description
Set up a simple FastAPI application and run it locally.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main application file (e.g., `main.py`)
- Define a root endpoint (`/`) that returns a welcome message
- Run the server locally and test the root endpoint

### 🛠️	CRUD API for a Resource

#### Description
Build a REST API to manage a simple resource (e.g., books, users, or tasks) with full CRUD (Create, Read, Update, Delete) functionality.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource
- Implement endpoints for:
  - Listing all resources (GET)
  - Creating a new resource (POST)
  - Retrieving a resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Use in-memory storage (e.g., a Python list or dictionary)
- Return appropriate status codes and error messages

### 🛠️	API Documentation & Validation

#### Description
Leverage FastAPI's automatic documentation and data validation features.

#### Requirements
Completed program should:

- Use Pydantic models for request and response validation
- Access the interactive API docs at `/docs`
- Add example data and field descriptions to the models
- Handle invalid input gracefully with clear error messages
