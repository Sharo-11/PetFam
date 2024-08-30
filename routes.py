from flask import render_template, redirect, request, url_for, Flask
from db import inventory  # Import inventory from db.py
from models import Pet, PetFood, Toy, Finance, Appointment, Contact

def setup_routes(app: Flask):
    @app.route('/')
    def first_page():
        return render_template("index.html")

    @app.route('/about')
    def about():
        return render_template("aboutus.html")
    
    @app.route('/contact')
    def contact():
        return render_template("contact.html")
    
    @app.route('/donation')
    def donation():
        return render_template("donation.html")
    
    @app.route('/adopt')
    def adopt():
        return render_template("adopt.html")
    
    @app.route('/community')
    def community():
        return render_template("community.html")
    
    @app.route('/foster')
    def foster():
        return render_template("foster.html")
    
    @app.route('/appointment')
    def appointment():
        return render_template("appointment.html")
    
    @app.route('/admin')
    def admin():
        pets = Pet.query.all()
        food_items = PetFood.query.all()
        toys = Toy.query.all()
        finances = Finance.query.all()
        return render_template('admin.html', pets=pets, food_items=food_items, toys=toys, finances=finances)

    @app.route('/add_pet', methods=['GET', 'POST'])
    def add_pet():
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            breed = request.form['breed']
            status = request.form['status']
            new_pet = Pet(name=name, age=age, breed=breed, status=status)
            inventory.session.add(new_pet)
            inventory.session.commit()
            return redirect(url_for('admin'))
        return render_template('add_pet.html')

    @app.route('/remove_pet/<int:pet_id>', methods=['POST'])
    def remove_pet(pet_id):
        pet = Pet.query.get(pet_id)
        inventory.session.delete(pet)
        inventory.session.commit()
        return redirect(url_for('admin'))

    @app.route('/add_food', methods=['GET', 'POST'])
    def add_food():
        if request.method == 'POST':
            food_type = request.form['food_type']
            quantity = request.form['quantity']
            new_food = PetFood(food_type=food_type, quantity=quantity)
            inventory.session.add(new_food)
            inventory.session.commit()
            return redirect(url_for('admin'))
        return render_template('add_food.html')

    @app.route('/add_toy', methods=['GET', 'POST'])
    def add_toy():
        if request.method == 'POST':
            toy_type = request.form['toy_type']
            quantity = request.form['quantity']
            new_toy = Toy(toy_type=toy_type, quantity=quantity)
            inventory.session.add(new_toy)
            inventory.session.commit()
            return redirect(url_for('admin'))
        return render_template('add_toy.html')

    @app.route('/add_finance', methods=['GET', 'POST'])
    def add_finance():
        if request.method == 'POST':
            amount = request.form['amount']
            date = request.form['date']
            description = request.form['description']
            new_finance = Finance(amount=amount, date=date, description=description)
            inventory.session.add(new_finance)
            inventory.session.commit()
            return redirect(url_for('admin'))
        return render_template('add_finance.html')

    @app.route('/approve_appointment/<int:appointment_id>', methods=['POST'])
    def approve_appointment(appointment_id):
        appointment = Appointment.query.get(appointment_id)
        # Handle appointment approval
        return redirect(url_for('admin'))

    @app.route('/remove_appointment/<int:appointment_id>', methods=['POST'])
    def remove_appointment(appointment_id):
        appointment = Appointment.query.get(appointment_id)
        inventory.session.delete(appointment)
        inventory.session.commit()
        return redirect(url_for('admin'))

    @app.route('/remove_contact/<int:contact_id>', methods=['POST'])
    def remove_contact(contact_id):
        contact = Contact.query.get(contact_id)
        inventory.session.delete(contact)
        inventory.session.commit()
        return redirect(url_for('admin'))
