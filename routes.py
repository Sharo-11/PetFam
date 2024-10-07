from flask import render_template, redirect, request, url_for, flash, Flask
from db import inventory
from models import Pet, PetFood, Toy, Finance, Appointment, Contact
from datetime import datetime

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

    @app.route('/dogs')
    def dogs():
        return render_template("dogs.html")

    @app.route('/cats')
    def cats():
        return render_template("cats.html")

    @app.route('/parrot')
    def parrot():
        return render_template("parrot.html")

    @app.route('/rabbit')
    def rabbit():
        return render_template("rabbit.html")

    @app.route('/compatible')
    def compatible():
        return render_template("compatible.html")

    @app.route('/appointment')
    def appointment():
        return render_template("appointment.html")

    @app.route('/admin')
    def admin():
        pets = Pet.query.all()
        food_items = PetFood.query.all()
        toys = Toy.query.all()
        finances = Finance.query.all()
        total_amount = sum(finance.amount for finance in finances)
        return render_template('admin.html', pets=pets, food_items=food_items, toys=toys, finances=finances, total_amount=total_amount)

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
            flash('Pet added successfully!', 'success')
            return redirect(url_for('admin'))
        return render_template('add_pet.html')

    @app.route('/pet_panel')
    def pet_panel():
        adopted_pets = Pet.query.filter_by(status='Adopted').all()
        fostered_pets = Pet.query.filter_by(status='Fostered').all()
        donated_pets = Pet.query.filter_by(status='Donated').all()
        return render_template('pet_panel.html', adopted_pets=adopted_pets, fostered_pets=fostered_pets, donated_pets=donated_pets)

    def remove_item(model, item_id, redirect_endpoint):
        item = model.query.get(item_id)
        if item:
            inventory.session.delete(item)
            inventory.session.commit()
            flash('Item removed successfully!', 'success')
        else:
            flash('Item not found.', 'error')
        return redirect(url_for(redirect_endpoint))

    @app.route('/remove_pet/<int:pet_id>', methods=['POST'])
    def remove_pet(pet_id):
        return remove_item(Pet, pet_id, 'admin')

    @app.route('/add_food', methods=['GET', 'POST'])
    def add_food():
        if request.method == 'POST':
            food_type = request.form['food_type']
            if food_type == 'Other':
                food_type = request.form['other_food']
            quantity = request.form['quantity']
            unit = request.form['unit']
            new_food = PetFood(food_type=food_type, quantity=quantity, unit=unit)
            inventory.session.add(new_food)
            inventory.session.commit()
            flash('Food item added successfully!', 'success')
            return redirect(url_for('admin'))
        return render_template('add_food.html')

    @app.route('/food_panel')
    def food_panel():
        food_items = get_food_items()
        return render_template('food_panel.html', food_items=food_items)

    @app.route('/toys_panel')
    def toys_panel():
        toys = get_toys()
        return render_template('toys_panel.html', toys=toys)

    @app.route('/add_toy', methods=['GET', 'POST'])
    def add_toy():
        if request.method == 'POST':
            toy_type = request.form['toy_type']
            quantity = request.form['quantity']
            new_toy = Toy(toy_type=toy_type, quantity=quantity)
            inventory.session.add(new_toy)
            inventory.session.commit()
            flash('Toy added successfully!', 'success')
            return redirect(url_for('admin'))
        return render_template('add_toy.html')

    @app.route('/add_finance', methods=['GET', 'POST'])
    def add_finance():
        if request.method == 'POST':
            try:
                amount = float(request.form['amount'])
                date_str = request.form['date']
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                description = request.form['description']
                
                new_finance = Finance(amount=amount, date=date, description=description)
                inventory.session.add(new_finance)
                inventory.session.commit()
                flash('Finance record added successfully!', 'success')
                return redirect(url_for('admin'))
            except ValueError:
                flash("Please enter a valid amount.", 'error')
            except Exception as e:
                flash(f"An error occurred: {str(e)}", 'error')
        return render_template('add_finance.html')

    @app.route('/finance_panel')
    def finance_panel():
        finances = get_finances()
        total_amount = sum(finance.amount for finance in finances)
        return render_template('finance_panel.html', finances=finances, total_amount=total_amount)

    @app.route('/remove_finance/<int:finance_id>', methods=['POST'])
    def remove_finance(finance_id):
        return remove_item(Finance, finance_id, 'finance_panel')

    @app.route('/appointment_panel')
    def appointment_panel():
        appointments = get_appointments()
        return render_template('appointment_panel.html', appointments=appointments)

    @app.route('/approve_appointment/<int:appointment_id>', methods=['POST'])
    def approve_appointment(appointment_id):
        appointment = Appointment.query.get(appointment_id)
        # Handle appointment approval logic here (e.g., updating status)
        flash('Appointment approved!', 'success')
        return redirect(url_for('admin'))

    @app.route('/remove_appointment/<int:appointment_id>', methods=['POST'])
    def remove_appointment(appointment_id):
        return remove_item(Appointment, appointment_id, 'admin')

    @app.route('/contact_panel')
    def contact_panel():
        contacts = get_contacts()
        return render_template('contact_panel.html', contacts=contacts)

    @app.route('/remove_contact/<int:contact_id>', methods=['POST'])
    def remove_contact(contact_id):
        return remove_item(Contact, contact_id, 'admin')

    @app.route('/test')
    def test():
        return render_template("test.html")

    # Donation routes
    @app.route('/donate_money')
    def donate_money():
        return render_template("donate_money.html")

    @app.route('/donate_treats')
    def donate_treats():
        return render_template("donate_treats.html")

    @app.route('/donate_toys')
    def donate_toys():
        return render_template("donate_toys.html")

    @app.route('/donate_pets')
    def donate_pets():
        return render_template("donate_pets.html")

    @app.route('/donate_other')
    def donate_other():
        return render_template("donate_other.html")

    @app.route('/submit_donation', methods=['POST'])
    def submit_donation():
        donation_type = request.form['donation_type']
        amount = request.form.get('amount')
        item_type = request.form.get('item_type')
        
        # Logic to handle the donation based on type
        if donation_type == 'money':
            # Process monetary donation
            new_donation = Finance(amount=amount, description='Monetary Donation')
            inventory.session.add(new_donation)
        elif donation_type == 'toys':
            # Process toy donation
            new_toy_donation = Toy(toy_type=item_type)
            inventory.session.add(new_toy_donation)
        
        inventory.session.commit()
        flash('Donation submitted successfully!', 'success')
        return redirect(url_for('donation'))

    # Helper functions to fetch data from the database
    def get_food_items():
        return PetFood.query.all()

    def get_toys():
        return Toy.query.all()

    def get_finances():
        return Finance.query.all()

    def get_appointments():
        return Appointment.query.all()

    def get_contacts():
        return Contact.query.all()
