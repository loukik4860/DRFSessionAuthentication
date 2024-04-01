# DRFSessionAuthentication
The Django Rest Framework (DRF) Session Authentication Repository is a component designed to handle authentication within Django Rest Framework APIs using session-based authentication. This repository serves as a central hub for managing user sessions, verifying their authenticity, and granting access to protected resources.

### **Installation**

#### 1. Clone the repository:

    git clone https://github.com/your_username/your_project.git

#### Install dependencies:

    pip install -r requirements.txt

#### Set up the database:

    python manage.py migrate

#### Create a superuser (optional):

    python manage.py createsuperuser

#### Start the development server:

    python manage.py runserver

## Usage


1. Register a new user by making a POST request to          
            /api/account/registration/.
2. Activate the user's account by visiting the activation link sent to the registered email.
3. Confirm the activation by making a POST request to 
         /api/account/activate/ with the activation token.
=======
1. Register a new user by making a POST request to /api/account/registration/.
2. Activate the user's account by visiting the activation link sent to the registered email.
3. Confirm the activation by making a POST request to /api/account/activate/ with the activation token.

4. Enjoy using the application!

## API Endpoints


*    / api / account / registration /                          :- _Register a new user._
*   / api /account /activate / <<str:uid>> / <<str:token>> /   :- Activate user's account.
*   / api / account / active /                                 : Confirm user's activation.
=======
* /api/account/registration/                         : Register a new user.
* /api/account/activate/<<str:uid>>/<<str:token>>/   :- Activate user's account.
* /api/account/active/                               : Confirm user's activation.


## Configuration
* Ensure that your email settings in settings.py are correctly configured for sending activation emails.
* Customize other settings as needed for your project.


## Credits

This project was created by loukik.

