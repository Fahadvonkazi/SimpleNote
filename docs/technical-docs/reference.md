---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
Fahad von Kazi

{: .label }
Ali Ozeir

# Reference documentation
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Creating Flask App

### create_app()

**Route:** 
none

**Methods:** 
none

**Purpose:** 
This function is responsible for creating the Flask application instance, configuring it with secret key and database URI, initializing the SQLAlchemy database instance, registering blueprints for different URLs, creating database models, initializing the login manager, and defining a function to load a user.

**Sample output:** 
none

---

## Register

### @auth.route('/register')

**Route:** 
/register

**Methods:** 
`GET` `POST`

**Purpose:** 
This route handles the registration process, accepting both GET and POST methods. Users can enter their username and password to create a new account. The application checks if the username already exists in the database and validates the password against specified criteria. Upon successful registration, the user is logged in and redirected to the notes.html which is the main page with a success message. Otherwise, an error message is displayed. Additionally, the register.html file is rendered and passes the current user as a variable to the template.

**Sample output:**
Browser shows: `Successfully logged in!`

---

## Check Database

### @auth.route('/check_database')

**Route:** 
'/check_database'

**Methods:** 
`GET`

**Purpose:** 
This route is for debugging purposes and checks the users stored in the database. It retrieves all users from the database and prints their information.

**Sample output:**
None 

---

## Login

### @auth.route('/login')

**Route:** 
('/login')

**Methods:** 
`GET``POST`

**Purpose:** 
This route handles user login. It receives the username and password from the login form, checks if the user exists in the database, compares the hashed password, logs in the user if the credentials are correct, and redirects them to the notes page upon successful login.

**Sample output:**
Browser shows: `Database flushed and populated with some sample data.`

---

## Logout

### @auth.route('/logout')

**Route:** 
('/logout')

**Methods:** 
`GET``POST`

**Purpose:** 
This route handles user logout. It logs out the current user and redirects them to the login page.

**Sample output:**
Browser shows: `Successfully logged out!`

---

## Notes

### @views.route('/notes')

**Route:** 
('/notes')

**Methods:** 
`GET`

**Purpose:** 
This route renders the 'notes.html' template, which displays the notes for the current user.

**Sample output:**
Browser shows: Rendered 'notes.html' template with user's notes.

---

## Index

### @views.route('/index')

**Route:** 
('/index')

**Methods:** 
`GET`

**Purpose:** 
This route renders the 'index.html' template.

**Sample output:**
Browser shows: Rendered 'index.html' template.

---

## Home

### @views.route('/')

**Route:** 
('/')

**Methods:** 
`GET``POST`

**Purpose:** 
This route renders the 'notes.html' template, displaying the notes for the current user. It retrieves the notes from the database based on the current user's ID.

**Sample output:**
Browser shows: Rendered 'notes.html' template with user's notes.

---

## Hinzufügen einer Note

### @views.route('/add_note')

**Route:** 
('/add_note')

**Methods:** 
`POST`

**Purpose:** 
This route handles the addition of a new note. It extracts the title and content from the request form, creates a new note object, adds it to the database, and redirects the user to the home page with a success message.

**Sample output:**
Redirect to main page with success message upon adding a note.

---

## Bearbeiten einer Note

### @views.route('/edit_note/')

**Route:** 
('/edit_note')

**Methods:** 
`GET``POST`

**Purpose:** 
This route handles the editing of a note. It retrieves the note from the database, allows the user to edit the title and content, updates the note in the database, and redirects the user to the home page with a success message.

**Sample output:**
Rendered 'notes.html' template with user's notes.

---

## Hinzufügen einer Page

### addPage()  

**Route:** 
none

**Methods:** 
none

**Purpose:** 
An alert is displayed when the "Add Page" button is clicked, suggesting an upgrade to unlock features.

**Sample output:**
Alert is shown.

---

## Löschen einer Note

### @views.route('/delete_note')

**Route:** 
('/delete_note/')

**Methods:** 
`GET``POST`

**Purpose:** 
This route handles the deletion of a note. It retrieves the note from the database, deletes it, and redirects the user to the notes page with a success message.

**Sample output:**
Redirect to notes pages with success message upon deleting a note.

---

## RegistrationForm

### class RegistrationForm(FlaskForm)

**Purpose:** 
This class defines a FlaskForm for user registration. It includes fields for username, password, and confirm password, along with validators to ensure that the input is required and meets certain length requirements. The form also includes validation to ensure that the password and confirm password fields match.

---

## LoginForm

### class LoginForm(FlaskForm)

**Purpose:** 
This class defines a FlaskForm for user login. It includes fields for username and password, along with validators to ensure that the input is required.

---

## NoteForm

### class NoteForm(FlaskForm)

**Purpose:** 
This class defines a FlaskForm for creating a note. It includes fields for title and content, along with validators to ensure that the input is required and meets certain length requirements.

---

## EditNoteForm

### class EditNoteForm(FlaskForm)

**Purpose:** 
This class defines a FlaskForm for editing a note. It includes fields for the ID of the note, title, and content, along with validators to ensure that the input is required and meets certain length requirements.

---

## Display Selected Placeholder

### showPlaceholder(placeholderNumber) 

**Route:** 
none

**Methods:** 
none

**Purpose:** 
This function is responsible for displaying the selected placeholder while hiding others. It also makes the "Save" button visible.

**Sample output:**
Make one place holder visible.

--- 

## Update Text Format

### updateText(format) 

**Route:** 
none

**Methods:** 
none

**Purpose:** 
This function is used to update the text in the active placeholder based on the selected text format (Normal, Bold, Underline, StrikeThrough).

**Sample output:**
Change text format.

--- 