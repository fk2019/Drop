from flask import Flask
from .views.main import main
from .views.auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.register_blueprint(main)
app.register_blueprint(auth)


if __name__ == '__main__':
    app.run()
