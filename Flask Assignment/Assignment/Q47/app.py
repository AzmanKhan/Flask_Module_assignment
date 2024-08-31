from flask import Flask
from app.main import main as main_blueprint
from app.auth import auth as auth_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
