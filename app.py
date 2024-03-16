from flask import Flask, render_template, request, redirect, url_for, session
from db import get_all_products, add_products,get_prod_by_id

app = Flask(__name__, template_folder='', static_folder='static')

@app.route("/")
def index():
    return render_template('home.html')



@app.route("/home/story")
def story():
    with open("static\story.txt", "r") as file:
        txt_content = file.read()
    return render_template('./story.html', txt_content=txt_content)

@app.route("/home/locations")
def locations():
    with open("static\locations.txt", "r") as file:
        txt_content = file.read()
    return render_template('./locations.html', txt_content=txt_content)

@app.route("/home/addToCart", methods=["POST"])
def addToCart():
    if request.method == "POST":
       
        try:
            id = request.form.get('id')
            cart = session['cart']
            if id in cart.keys():
                cart[id] = int(cart[id]) + 1
                
            else:
                cart[id] = 1
            session['cart'] = cart
            
            
        except:
            session['cart'] = {id:1}
        return redirect(url_for('products'))


@app.route("/home/cart")
def cart():
    try:
        elementsId = session['cart']
        cart = []
        total = 0
        for id in elementsId:
            
            element = get_prod_by_id(id)
            
            total += float(element[2]) * elementsId[id]
             
            cart.append((element[0], elementsId[id]))

        return render_template('cart.html', cart=cart, total=total,products=get_all_products())
    except Exception as e:
        print(e)
        return render_template('cart.html', cart=[],products=get_all_products())
@app.route("/home/products")
def products():
    if request.method == "POST":
       
        try:
            id = request.form.get('id')
            cart = session['cart']
            if id in cart.keys():
                cart[id] = int(cart[id]) + 1
            else:
                cart[id] = 1
            session['cart'] = cart
            return render_template('products.html', products=get_all_products(),cart=cart)
        except:
            session['cart'] = {id:1}
        return redirect(url_for('products'))
        
    else:
        return render_template('products.html', products=get_all_products(),cart=0)
        
    

app.secret_key = "secret"
if __name__ == "__main__":
    app.run(debug=True)