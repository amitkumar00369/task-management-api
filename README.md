Task Management API

This is a Django-based API for managing tasks, users, and task assignments. It allows you to create users, tasks, assign tasks to users, and retrieve tasks assigned to users.

Technologies Used:
- Django
- Django REST Framework
- By Default DbSqlite3

Installation Guide:

1. Clone the repository:
   git clone https://github.com/your-username/task-management-api.git
   cd task-management-api

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set up the database:
   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:
   python manage.py runserver

   Your app will be available at http://127.0.0.1:8000/.

API Endpoints:

1. Create a User
   URL: /createUser
   Method: POST
   Request Body:
     {
       "name": "John Doe",
       "email": "johndoe@example.com",
       "mobile": "1234567890"
     }
   Response:
     {
       "message": "User Created",
       "data": {
         "id": 1,
         "name": "John Doe",
         "email": "johndoe@example.com",
         "mobile": "1234567890"
       },
       "status": 201
     }

2. Create a Task
   URL: /tasks/create
   Method: POST
   Request Body:
     {
       "name": "Complete Documentation",
       "description": "Complete the API documentation for the project.",
       "task_type": "Documentation"
     }
   Response:
     {
       "message": "Task Created",
       "data": {
         "id": 1,
         "name": "Complete Documentation",
         "description": "Complete the API documentation for the project.",
         "task_type": "Documentation",
         "created_at": "2025-03-25T00:00:00Z",
         "status": "pending",
         "users": []
       },
       "status": 201
     }

3. Assign a Task to Users
   URL: /tasks/assign
   Method: POST
   Request Body:
     {
       "taskId": 1,
       "userIds": [1, 2]
     }
   Response:
     {
       "message": "Task assigned successfully",
       "status": 201
     }

4. View Tasks Assigned to a User
   URL: /usersViewTask/{userId}/tasks
   Method: GET
   Response:
     {
       "message": "User Assigned Tasks",
       "data": [
         {
           "id": 1,
           "name": "Complete Documentation",
           "description": "Complete the API documentation for the project.",
           "created_at": "2025-03-25T00:00:00Z",
           "task_type": "Documentation",
           "status": "pending",
           "users": [
             {
               "id": 1,
               "name": "John Doe",
               "email": "johndoe@example.com",
               "mobile": "1234567890"
             }
           ]
         }
       ],
       "status": 200
     }

Configuration:

Database Configuration
By default, the app uses SQLite. To configure a different database (e.g., PostgreSQL), update the DATABASES setting in settings.py as follows:

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Running Tests:
To run tests for the application, use the following command:
   python manage.py test

License:
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments:
- Django Framework
- Django REST Framework
- DbSqlite3
If you encounter any issues or have questions, please feel free to raise an issue or contact the repository maintainer.
