from flask import Flask
from flask_cors import CORS
from routers.musical_scale_routes import musical_scale_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

client_url = os.getenv("LOCAL_URL_FRONTEND_DEBUG")

CORS(app, resources={
    r"/musical-scale/*": {
        "origins": client_url,
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"],
        "max_age": 3600
    }
})

app.register_blueprint(musical_scale_bp, url_prefix ="/musical-scale")


if __name__ == '__main__':
    app.run(debug=True)