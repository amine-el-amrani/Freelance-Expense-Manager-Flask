# Freelance Expense Manager

Freelance Expense Manager is a web application that allows freelancers to manage their projects and associated expenses. Managers can approve or reject expenses submitted by freelancers.

## Features

- User registration and login.
- Create, update, and delete projects.
- Add and track expenses by project.
- Managers can approve or reject expenses.
- RESTful API with Flask for backend operations.

## Technologies Used

- **Backend**: Flask, Flask-RESTful, Flask-JWT-Extended, Flask-Migrate
- **Database**: PostgreSQL
- **Testing**: Pytest
- **Containerization**: Docker, Docker Compose

## Installation

### Prerequisites

- Docker
- Docker Compose

### Clone the Repository

```sh
git clone https://github.com/amine-el-amrani/Freelance-Expense-Manager.git
cd Freelance-Expense-Manager
```
### Configure Environment Variables

Create a .env file at the root of the project and add the following environment variables:

```sh
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@db/freelance_expense_manager
JWT_SECRET_KEY=your-jwt-secret-key
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=freelance_expense_manager
```
### Build and Start Containers

```sh
docker-compose up --build
```

## Usage

The API will be available at http://127.0.0.1:5000. You can use tools like Postman or cURL to interact with the API.

## Running Tests
To run the test suite, use the following command:
```sh
docker-compose run web pytest
```
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.