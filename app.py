# create_app aus dem aktuellen Ordner wird importiert
from . import create_app

# Hier wird eine Flask-Anwendung mit der create_app-Funktion erstellt
app = create_app()

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)

