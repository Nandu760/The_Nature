from flask import Flask
from Blueprint.routes import blueprint
from Blueprint.extensions import mail

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'

    # Mail configuration — replace with your email info
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'jangidnisha83@gmail.com'
    app.config['MAIL_PASSWORD'] = 'jpzlmvrnlzujspuf'

    mail.init_app(app)

    app.register_blueprint(blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)