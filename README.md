# 🎟️ Event Registration System

A Django-based web application where users can **view events**, **see available tickets**, and **register** for events after **signing up or logging in**.

## 🔑 Features

- 👤 User Authentication (Login / Signup / Logout)
- 📅 Event Listings with Date, Time, and Description
- 🎫 Real-time Ticket Availability
- 📝 User Registration for Events
- 🛡️ Admin Panel to Manage Events and Registrations

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS (optional: Bootstrap or JS)  
- **Database:** SQLite (easily switchable to PostgreSQL)  
- **Auth System:** Django's built-in authentication

## 🚀 Getting Started

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/event-registration-system.git
cd event-registration-system

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
