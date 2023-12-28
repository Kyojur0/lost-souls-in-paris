# Documentation

```plaintext
myproject/
├── manage.py
├── django_app/
    ├── __init__.py 
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## settings.py

The `settings.py` file in your Django project is a central configuration file that governs various aspects of your application. Below are key configurations managed by this file:

1. **Database Configurations:**
   - Defines database-related settings such as database engine, name, user, and password.

2. **Mail Server Configurations:**
   - Specifies settings for sending emails, including SMTP server details.

3. **Static File Path Configurations:**
   - `STATIC_URL` defines the base URL for static files.
   - `STATICFILES_DIRS` lists additional directories to look for static files.

4. **Media File Path Configurations:**
   - `MEDIA_URL` sets the base URL for media files.
   - `MEDIA_ROOT` specifies the directory to store uploaded media files.

5. **Adding/Removing Django Apps:**
   - `INSTALLED_APPS` lists the Django apps installed in your project.
   - To add a new app, append its name to the `INSTALLED_APPS` list.

   ```python
   INSTALLED_APPS = [
       ...  # old default apps
       '<new_app>',
   ]
   ```

6. **Root URL Configuration:**
   - `ROOT_URLCONF` directs Django to the main app's URL configuration.

   ```python
   ROOT_URLCONF = 'django_app.urls'
   ```

7. **Template Configuration:**
   - `TEMPLATES` lists the template engines and their configurations.
   - Set the `DIRS` option to specify additional template directories.

8. **Static and Media File Directories/URLs:**
   - `STATICFILES_DIRS` and `MEDIA_ROOT` define the directories for static and media files.

   ```python
   STATICFILES_DIRS = [BASE_DIR / "static"]
   MEDIA_ROOT = BASE_DIR / "media"
   ```

   - `STATIC_URL` and `MEDIA_URL` set the base URLs for static and media files.

   ```python
   STATIC_URL = '/static/'
   MEDIA_URL = '/media/'
   ```

Note: The `BASE_DIR` variable is defined as `Path(__file__).resolve().parent.parent`, indicating the base directory for Django to reference.

Understanding the distinction between `STATIC` and `MEDIA` configurations is crucial. `STATIC` refers to static assets like CSS and JavaScript, while `MEDIA` pertains to user-uploaded content, such as images or videos. Both have separate configurations to ensure appropriate file handling.
