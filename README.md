# Late Show API

A Flask REST API for managing a Late Night TV show. Users can register, log in, view guests and episodes, and manage guest appearances. Uses PostgreSQL as the database and JWT for authentication.

---

## # Setup Instructions

1. Clone the repository
git clone https://github.com/Esther-WI/late_show_api_challenge.git
cd late_show_api_challenge

2. Install dependencies
pipenv install
pipenv shell

3. Create PostgreSQL database
Open your terminal or psql:
CREATE DATABASE late_show_db;

4. Update database URI in server/config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://your_user:your_password@localhost:5432/late_show_db'

# How to Run the App
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
flask run

# Authentication Flow
Register User
Endpoint: POST /register
{
  "username": "user1",
  "password": "password123"
}

Login User
Endpoint: POST /login
{
  "username": "user1",
  "password": "password123"
}

Use JWT Token
Add the following to your headers for protected routes:
Authorization: Bearer <your_token>

# API Routes
Method	Endpoint	Auth Required	Description
POST	/register	No	Register a new user
POST	/login	No	Log in and get a JWT token
GET	/episodes	No	List all episodes
GET	/episodes/<id>	No	Get one episode + appearances
DELETE	/episodes/<id>	Yes	Delete an episode
GET	/guests	No	List all guests
POST	/appearances	Yes	Create an appearance

# Postman Usage Guide
Open Postman

Click "Import"

Select the file: challenge-4-lateshow.postman_collection.json

Use the collection to:

Register a user

Login and copy token

Test protected routes by adding token in Authorization header

# GitHub Repository
GitHub Link: https://github.com/Esther-WI/late_show_api_challenge.git


