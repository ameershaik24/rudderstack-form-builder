# Rudderstack form builder

## Backend
- Written in Django (4.1.7) and Python (3.9.13), using Django REST framework
- To run the backend service
  ```
  python -m venv form-builder-venv
  source form-builder-venv/bin/activate

  cd backend
  pip install -r requirements.txt

  python manage.py runserver
  ```

## Frontend
- Written in Angular 8, using Bootstrap
- To run the fronend service
  ```
  cd frontend
  npm install

  ng serve --open
  ```

---
A postman collection is included containing sample API examples.

