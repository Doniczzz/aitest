from flask import Flask
from api import app

app = Flask(__name__)

if __name__ == '__main__':
    app.run()