from flask import Flask 
from extensions import db
from main.routes import main_bp
from config import config

def creat_app():
    app = Flask (__name__)

    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(main_bp)

    return app

app = creat_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(host='0.0.0.0', port=5000)