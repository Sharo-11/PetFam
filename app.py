from flask import Flask, render_template, redirect
from routes import setup_routes


app = Flask(__name__)
app.config['SECRET_KEY'] = "123456787"

setup_routes(app)

app.static_folder = 'static'

if __name__ == '__main__':
    app.run(debug=True, port = 5001)