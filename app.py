from flask import Flask
from routers.musical_scale_routes import musical_scale_bp

app = Flask(__name__)

app.register_blueprint(musical_scale_bp, url_prefix ="/musical-scale")


if __name__ == '__main__':
    app.run(debug=True)