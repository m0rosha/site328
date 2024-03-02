from flask import Flask, render_template
from db import get_all_products, add_products

app = Flask(__name__, template_folder='', static_folder='static')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home/products")
def products():
    
    return render_template('./products.html', products=get_all_products())

@app.route("/home/story")
def story():
    with open("static\story.txt", "r") as file:
        txt_content = file.read()
    return render_template('./story.html', txt_content=txt_content)

@app.route("/home/locations")
def locations():
    return render_template('./locations.html')

@app.route("/home/careers")
def careers():
    return render_template('./careers.html')



if __name__ == "__main__":
    app.run(debug=True)