from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/MiaSecret_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import (
    Producto,
    Categoria, 
    Precio,
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def lista_productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria_nombre = request.form['categoria']
        precio_valor = request.form['precio']

        # Buscar o crear la categoría
        categoria = Categoria.query.filter_by(categoria=categoria_nombre).first()
        if not categoria:
            categoria = Categoria(categoria=categoria_nombre)
            db.session.add(categoria)
            db.session.commit()

        # Crear el producto
        producto = Producto(nombre=nombre, categoria=categoria)
        db.session.add(producto)
        db.session.commit()

        # Crear el precio asociado al producto
        precio = Precio(precio=precio_valor, producto=producto)
        db.session.add(precio)
        db.session.commit()

        return redirect(url_for('lista_productos'))
    return render_template('add_producto.html')

if __name__ == '__main__':
    app.run(debug=True)




