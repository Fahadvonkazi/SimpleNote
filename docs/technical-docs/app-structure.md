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

## Übersicht über die App-Architektur
Die Web-App "SimpleNote" verwendet eine Architektur, bestehend aus der Datenbank, Nutzeroberfläche und Geschäftslogik.

### Datenbank
In dieser Schicht wird SQLAlchemy verwendet, um den Zugriff auf die SQLite-Datenbank zu verwalten. SQLite wird als Datenbanksystem eingesetzt, da es eine einfache, relationale Datenbank ist. SQLAlchemy erleichtert die Interaktion mit der Datenbank, indem es eine objektorientierte Schnittstelle bereitstellt.

### Nutzeroberfläche
Die Nutzeroberfläche ist für die Interaktion mit dem Nutzenden der Anwendung zuständig. Dabei wird das Flask-Template und Jinja2 für die Erstellung der HTML-Pages verwendet. Des Weiteren hat dasa Team SimpleNote das Framework Bootstrap eingesetzt, um ein entspechendes Frontend zu gestalten.

### Geschäftslogik
Diese Schicht ist zuständig für die Datenverarbeitung und die Ausführung der Geschäftslogik. Dabei wird Python in Kombination mit SQLAlchemy, um die Daten zu verarbeiten, verwendet.

Die verschiedenen Schichten kommunizieren miteinander über das HTTP-Protokoll, indem sie Anfragen und Antworten miteinander austauschen. Die Nutzeroberfläche sendet Anfragen an die Geschäftslogik, welche die Anfrage verarbeitet und die entsprechenden Daten aus der Datenbank abruft oder speichert. Die Geschäftslogik sendet dann die benötigten Daten zurück an das Frontend, um sie den Benutzern zur Anzeige auf der Oberfläche bereitzustellen.

## Projektverzeichnisstruktur

