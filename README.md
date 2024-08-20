# Fleet Management System

## Overview

This project is a Fleet Management System designed for a transport company to manage and monitor its vehicle fleet, drivers, and routes. The system integrates with external services to obtain technical data about vehicles and caches the results for performance optimization.

### Key Features

- **Vehicle Management**: Track and manage vehicles, assign them to drivers, and register routes.
- **Driver Management**: Manage driver profiles and assign them to vehicles and routes.
- **Route Management**: Register and manage transport routes.
- **Vehicle Technical Data Monitoring**: Integration with an external API to retrieve and cache vehicle technical data (e.g., fuel levels, brake condition).
- **User Authentication**: Secure user login and registration.
- **Caching with Redis**: Cache external API data to reduce load and improve performance.
- **Session Management**: Use Redis to manage user sessions.
- **API Documentation**: Accessible through Swagger and ReDoc for easy API interaction.

### Technologies Used

- **Django**: For the web application managing vehicles, drivers, and routes.
- **Flask**: As a microservice for fetching vehicle technical data.
- **MySQL**: As the relational database for storing application data.
- **Redis**: For caching and session management.
- **Swagger & ReDoc**: For API documentation.

## API Endpoints

### Django Endpoints

- **/vehicles/**: Manage vehicles (GET, POST, PUT, DELETE).
- **/drivers/**: Manage drivers (GET, POST, PUT, DELETE).
- **/routes/**: Manage routes (GET, POST, PUT, DELETE).
- **/vehicle-status/**: Manage vehicle statuses (GET, POST, PUT, DELETE).
- **/register/**: Register a new user.
- **/auth/login/**: Log in a registered user.
- **/auth/logout/**: Log out a registered user.

### Flask Endpoints

- **/vehicle_status/**: Retrieve vehicle technical data (mocked response).

## Local Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- MySQL
- Redis
- Pipenv or virtualenv (optional, for creating virtual environments)

### MySQL Configuration

1. Create a new MySQL database named `fleet_db`:

    ```sql
    CREATE DATABASE fleet_db;
    ```

2. Update the Django `settings.py` file with your MySQL database credentials.

### Redis Configuration

Ensure that Redis is running on your local machine. The default configuration should work fine.

### Project Setup

1. **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment** and activate it (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **You can load test data into the database**:

    ```bash
    python manage.py loaddata fixtures.json
    ```

6. **Run the Django server**:

    ```bash
    python manage.py runserver
    ```

7. **Run the Flask microservice**:

    ```bash
    cd flask_microservice  # Navigate to the Flask service directory
    flask run
    ```

### Authentication

Before using the system, you need to **register** and then **log in** to access the dashboard and other functionalities.

### Session Management with Redis

User sessions are managed using Redis to improve performance and scalability.

### API Documentation

You can explore the API using Swagger and ReDoc:

- Swagger: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

### Testing

The project includes basic unit tests to verify the correctness of key functionalities.

- To run tests, use:

    ```bash
    python manage.py test
    ```

### Flask Microservice Details

The Flask microservice fetches and mocks data from an external API, simulating the retrieval of vehicle technical data (like fuel levels and brake conditions). The results are cached in Redis for optimized performance.

## Additional Information

- The Flask service assigns the API data to the respective Django models, integrating the external data into the main application.
- The project includes fixtures (`fixtures.json`) with test data for easy setup.
