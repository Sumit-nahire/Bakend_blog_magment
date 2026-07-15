# 📝 Blog Management System

A full-stack Blog Management System built using **FastAPI**, **React.js**, **PostgreSQL**, and **JWT Authentication**. This application allows users to securely log in and perform complete CRUD operations on blogs.

## 📸 Project Screenshots

### 🔐 Login Page

![Login](./screenshots/login.png)

### 📚 Blog List

![Blog List](./screenshots/blog-list.png)

### ➕ Create Blog

![Create Blog](./screenshots/create-blog.png)

## 🚀 Features

- 🔐 JWT Authentication
- 👤 Secure Login System
- ➕ Create Blog
- 📖 View All Blogs
- ✏️ Update Existing Blog
- ❌ Delete Blog
- 🔍 Search Blogs
- 📄 REST API using FastAPI
- 🗄️ PostgreSQL Database
- 🎨 Responsive React UI
- ⚡ Axios API Integration

## 🛠️ Tech Stack

### Frontend

- React.js
- React Router DOM
- Axios
- CSS

### Backend

- FastAPI
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (Password Hashing)
- Uvicorn

### Database

- PostgreSQL

## 📂 Project Structure

Blog_full_application
│
├── blog-frontend
│ ├── src
│ │ ├── components
│ │ ├── services
│ │ ├── App.jsx
│ │ └── main.jsx
│ └── package.json
│
├── blog-backend
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── auth.py
│ └── requirements.txt
│
└── README.md

## ⚙️ Installation

### Clone Repository

git clone https://github.com/your-username/blog-management-system.git

cd blog-management-system

## Backend Setup

### Create Virtual Environment

python -m venv venv
Activate Environment

Windows
venv\Scripts\activate

Linux / Mac
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Run Backend
uvicorn main:app --reload

Backend runs on
http://127.0.0.1:8000

Swagger Documentation
http://127.0.0.1:8000/docs

## Frontend Setup

Go to frontend folder
cd blog-frontend

Install packages
npm install

Run React
npm run dev

Frontend runs on
http://localhost:5173

## PostgreSQL Configuration

Create a PostgreSQL database named
blogdb

Update your `database.py`
DATABASE_URL = "postgresql://postgres:your_password@localhost/blogdb"

## API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /login      | Login         |
| GET    | /blogs      | Get All Blogs |
| POST   | /blogs      | Create Blog   |
| PUT    | /blogs/{id} | Update Blog   |
| DELETE | /blogs/{id} | Delete Blog   |

## Authentication

This project uses **JWT (JSON Web Token)** authentication.
After login, the access token is stored in Local Storage.
Protected API requests automatically include
Authorization: Bearer <access_token>

## Future Improvements

- User Registration
- Multiple User Roles
- Blog Categories
- Comments
- Likes
- Image Upload
- Rich Text Editor
- Pagination

## Author

**Sumit Nahire**

- GitHub: https://github.com/sumit-nahire
- LinkedIn: https://linkedin.com/in/sumitnahire

## License

This project is developed for learning purposes.
