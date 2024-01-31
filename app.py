from flask import Flask, render_template
from flask_login import LoginManager
from .views import views
from .models import User
from .auth import auth  # Importiere die auth-Blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key_for_dev_environment'
    app.register_blueprint(views)
    app.register_blueprint(auth)  # Registriere die auth-Blueprint

    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    return app

app = create_app()

# Home / Login/ Index Route
@app.route('/')
def home():
    return render_template('index.html')

# Notes Route
@app.route('/notes')
def notes():
    return render_template('notes.html')

# Register Route
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
