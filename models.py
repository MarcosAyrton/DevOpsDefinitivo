from app import db
from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import relationship

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria_id = db.Column(db.Integer, ForeignKey('categoria.id'), nullable=False)
    categoria = relationship('Categoria', back_populates='productos')
    precio = relationship('Precio', back_populates='producto', uselist=False)

    def __str__(self):
        return self.nombre

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)
    productos = relationship('Producto', back_populates='categoria')

    def __str__(self):
        return self.categoria

class Precio(db.Model):
    id = db.Column(db.Integer, ForeignKey('producto.id'), primary_key=True)
    precio = db.Column(Numeric(precision=10, scale=2), nullable=False)
    producto = relationship('Producto', back_populates='precio')

    def __str__(self):
        return f"{self.precio:.2f}"
