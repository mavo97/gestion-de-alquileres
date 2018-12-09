from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Propietario(db.Model):#Propietario
    id = db.Column(db.String(5), primary_key=True) #nif
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    propietarios = db.relationship('Vivienda', backref='propietario', lazy=True)

class Agencia(db.Model):#Agencia
    id = db.Column(db.String(5), primary_key=True) #cif
    codigo_agencia = db.Column(db.String(5))
    direccion = db.Column(db.String(50), nullable=False)
    agencias = db.relationship('Vivienda', backref='agencia', lazy=True)

class Vivienda(db.Model):#Vivivenda
    id = db.Column(db.String(5), primary_key=True) #codigo vivienda
    propietario_id = db.Column(db.String(5), db.ForeignKey('propietario.id'), nullable=False)#nif
    agencia_id = db.Column(db.String(5), db.ForeignKey('agencia.id'), nullable=False)#cif
    numero = db.Column(db.String(5))
    piso = db.Column(db.String(5))
    cp = db.Column(db.String(5))
    poblacion = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    alquiler = db.relationship('Alquiler', backref='vivienda', lazy=True)


class Inquilino(db.Model):#Inquilino
    id = db.Column(db.String(5), primary_key=True) #nif
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    alquiler2 = db.relationship('Alquiler', backref='inquilino', lazy=True)

class Alquiler(db.Model):#Alquiner
    id = db.Column(db.String(5), primary_key=True) #codigo alquiler
    inquilino_id = db.Column(db.String(5), db.ForeignKey('inquilino.id'), nullable=False)#nif
    vivienda_id = db.Column(db.String(5), db.ForeignKey('vivienda.id'), nullable=False)#codigo vivienda
    fianza = db.Column(db.String(10))
    fecha_firma = db.Column(db.String(10))
    fecha_inicio = db.Column(db.String(10))
    fecha_fin = db.Column(db.String(10))
    importe_mensual = db.Column(db.String(10))

