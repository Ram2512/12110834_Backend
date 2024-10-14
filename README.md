# Task Management API

This is a simple Task Management API built using **FastAPI** and **MongoDB**. It allows you to perform basic CRUD operations (Create, Read, Update, Delete) for managing tasks. You can also perform bulk operations like adding multiple tasks and deleting multiple tasks at once.

## Features

- **Create a task**
- **List all tasks**
- **Get a specific task by ID**
- **Update a task by ID**
- **Delete a task by ID**
- **Bulk add tasks**
- **Bulk delete tasks**

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **MongoDB**: A NoSQL database for storing tasks.
- **Motor**: An async Python driver for MongoDB.
- **Pydantic**: Data validation using Python type hints.
- **Uvicorn**: ASGI server for serving FastAPI applications.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.10 or higher
- MongoDB
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/task-manager-api.git
    cd task-manager-api
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use: env\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MongoDB:**

   Make sure MongoDB is running on your local machine. The default MongoDB connection string used in this project is `mongodb://localhost:27017`.

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be accessible at http://127.0.0.1:8000.


