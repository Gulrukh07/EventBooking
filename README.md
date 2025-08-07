# 🎟️ EventBooking API

EventBooking is a Django-based REST API that allows users to view and register for events. Organizers can create events, and authenticated users can register for them. The API also includes Swagger documentation for easy testing and integration.

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Gulrukh07/EventBooking.git
cd EventBooking
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your settings (e.g., database config, secret key).  
Example:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)


## ⚙️ Tech Stack

| Category        | Technology                   |
|----------------|------------------------------|
| Language        | Python 3.12                  |
| Framework       | Django, Django REST Framework |
| Auth            | Token / JWT (djoser / drf-simplejwt) |
| Documentation   | Swagger (drf-yasg)           |
| Database        | SQLite (default), PostgreSQL compatible |

---

## 📚 API Documentation (Swagger)

The project uses **Swagger UI** for interactive API exploration. After running the server, visit:

👉 [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

### Sample Endpoints:

| Method | Endpoint                | Description               | Auth Required |
|--------|-------------------------|---------------------------|----------|
| GET    | /api/events/            | List all events           | ❌ No     |
| POST   | /api/events/            | Create a new event        | ✅ Yes    |
| GET    | /api/events/<id>/       | List user's event         | ✅ Yes    |
| POST   | /api/registrations/     | Register for an event     | ✅ Yes    |
| GET    | /api/registrations/<id> | lists user's registration | ✅ Yes    |
| POST   | /api/auth/token/        | Get auth token (login)    | ❌ No     |

---

## 👤 User Roles

- **Admin/Organizer** – Can create and manage events
- **Authenticated User** – Can register for events
- **Anonymous** – Can view events, but cannot register

---

## 📦 Folder Structure

```
EventBooking/
├── event/              # App containing event logic
├── registration/       # App for event registrations
├── users/              # Custom user model & auth logic
├── manage.py
├── requirements.txt
└── ...
```


## 🙋‍♀️ Author

**Gulrukh Khayrullaeva**  
🔗 [LinkedIn](https://www.linkedin.com/in/gulrukh-khayrullaeva-7262a9295/) | 📧 [Email](mailto:gulrukhkhalilovna@gmail.com)