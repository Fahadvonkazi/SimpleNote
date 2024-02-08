---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
Fahad von Kazi

{: .label }
Ali Ozeir

# App structure, incl. context
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details> 

## Overview of the App Architecture
The web app "SimpleNote" utilizes an architecture consisting of the database, user interface, and business logic. The various layers communicate with each other via the HTTP protocol, exchanging requests and responses. The user interface sends requests to the business logic, which processes the request and retrieves or stores the corresponding data from the database. The business logic then sends the required data back to the frontend to display it to the users on the interface.

### Database
In this layer, SQLAlchemy is used to manage access to the SQLite database. SQLite is employed as the database system because it is a simple, relational database. SQLAlchemy facilitates interaction with the database by providing an object-oriented interface.

### User Interface
The user interface is responsible for interacting with the user of the application. Flask templates and Jinja2 are used to create the HTML pages. Furthermore, the SimpleNote team has utilized the Bootstrap framework to design a corresponding frontend.

### Business Logic
This layer is responsible for data processing and executing the business logic. Python is used in combination with SQLAlchemy to process the data.

## Project Structure
The project structure is as follows: In the main folder "SimpleNote," the file "app.py" creates the application. Additionally, the folder contains the packages described below. Moreover, external packages such as Flask-SQLAlchemy, Flask, and Flask-Login are utilized.

### __ init __.py
This package is used to initialize and configure the Flask package. The application is connected to the SQLAlchemy database, and blueprints are registered for various parts of the application.

### auth.py
The auth package is required for user authorization and authentication. It contains routes and functions for login, registration, and logout.

### forms.py
The file forms.py defines various forms using Flask-WTF and WTForms, which are used to process user input.

### models.py
The models package contains models that define the structure of the data in the database. This allows data to be stored and retrieved from the database.

### views.py
The views package contains routes and logical functionalities for various views of the website.