from flask import render_template, Flask

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
    def commnity():
        return render_template("community.html")
    
    @app.route('/dogs')
    def dogs():
        return render_template("dogs.html")
    
    @app.route('/cats')
    def cats():
        return render_template("cats.html")
    
    @app.route('/rabbit')
    def rabbit():
        return render_template("rabbit.html")
    
    @app.route('/parrot')
    def parrot():
        return render_template("parrot.html")