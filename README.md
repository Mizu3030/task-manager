taskmanager/                  ← Main project folder
│
├── taskmanager/              ← Django project settings folder
│   ├── __init__.py           ← Marks this folder as a Python package
│   ├── settings.py           ← Django settings (add LOGIN_URL, etc.)
│   ├── urls.py               ← Project-level URL routing (includes app URLs)
│   ├── wsgi.py / asgi.py     ← Web server interface files
│
├── tasks/                    ← Django app for task management
│   ├── __init__.py           ← Marks this folder as a Python package
│   ├── admin.py              ← Admin panel configuration for Task model
│   ├── apps.py               ← App configuration
│   ├── models.py             ← Database models (e.g., Task)
│   ├── forms.py              ← Django forms for task input
│   ├── views.py              ← View functions (login, task list, etc.)
│   ├── urls.py               ← App-level URL routing (login, register, add task...)
│   ├── migrations/           ← Database migration files
│
├── templates/                ← HTML templates folder
│   ├── base.html             ← Base layout shared across pages
│   ├── users/                ← Templates for user authentication
│   │   ├── login.html        ← Login page
│   │   └── register.html     ← Registration page
│   └── tasks/                ← Templates for task operations
│       ├── task_list.html    ← Task list view
│       ├── add_task.html     ← Add new task form
│       ├── edit_task.html    ← Edit task form
│       └── delete_task.html  ← Delete confirmation page
│
├── db.sqlite3                ← Default SQLite database
├── manage.py                 ← Django command-line utility
