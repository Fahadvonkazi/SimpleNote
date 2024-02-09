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

---

## 01: Database Utilization

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 29-11-2023

### Problem statement
The project identified the need for efficient database management to handle data effectively and pass DB objects to Python.

### Decision
The team opted to utilize SQLite as the relational database. SQLite was chosen due to its suitability for small projects, requiring minimal server configuration. Additionally, Flask-SQLAlchemy was selected as the ORM framework, streamlining the interaction between Python objects and the database.

### Regarded options
**Consider alternative databases like MySQL or PostgreSQL**
  - *Pro:* Provides potentially greater scalability and robustness
  - *Con:* May introduce additional complexity and configuration overhead
  
**Evaluate other ORM frameworks like Django ORM**
  - *Pro:* Offers alternative features and functionalities
  - *Con:* Might require adaptation to project requirements
  
---

## 02: WYSIWYG-Editor

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-11-2023

### Problem statement
The complexity of designing the notes.html page as our specifications proved challenging and complex.

### Decision
To address this complexity, we opted for a WYSIWYG editor, aiming to streamline the design process and reduce frontend dependencies.

### Regarded options
**Implement a custom HTML/CSS design for the notes.html page**
  - *Pro:* Provides complete control over design and layout
  - *Con:* Requires significant development effort and may increase complexity

---

## 03: Login Mechanism

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 12-12-2023

### Problem statement
Implementation of user login is necessary to grant access to user data, e.g. notes after login.

### Decision
We collectively opted for Flask-Login as the framework for implementing a straightforward login system. This choice provides methods for login, logout, user loading, and login status verification.

### Regarded options
**Evaluate alternative authentication frameworks**
  - *Pro:* Potential for finding a framework better suited to project requirements
  - *Con:* Time-consuming evaluation process, potential learning curve for new framework
  
**Implement custom authentication logic without using a framework (too complex)**
  - *Pro:* Full control over authentication process, tailored to project needs
  - *Con:* Highly complex and time-consuming to implement, potential for security vulnerabilities without established framework
  
---

## 04: Package Organization

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 18-12-2023

### Problem statement
Managing all routes becomes complex without segregating business logic into different files.

### Decision
We agreed to store routes, registration/login logic, and form creation in separate files:
views.py: Routes are stored separately due to their abundance.
models.py: The data model was simplified to manage complexity.
auth.py: Registration and login logic are stored in a separate file.
forms.py: Forms are imported and created here.

### Regarded options
**Keep all routes in a single file**
  - *Pro:* Simplifies file management
  - *Con:* May lead to a large, unwieldy file and hinder code readability and maintenance

**Segregate routes based on functionality**
  - *Pro:* Improves code organization and maintainability
  - *Con:* May require additional file management overhead

---

## 05: Templates Decision

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 19-12-2023

### Problem statement
The login page and register page have very similar elements on the GUI, which requires us to consolidate all these elements into one file to serve as a template. This will save us time, lines of code, and simplify the structure.

### Decision
The SimpleNote team chose to create an HTML base template, incorporating common elements and Bootstrap imports across screens. Other HTML templates will extend base.html, reducing code duplication and simplifying the structure.

### Regarded options
**Using a single HTML base template with shared elements**
  *Pro:* Reduces code duplication, simplifies maintenance, and ensures consistency
  *Con:* May limit customization options for individual pages

---

## 06: GUI-Navigation

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 13-01-2023

### Problem statement
Improving user navigation after registration and login for support and a more seamless user experience regarding the navigation.

### Decision
We decided to automatically redirect users upon successful registration or login, supported by green or red banners for success or failure. If the banner is red, there will be a flash and a reason appears why the process didn't function correctly, e.g. "Log-In not successfull".

### Regarded options
**Implement manual navigation prompts after registration and login**
  - *Pro:* Complete control over navigation flow
  - *Con:* Increased user effort, potential for inconsistencies or errors in navigation prompts

**Explore user authentication libraries for navigation assistance**
  - *Pro:* Utilizes established libraries for navigation, potentially reducing development time
  - *Con:* Dependency on external libraries, may require customization to fit project needs

**Design custom navigation elements for a tailored user experience**
  - *Pro:* Allows for highly customized and intuitive navigation
  - *Con:* Increased development time and complexity, potential for inconsistencies without careful design and testing

---

## 07: Speicherung der Notizen

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 13-01-2023

### Problem statement
There was no efficient method in place to store the notes, leading to uncertainty regarding data management.

### Decision
Team SimpleNote considered implementing a "Save-Button" to allow users the option to store their notes when desired, providing a straightforward solution to address the problem.

### Regarded options
**Implementing automatic periodic saving of notes without user intervention**
  - *Pro:* Ensures data persistence and minimizes the risk of data loss due to user oversight
  - *Con:* May increase server load and resource usage, potentially impacting performance

---

## 08: Reducing and Minimizing Functionality

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 19-01-2024

### Problem statement
The project team encountered a challenge due to the ambitious scope initially set for the application.

### Decision
Recognizing the limitations of time and resources, the team opted to streamline the project by scaling back certain features, such as the planned integration of books. This decision was made collaboratively to ensure project feasibility within the given constraints.

### Regarded options
**Keep all the other planned functionalities intact**
  - *Pro:* Ensures the fulfillment of the project's original vision
  - *Con:* May lead to project delays and increased complexity

**Prioritize functionalities and discard less essential ones to meet the project deadline**
  - *Pro:* Allows a more focused and achievable development approach
  - *Con:* Some planned features may need to be sacrificed, potentially impacting the user experience

---