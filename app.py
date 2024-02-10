from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='static')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home/products")
def products():
    return render_template('./products.html')

@app.route("/home/story")
def story():
    return render_template('./story.html')

@app.route("/home/locations")
def locations():
    return render_template('./locations.html')

@app.route("/home/careers")
def careers():
    return render_template('./careers.html')

if __name__ == "__main__":
    app.run(debug=True)