# Shadino
This is a small shop project and a store that I have designed with Django framework and Rest-framework API.

##### This store is completely Persianized :)

### requirements install
```bash
  pip install requirements.txt
```

### database config
Please go to the following path and configure the database according to your needs:

### core/settings:
```python
  DATABASES = {
      'default': {
          'ENGINE': 'your-backend-database',
          'NAME': 'your-database-name',
          'USER': 'your-username',
          'PASSWORD': 'your-password',
          'HOST': 'your-how',
          'PORT': 'your-port',
      }
  }
```

### aplly model migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

### Run server
```bash
  python manage.py runserver
```
