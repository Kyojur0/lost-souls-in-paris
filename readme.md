# Django Ecommerce Application

Code from [Advance Django Course | E-Commerce Shoping Cart | Paytm Integration & 100%Authentication](https://www.youtube.com/watch?v=7VEveJz7hdM)

If you open each sub-folder they have their own Readme.md to better explain the code :3

## Tech Stack

**Client:** HTML , CSS , Bootstrap , JS

**Server:** Django (Pyhton)

Python Version: 3.11.3

Django Version: 5.0

## Run Locally

Clone the project

```bash
  git clone https://github.com/Kyojur0/lost-souls-in-paris.git
```

Go to the project directory

```bash
  cd lost-souls-in-paris
```

Create Virtual Enviroment in Python (Windows)

```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
```

Install dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

Delete any previous pychache folders in subdirectories.

Start the server using 2 terminals

1st run follownig this will give you Hot-Reload

```bash
python ./manage.py livereload
```

Then in another terminal use following command to run the code

```bash
python ./manage.py runserver
```

Go to http://localhost:8000/ to access the ecommerce site. While
http://localhost:8000/admin to access the admin panel the password for admin is

---

Username: admin

Password: admin

---

## Documentation

What this project has ?

1. Complete Authentication System with

- **Login:**

  - Users can securely log in to their accounts.

- **Logout:**

  - Users can log out of their accounts to terminate their authenticated sessions.

- **Account Activation with Token:**

  - New user accounts require email verification for activation.
  - Activation tokens are sent via email to the user.
  - Users activate their accounts by clicking on the activation link with the token.

- **Reset Password:**
  - Users can initiate a password reset by providing their email address.
  - Password reset tokens are sent via email.
  - Users can reset their passwords by clicking on the reset password link with the token.

## Main Front Face

- **Dashboard:**

  - Users are greeted with a user-friendly dashboard upon logging in.
  - Displays personalized information and quick links.

- **Profile Page:**

  - Users can view and edit their profiles.
  - Includes profile picture, personal details, and account settings.

- **User Interface:**
  - The application features a clean and responsive user interface.
  - Mobile-friendly design for a seamless experience on various devices.

## Payment Integration

**Note:** _I skipped :)_
