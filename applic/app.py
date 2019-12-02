import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

@app.route('/')
def hello_world():
    return 'Привіт дев!!!'

if __name__ == '__main__':
    app.run()