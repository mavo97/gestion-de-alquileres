from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Propietario, Agencia, Vivienda, Inquilino, Alquiler
#---
import os 

app = Flask(__name__)
POSTGRES = {
    'user': 'mavo1997',
    'pw': '020897',
    'db': 'alquileres',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#--

#----------
#---
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registros/")
def registros():
    return render_template("registros.html")
#--
@app.route("/registro/propietario/", methods=["GET", "POST"])
def propietario():
    if request.method == "POST":
        new_propietario = Propietario(id=request.form["id"], nombre=request.form["nombre"],
        apellidos=request.form["apellidos"],telefono=request.form["telefono"],
        direccion=request.form["direccion"], email=request.form["email"])
        db.session.add(new_propietario)
        db.session.commit()
        return render_template("correcto.html")
    return render_template("propietario.html")
#--
@app.route("/registro/vivienda/", methods=["GET", "POST"])
def vivienda():
    if request.method == "POST":
        new_vivienda = Vivienda(id=request.form["id"], propietario_id=request.form["propietario_id"],
        agencia_id=request.form["agencia_id"],numero=request.form["numero"],piso=request.form["piso"],
        cp=request.form["cp"], poblacion=request.form["poblacion"], descripcion=request.form["descripcion"])
        db.session.add(new_vivienda)
        db.session.commit()
        return render_template("correcto.html")
    return render_template("vivienda.html")

#--
@app.route("/registro/agencia/", methods=["GET", "POST"])
def agencia():
    if request.method == "POST":
        new_agencia = Agencia(id=request.form["id"], codigo_agencia=request.form["codigo_agencia"],
        direccion=request.form["direccion"])
        db.session.add(new_agencia)
        db.session.commit()
        return render_template("correcto.html")
    return render_template("agencia.html")
#--

#--
@app.route("/registro/alquiler/", methods=["GET", "POST"])
def alquiler():
    if request.method == "POST":
        new_alquiler = Alquiler(id=request.form["id"], inquilino_id=request.form["inquilino_id"],
        vivienda_id=request.form["vivienda_id"], fianza=request.form["fianza"],fecha_firma=request.form["fecha_firma"],
        fecha_inicio=request.form["fecha_inicio"], fecha_fin=request.form["fecha_fin"], importe_mensual=request.form["importe_mensual"])
        db.session.add(new_alquiler)
        db.session.commit()
        return render_template("correcto.html")
    return render_template("alquiler.html")
#--

#--
@app.route("/registro/inquilino/", methods=["GET", "POST"])
def inquilino():
    if request.method == "POST":
        new_inquilino = Inquilino(id=request.form["id"], nombre=request.form["nombre"],
        apellidos=request.form["apellidos"], fecha_nacimiento=request.form["fecha_nacimiento"],
        descripcion=request.form["descripcion"], telefono=request.form["telefono"])
        db.session.add(new_inquilino)
        db.session.commit()
        return render_template("correcto.html")
    return render_template("inquilino.html")
#--

#----------
@app.route("/busquedas/")
def busquedas():
    return render_template("busqueda.html")

#----------
@app.route('/propietario/')
def show_owner():
    prop = request.args.get("prop")
    prop = Propietario.query.filter_by(id=prop).first_or_404()
    return render_template('show_propietario.html', prop=prop)
#----------
#----------
@app.route('/vivienda/')
def show_tenement():
    viviev = request.args.get("viviev")
    viviev = Vivienda.query.filter_by(id=viviev).first_or_404()
    return render_template('show_tenement.html', viviev=viviev)
#----------
#----------
@app.route('/agencia/')
def show_agency():
    agen = request.args.get("agen")
    agen = Agencia.query.filter_by(id=agen).first_or_404()
    return render_template('show_agency.html', agen=agen)
#----------
#----------
@app.route('/alquiler/')
def show_rental():
    rent = request.args.get("rent")
    rent = Alquiler.query.filter_by(id=rent).first_or_404()
    return render_template('show_rental.html', rent=rent)
#----------
#----------
@app.route('/inquilino/')
def show_tenant():
    tena = request.args.get("tena")
    tena = Inquilino.query.filter_by(id=tena).first_or_404()
    return render_template('show_tenant.html', tena=tena)
#----------
#--
if __name__ == "__main__":
    app.run()
#--