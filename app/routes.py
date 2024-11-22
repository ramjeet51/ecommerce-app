from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Product
from app.forms import AddProductForm

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('home'))
    return render_template('add_product.html', form=form)
