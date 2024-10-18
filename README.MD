Banking System API Documentation
================================

Table of Contents
-----------------

1.  [Project Overview](#project-overview)
2.  [Project Structure](#project-structure)
3.  [Setup Instructions](#setup-instructions)
4.  [API Endpoints](#api-endpoints)
    -   [User Authentication](#user-authentication)
    -   [Accounts](#accounts)
    -   [Transactions](#transactions)
5.  [Models](#models)
6.  [Usage](#usage)
7.  [Contributing](#contributing)
8.  [License](#license)

Project Overview
----------------

This is a banking system API built with Django and Django REST Framework. The API allows users to manage bank accounts, perform transactions, and maintain user authentication using JWT.

Project Structure
-----------------


```bash
banking_system/
├── accounts/           # App for user accounts and authentication
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── bank/               # App for banking transactions and accounts
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── banking_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Setup Instructions
------------------

1.  **Clone the repository:**

    
    ```bash
    git clone https://github.com/Ahmed3atef/Banking-System-API.git
    cd banking_system
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install the required packages:**

    

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    `

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

API Endpoints
-------------

### User Authentication

-   **Register User**

    -   **Endpoint:** `POST /api/accounts/register/`
    -   **Request Body:**

        ```json
        {
          "username": "user1",
          "password": "password123"
        }
        ```

-   **Login User**

    -   **Endpoint:** `POST /api/accounts/login/`
    -   **Request Body:**

        ```json
        {
          "username": "user1",
          "password": "password123"
        }
        ```

-   **Logout User**

    -   **Endpoint:** `POST /api/accounts/logout/`
    -   **Headers:**
        -   `Authorization: JWT <token>`

### Accounts

-   **Create Account**

    -   **Endpoint:** `POST /api/bank/accounts/`
    -   **Request Body:**

        ```json
        {
          "account_number": "550e8400-e29b-41d4-a716-446655440000",
          "balance": 1000.00
        }
        ```

-   **Retrieve Account**

    -   **Endpoint:** `GET /api/bank/accounts/<account_number>/`
    -   **Headers:**
        -   `Authorization: JWT <token>`

### Transactions

-   **Create Transaction**

    -   **Endpoint:** `POST /api/bank/transactions/`
    -   **Request Body:**

        ```json
        {
          "account_number": "550e8400-e29b-41d4-a716-446655440000",
          "amount": 200.00,
          "transaction_type": "deposit"
        }
        ```

-   **Retrieve Transactions**

    -   **Endpoint:** `GET /api/bank/transactions/`
    -   **Headers:**
        -   `Authorization: JWT <token>`

Models
------

### CustomUser

-   `username`: CharField
-   `password`: CharField

### BankAccount

-   `account_number`: UUIDField (Primary Key)
-   `balance`: DecimalField

### Transaction

-   `account_number`: UUIDField (Foreign Key to BankAccount)
-   `amount`: DecimalField
-   `transaction_type`: CharField (Choices: deposit, withdrawal)
-   `timestamp`: DateTimeField (auto_now_add=True)

Usage
-----

1.  Register a new user.
2.  Login to get a JWT token.
3.  Create a bank account using the token.
4.  Perform transactions (deposit/withdrawal) using the account number.

Contributing
------------

If you would like to contribute to this project, please fork the repository and submit a pull request.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.