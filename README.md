# Supermarket Checkout

This project implements a supermarket checkout process using Python3 and OOP principles.

## Setup

1. Clone the repository.
2. Navigate to the project directory.

## How to Run

### Without Docker

1. Ensure Python 3 is installed.
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the main script:
    ```sh
    python main.py
    ```

### With Docker

1. Build the Docker image:
    ```sh
    docker-compose build
    ```
2. Run the Docker container:
    ```sh
    docker-compose up
    ```

## Tests

To run the tests:
```sh
pytest tests/test_checkout.py
