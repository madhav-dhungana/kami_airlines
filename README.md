# KAMI WorkForce Assessment for Kami Airlines Project

This project is part of assessment for a Django-based RESTful API for KAMI Airlines.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

Make sure you have Python and Django installed on your machine.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/madhav-dhungana/kami_airlines.git
    ```

2. Change into the project directory:

    ```bash
    cd kami-airlines
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

4. Make migrations:

    ```bash
    python manage.py makemigrations
    ```

5. Migrate the database:

    ```bash
    python manage.py migrate
    ```

### Create Superuser

6. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up the superuser account.

### Running the Server

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The server will be running at `http://localhost:8000/`.

### Access API Endpoints

API endpoints can be accessed through the browser or tools like [Postman](https://www.postman.com/).

- Example API endpoint: `http://localhost:8000/api/airplanes/` # for list view
- Example API endpoint: `http://localhost:8000/api/airplanes/1` # for detail view

### Access Admin Interface

8. Access the admin interface:

    Open your browser and go to `http://localhost:8000/admin/`. Log in with the superuser credentials created earlier.

## Additional Notes

- Ensure that the virtual environment is activated before running any commands.

- Add `airplanes` and `rest_framework`, in the `settings.py` file installed apps global variable.

## Testing and Test Coverage

To run tests and generate a test coverage report, follow these steps:

### Running Tests

9. Run tests:

    ```bash
    python manage.py test
    ```

    This command will execute all tests in the project.

### Test Coverage

10. Generate a test coverage report:

    ```bash
    coverage run --source='.' manage.py test
    ```

11. View the coverage report:

    ```bash
    coverage report
    ```

    This command will display a text-based coverage report in the terminal.

12. Generate an HTML coverage report:

    ```bash
    coverage html
    ```

    Open the generated HTML report located in the `htmlcov` directory:

    ```bash
    open htmlcov/index.html
    ```

    This will open the coverage report in your default web browser.


