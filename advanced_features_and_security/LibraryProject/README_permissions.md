# Django Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created with management command:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → all permissions

## Usage
- Run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
