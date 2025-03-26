from flask import Flask

app = Flask("My Flask Application")

@app.route("/")
def hello():
    return "<h1>My First Hello World!</h1>"

@app.route("/cart")
def shopping_cart():
    return "<h2>Shopping Cart</h2><p>Your cart is currently empty.</p>"

@app.route("/about")
def about_page():
    return """
    <h1>About Us</h1>
    <p>We're a passionate team dedicated to creating great web experiences!</p>
    """

if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000


