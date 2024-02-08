---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

# Data model
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

[Figure 2: Data Model, Source: Own Illustration](docs/assets/images/datamodel.png)

Figure 2 illustrates the data model of the application. The processes are explained in more detail below:

The data model of the project consists of the tables User, Notes, and Pages. The first table, User, consists of the attributes ID as the primary key, Password, Username, and Password. The entity Note also has an ID as the primary key and consists of the attribute Content. It contains the foreign keys UserID and PageID. The entity Page again contains an ID as the primary key and a Title. Additionally, it contains the foreign key NoteID.
