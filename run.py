from flask import Flask
from flask_smorest import Api
from app.api.routes import blp

def create_app():
    app = Flask(__name__)
    app.config['API_TITLE'] = 'Todo API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    api = Api(app)
    api.register_blueprint(blp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)