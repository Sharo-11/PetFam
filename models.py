from db import inventory  # Import the inventory instance from db.py

class Pet(inventory.Model):
    id = inventory.Column(inventory.Integer, primary_key=True)
    name = inventory.Column(inventory.String(100), nullable=False)
    age = inventory.Column(inventory.Integer, nullable=False)
    breed = inventory.Column(inventory.String(100), nullable=False)
    status = inventory.Column(inventory.String(50), nullable=False)

class PetFood(inventory.Model):
    id = inventory.Column(inventory.Integer, primary_key=True)
    food_type = inventory.Column(inventory.String(100), nullable=False)
    quantity = inventory.Column(inventory.Integer, nullable=False)

class Toy(inventory.Model):
    id = inventory.Column(inventory.Integer, primary_key=True)
    toy_type = inventory.Column(inventory.String(100), nullable=False)
    quantity = inventory.Column(inventory.Integer, nullable=False)

class Finance(inventory.Model):
    id = inventory.Column(inventory.Integer, primary_key=True)
    amount = inventory.Column(inventory.Float, nullable=False)
    date = inventory.Column(inventory.Date, nullable=False)
    description = inventory.Column(inventory.String(255), nullable=False)
