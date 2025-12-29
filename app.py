import os
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Flask DevOps App")
ENV = os.getenv("ENV", "development")

@app.route("/")
def home():
    return f"🚀 {APP_NAME} running in {ENV} environment"

@app.route("/health")
def health():
    return {"status": "UP", "environment": ENV}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
