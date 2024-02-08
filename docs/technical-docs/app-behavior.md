---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
Fahad von Kazi

{: .label }
Ali Ozeir

# App behavior
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## User Functionalities
The following functionalities are available to the user:

### Log-in
The application allows users to log in using their credentials to access additional functionalities and view their notes.

### Register
The application enables users to create a new account by entering their desired username and password.

### Display of Notes
The application allows users to view an overview of all existing books and pages that have been created.

### Create Books and Pages
Users can create new books and pages for their notes within the application.

### Edit Notes
Users can edit notes by modifying the title or content of the page.

### Text Formatting
Additionally, the app provides text formatting features to format the entered text accordingly.



### Register-Page
Hier kann sich der Nutzer registireren und einen Account erstellen, indem den gewünschten Benutzernamen und das Passwort eingibt. Diese werden vom Frontend übergeben und nach Prüfung wird der Benutzername und das Passwort als hash gespeichert. Die Variable wird der Datenbank übergeben, welches dann ein neues User-Objekt erstellen. Falls der User doch wieder zurück zur Log-In-Page möchte, kann dieser das durch Klick auf "Log in!" tun.

### Main-Page
Hier wird die Side Navigation Bar mit den einzelnen Büchern und ihren Pages angezeigt. Hier kann der Nutzer seine Notizen erstellen, bearbeiten und löschen. Der Nutzer kann durch die Buttons "Add new page" und "add new book" neue Bücher und Seiten erstellen. Außerdem gibt es oben Textformatierungsmöglichkeiten. Der Nutzer kann sich auch wieder ausloggen. Die Notizen werden in der Datenbank gespeichert.

## Navigation
The navigation proceeds as follows: The user first registers. Upon successful registration, the user is automatically redirected to the log-in page and asked to log in. After successful login, the user is automatically redirected to the main page, where the user can create and edit their notes.

## Application Logic
![Figure 1: App Behavior, Source: Own Illustration](assets/images/Appverhalten.png)

Figure 1 illustrates the behavior and relationships of the application. The processes are explained in more detail below:

### Log-In Page
Here, the user can log in with their username and password. The input data is compared with the entries stored in the database. If the entered information is correct, a success message is displayed, and the user is redirected to the log-in-page. Otherwise, an error message appears, and the user must re-enter the information. The prerequisite for this function is that the user has already registered. If no account exists, the user can navigate to the register page by clicking "Create one!"

### Register Page
Here, the user can register and create an account by entering the desired username and password. These are passed from the frontend, and after verification, the username and password are saved as a hash. The variable is passed to the database, which then creates a new user object. If the user wants to go back to the log-in page, they can do so by clicking "Log in!"

### Main Page
Here, the side navigation bar with the individual books and their pages is displayed. The user can create, edit, and delete their notes here. The user can create new books and pages by clicking the "Add new page" and "add new book" buttons. Additionally, there are text formatting options at the top. The user can also log out. The notes are stored in the database.
