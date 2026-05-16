# Order Management API

A Django REST Framework based Order Management API using JWT Authentication and Role-Based Access Control.

---

# Project Overview

This project is developed using:

- Python
- Django
- Django REST Framework
- JWT Authentication

The system contains two types of users:

- Admin
- Customer

Customers can:

- Register
- Login
- View products
- Create orders
- View their own orders

Admins can:

- Manage products
- View all orders
- Update order status

---

# Features

## Authentication

- JWT Authentication
- Access Token
- Refresh Token

## Role-Based Access

### Admin
- Create products
- Update products
- Delete products
- View all orders
- Update order status

### Customer
- Register account
- Login
- Create orders
- View own orders

---

# Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite

---

# Project Structure

```bash
order_management/
│
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│
├── order_management/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── README.md
````

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Anjanajoshy717/Order_Management_Project.git

cd order_management
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```
---

## 3. Install Dependencies

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install pillow
```

---

## 4. Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 5. Create Admin User

```bash
python manage.py shell
```

```python
from api.models import User

User.objects.create_user(
    username='admin',
    password='admin123',
    role='admin'
)

exit()
```

---

## 6. Run Server

```bash
python manage.py runserver
```

Server URL:

```bash
http://127.0.0.1:8000/
```

---

# Authentication

JWT Authentication is used.

After login, add token in request headers:

```bash
Authorization: Bearer ACCESS_TOKEN
```

---

# API Endpoints

# Register Customer

## Endpoint

```bash
POST /api/register/
```

## Request

```json
{
    "username": "anjana",
    "email": "anjana@gmail.com",
    "password": "Anjana@123"
}
```

## Response

```json
{
    "id": 2,
    "username": "anjana",
    "email": "anjana@gmail.com"
}
```

---

# Login

## Endpoint

```bash
POST /api/login/
```

## Request

```json
{
    "username": "anjana",
    "password": "Anjana@123"
}
```

## Response

```json
{
    "refresh": "jwt_refresh_token",
    "access": "jwt_access_token"
}
```

---

# Create Product (Admin Only)

## Endpoint

```bash
POST /api/products/
```

## Headers

```bash
Authorization: Bearer ADMIN_ACCESS_TOKEN
```

## Request

```json
{
    "name": "Laptop",
    "description": "HP Laptop",
    "price": 50000,
    "stock": 5
}
```

---

# List Products

## Endpoint

```bash
GET /api/products/
```

---

# Create Order

## Endpoint

```bash
POST /api/orders/create/
```

## Headers

```bash
Authorization: Bearer CUSTOMER_ACCESS_TOKEN
```

## Request

```json
{
    "items": [
        {
            "product": 1,
            "quantity": 2
        },
        {
            "product": 2,
            "quantity": 1
        }
    ]
}
```

## Response

```json
{
    "id": 1,
    "customer": 2,
    "status": "pending",
    "created_at": "2026-05-15T10:00:00Z",
    "items": [
        {
            "id": 1,
            "product": 1,
            "product_name": "Laptop",
            "quantity": 2,
            "price": "50000.00",
            "subtotal": 100000.00
        }
    ],
    "total_amount": 100000.00
}
```

---

# View Orders

## Endpoint

```bash
GET /api/orders/
```

Customer can view only their own orders.

Admin can view all orders.

---

# Update Order Status (Admin Only)

## Endpoint

```bash
PATCH /api/orders/1/
```

## Request

```json
{
    "status": "completed"
}
```

---

# Business Logic Implemented

* Nested order creation
* JWT authentication
* Role-based access control
* Total amount calculation
* Order item subtotal calculation
* Product price stored in OrderItem
* Customers restricted to own orders

---

# Evaluation Criteria Covered

- Correct model relationships
- REST API structure
- JWT Authentication
- Role-based permissions
- Nested order creation
- Total amount calculation
- Clean code structure
- API documentation

---

# Author

Anjana Joshy

```
```
