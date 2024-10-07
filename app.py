from flask import Flask, render_template
from db import inventory
from routes import setup_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456787"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petfam_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance with the Flask app
inventory.init_app(app)

setup_routes(app)

app.static_folder = 'static'

if __name__ == '__main__':
    with app.app_context():
        inventory.create_all()  # Create database tables
    app.run(debug=True, port=5001)
