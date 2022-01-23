''' 터미널에 입력할 실행 코드
파이썬 터미널: set FLASK_APP=jh_flask
             set FLASK_ENV=development
             flask run
컴퓨터 터미널: ngrok.exe http 5000  (껐다 키면 url 새로 생성)
'''

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    ### ORM
    db.init_app(app)
    migrate.init_app(app, db)
    #from . import models

    ### 블루프린트
    from .views import main_views, policynews
    app.register_blueprint(main_views.bp)
    #app.register_blueprint(policynews.bp)

    return app
'''app = create_app()
if __name__ == '__main__':
    app.run(debug=True) #host='0.0.0.0', port=4040 등으로 지정 가능'''

