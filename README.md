# 🎉 EventFlow - Event Registration & Management System

EventFlow is a modern event registration and management web application built with **Django**. It allows users to create, explore, register for, and manage events through a clean and responsive interface.

---

## ✨ Features

### Authentication
- User Registration
- User Login
- Secure Logout
- Profile Management

### Event Management
- Create Events
- Edit Events
- Delete Events
- Upload Event Images
- Manage Your Events

### Event Discovery
- Browse Available Events
- View Event Details
- Save Events
- Register for Events
- Cancel Registration

### Dashboard
- Event Statistics
- Upcoming Events
- Active Registrations
- Quick Navigation

### User Features
- Saved Events
- Registered Events
- Profile Page
- Settings Page

---

## 🛠 Tech Stack

### Backend
- Django 5
- Django ORM

### Database
- SQLite (Development)
- PostgreSQL (Production)

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Deployment
- Gunicorn
- WhiteNoise
- Render / Railway
- PostgreSQL

---

## 📂 Project Structure

```
Event Registration/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
├── events/
├── registrations/
│
├── templates/
├── static/
├── media/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/ujjaval-21/eventflow.git

cd eventflow
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## 📌 Future Improvements

- Email Verification
- Password Reset
- Event Categories
- Search & Filters
- Notifications
- QR Code Event Tickets
- Payment Gateway
- Admin Analytics
- REST API
- Mobile Responsive Improvements
- Dark Mode

---


## 👨‍💻 Author

**Ujjaval Yadav**

GitHub: https://github.com/ujjaval-21

LinkedIn: www.linkedin.com/in/ujjavalyadav21

---

## 📄 License

This project is developed for learning, portfolio, and demonstration purposes.
