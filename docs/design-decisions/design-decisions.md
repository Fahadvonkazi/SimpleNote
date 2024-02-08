---
title: Design Decisions
nav_order: 3
---

{: .label }
Fahad von Kazi

{: .label }
Ali Ozeir

# [Design decisions]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Reducing and Minimizing Functionality

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 19-01-2024

### Problem statement
We aimed for too much.

### Decision
We collectively decided to abandon certain functionalities, such as the integration of Books, as it became unfeasible towards the end.

### Regarded options
- Keep all the other planned functionalities intact
- Prioritize functionalities and discard less essential ones to meet the project deadline

---

## 02: Database Utilization

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 18-12-2023

### Problem statement
Effective database management is required to handle the data efficiently and pass DB objects to Python.

### Decision
SQLite is utilized as the relational database, suitable for small projects due to its simplicity and lack of server configuration requirements. Additionally, Flask-SQLAlchemy serves as the ORM framework, allowing for Python objects to be passed to the database. 

### Regarded options
- Consider alternative databases like MySQL or PostgreSQL
- Evaluate other ORM frameworks like Django ORM

---

## 03: WYSIWYG-Editor

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 18-12-2023

### Problem statement
Designing the notes.html page to meet our specifications proved to be overly complex.


### Decision
We opted for a WYSIWYG editor to facilitate a more intuitive design, reducing complexity and frontend dependencies.

### Regarded options
- Implement a custom HTML/CSS design for the notes.html-page

---

## 04: Package Organization

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 13-01-2024

### Problem statement
Managing all routes becomes complex without segregating business logic into different files.

### Decision
We agreed to store routes in separate files due to their abundance, along with logic for registration and login, minimizing code clutter and improving maintainability:
views.py: The project team decided to store the routes in a separate file due to the large number of routes.
models.py: The data model was simplified due to its complexity. 
auth.py: The project team opted to store the logic for registration and login in a separate file.
forms.py: Forms are imported and created here.

### Regarded options
- Keep all routes in a single file (huge disadvantage = one long file => no overview and decentralisation and problems with debugging are forcasted in that method)
- Segregate routes based on functionality

---

## 05: Templates Decision

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 13-01-2024

### Problem statement
The login page and register page have very similar elements on the GUI, which requires us to consolidate all "similar" elements into one file to serve as a template. This will save us time, lines of code, and simplify the structure.

### Decision
The SimpleNote team has decided to create an HTML base template. This template includes Bootstrap imports and elements used across screens (e.g., footer). Other HTML templates will extend base.html. This significantly reduces the amount of code and simplifies the structure.

### Regarded options
- Creating separate HTML templates for login and register pages.
  **Pros:** Allows for individual customization of each page.
  **Cons:** Increases code duplication and complicates maintenance.
- Using a single HTML base template with shared elements.
  **Pros:** Reduces code duplication, simplifies maintenance, and ensures consistency.
  **Cons:** May limit customization options for individual pages.

---

## 05: Login Mechanism

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 18-12-2023

### Problem statement
Implementation of user login is necessary to grant access to user data, e.g. notes after login.

### Decision
We collectively opted for Flask-Login as the framework, facilitating the implementation of a straightforward login system with methods for login, logout, user loading, and login status verification. 

### Regarded options
- Evaluate alternative authentication frameworks
- Implement custom authentication logic without using a framework (=>too complex)

---


## 06: GUI-Navigation

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 13-01-2023

### Problem statement
Improving user navigation post-registration and login for support and a more seamless user experience regarding the navigation.


### Decision
We decided to automatically redirect users upon successful registration or login, supported by green or red banners for success or failure. If the banner is red, there will be a flash and a reason appears why the process didn't function correctly, e.g. "Log-In not successfull".


### Regarded options
- Implement manual navigation prompts post-registration and login
- Explore user authentication libraries for navigation assistance
- Design custom navigation elements for a tailored user experience

---