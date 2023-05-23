import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Connection credentials
db_user = 'usuario'
db_pass = 'pa55wort0_'
db_name = 'encuesta2023'

# configuring our database uri
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@localhost/{dbname}".format(
        username=db_user, password=db_pass, dbname=db_name)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

db = SQLAlchemy(app)

class Encuestados(db.Model):
    __tablename__ = 'encuestados'
    id = db.Column(db.String(36), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(30), nullable=False)
    asesor = db.Column(db.String(50), nullable=False)

class Respuestas(db.Model):
    __tablename__ = "respuestas"
    id = db.Column(db.String(36), primary_key=True)
    ip = db.Column(db.String(16), nullable=False)
    respuesta1 = db.Column(db.Integer, nullable=True)
    respuesta2 = db.Column(db.Integer, nullable=True)
    respuesta3 = db.Column(db.Integer, nullable=True)
    respuesta4 = db.Column(db.Integer, nullable=True)
    respuesta5 = db.Column(db.Integer, nullable=True)
    respuesta6 = db.Column(db.Integer, nullable=True)
    respuesta7 = db.Column(db.Integer, nullable=True)
    respuesta8 = db.Column(db.Integer, nullable=True)
    respuesta9 = db.Column(db.Integer, nullable=True)
    respuesta10 = db.Column(db.Integer, nullable=True)
    respuesta11 = db.Column(db.Integer, nullable=True)
    respuesta12 = db.Column(db.Integer, nullable=True)
    respuesta13 = db.Column(db.Integer, nullable=True)
    respuesta14 = db.Column(db.Integer, nullable=True)
    respuesta15 = db.Column(db.Integer, nullable=True)
    sugerencias = db.Column(db.String(1000), nullable=True)
    productos_usuales = db.Column(db.String(500), nullable=True)
    productos_sugeridos = db.Column(db.String(500), nullable=True)
    nombre = db.Column(db.String(50), nullable=False)
    whatsapp = db.Column(db.String(10), nullable=False)
    vendedor = db.Column(db.String(50), nullable=False)

class EncuestadosInterna(db.Model):
    __tablename__ = 'encuestados_interna'
    id = db.Column(db.String(10), primary_key=True)

class RespuestasInterna(db.Model):
    __tablename__ = "respuestas_interna"
    id = db.Column(db.String(10), primary_key=True)
    ip = db.Column(db.String(16), nullable=False)
    area = db.Column(db.String(30), nullable=False)
    antiguedad = db.Column(db.Integer, nullable=False)
    respuesta1 = db.Column(db.Integer, nullable=True)
    respuesta2 = db.Column(db.Integer, nullable=True)
    respuesta3 = db.Column(db.Boolean, nullable=True)
    respuesta4 = db.Column(db.Boolean, nullable=True)
    respuesta5 = db.Column(db.Boolean, nullable=True)
    respuesta6 = db.Column(db.Boolean, nullable=True)
    respuesta7 = db.Column(db.Boolean, nullable=True)
    respuesta8 = db.Column(db.Boolean, nullable=True)
    respuesta9 = db.Column(db.Boolean, nullable=True)
    respuesta10 = db.Column(db.Boolean, nullable=True)
    respuesta11 = db.Column(db.Integer, nullable=True)
    respuesta12 = db.Column(db.Integer, nullable=True)
    respuesta13 = db.Column(db.Integer, nullable=True)
    respuesta14 = db.Column(db.Integer, nullable=True)
    respuesta15 = db.Column(db.Integer, nullable=True)
    respuesta16 = db.Column(db.Boolean, nullable=True)
    respuesta17 = db.Column(db.Boolean, nullable=True)
    respuesta18 = db.Column(db.Boolean, nullable=True)
    respuesta19 = db.Column(db.Boolean, nullable=True)
    respuesta20 = db.Column(db.String(30), nullable=True)
    respuesta21 = db.Column(db.Boolean, nullable=True)
    respuesta22 = db.Column(db.Integer, nullable=True)
    respuesta23 = db.Column(db.Integer, nullable=True)
    respuesta24 = db.Column(db.Integer, nullable=True)
    respuesta25 = db.Column(db.Integer, nullable=True)
    respuesta26 = db.Column(db.Integer, nullable=True)
    respuesta27 = db.Column(db.Integer, nullable=True)
    respuesta28 = db.Column(db.Integer, nullable=True)
    respuesta29 = db.Column(db.Integer, nullable=True)
    respuesta30 = db.Column(db.Integer, nullable=True)
    respuesta31 = db.Column(db.Integer, nullable=True)
    respuesta32 = db.Column(db.Integer, nullable=True)
    respuesta33 = db.Column(db.Integer, nullable=True)
    respuesta34 = db.Column(db.Integer, nullable=True)
    respuesta35 = db.Column(db.Boolean, nullable=True)
    respuesta36 = db.Column(db.Integer, nullable=True)
    respuesta37 = db.Column(db.Integer, nullable=True)
    respuesta38 = db.Column(db.Integer, nullable=True)
    respuesta39 = db.Column(db.Integer, nullable=True)
    respuesta40 = db.Column(db.Integer, nullable=True)
    respuesta41 = db.Column(db.Integer, nullable=True)
    respuesta42 = db.Column(db.Integer, nullable=True)
    respuesta43 = db.Column(db.Integer, nullable=True)
    respuesta44 = db.Column(db.Boolean, nullable=True)
    respuesta45 = db.Column(db.Integer, nullable=True)
    respuesta46 = db.Column(db.Integer, nullable=True)
    respuesta47 = db.Column(db.Integer, nullable=True)
    respuesta48 = db.Column(db.Integer, nullable=True)
    respuesta49 = db.Column(db.Integer, nullable=True)
    respuesta50 = db.Column(db.Integer, nullable=True)
    respuesta51 = db.Column(db.Integer, nullable=True)
    respuesta52 = db.Column(db.Integer, nullable=True)
    respuesta53 = db.Column(db.Boolean, nullable=True)
    respuesta54 = db.Column(db.Boolean, nullable=True)
    respuesta55 = db.Column(db.Boolean, nullable=True)
    respuesta56 = db.Column(db.Integer, nullable=True)
    respuesta57 = db.Column(db.Integer, nullable=True)
    mejoras = db.Column(db.String(500), nullable=True)
    aquienascender = db.Column(db.String(500), nullable=True)
    aquiendespedir = db.Column(db.String(500), nullable=True)
    comentarios = db.Column(db.String(500), nullable=True)
    nombre = db.Column(db.String(50), nullable=True)

with app.app_context():
    db.create_all()

#@app.route('/', methods=['GET', 'POST'])
#def survey():
#    if request.method == 'POST':
#        print(request.form)
#        return 'Thank you for your responses!'
#    else:
#        return 'Solicite un codigo a su asesor'# render_template('survey.html')
#

@app.route('/interna', methods=['GET', 'POST'])
def interna_main():
    if request.method == 'POST':
        return redirect('/interna/'+request.form['codigo'].lower())

    return (
    '''
    <html>
    <head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
	<title>Encuesta interna</title>
	<link rel="stylesheet" href={{url_for('static', filename='style.css')}}>
    </head>

    <body><form method="post">
    <input type="text" placeholder="Ingrese su código" name="codigo" required>
    <input type="submit" value="Empezar">
    </form></body></html>
    '''
    )

@app.route('/interna/<uuid>', methods=['GET', 'POST'])
def interna(uuid):
    # compruebo que ese id existe y no se uso todavia
    rentries_count = RespuestasInterna.query.filter(RespuestasInterna.id == uuid).count()
    if (rentries_count == 0):
        tentries = EncuestadosInterna.query.filter(EncuestadosInterna.id == uuid).all()
        if len(tentries) == 1:
            if request.method == 'POST':
                f = request.form

                def respuesta(n):
                    return None if f['pregunta'+str(n)] == "null" else f['pregunta'+str(n)]
                def respuesta_bool(n):
                    return None if f['pregunta'+str(n)] == "null" else (f['pregunta'+str(n)] == "y")

                nueva_respuesta_interna = RespuestasInterna(
                        id=escape(uuid),
                        ip=request.remote_addr,
                        area=escape(f['area']),
                        antiguedad=escape(f['antiguedad']),
                        respuesta1=respuesta(1),
                        respuesta2=respuesta(2),
                        respuesta3=respuesta_bool(3),
                        respuesta4=respuesta_bool(4),
                        respuesta5=respuesta_bool(5),
                        respuesta6=respuesta_bool(6),
                        respuesta7=respuesta_bool(7),
                        respuesta8=respuesta_bool(8),
                        respuesta9=respuesta_bool(9),
                        respuesta10=respuesta_bool(10),
                        respuesta11=respuesta(11),
                        respuesta12=respuesta(12),
                        respuesta13=respuesta(13),
                        respuesta14=respuesta(14),
                        respuesta15=respuesta(15),
                        respuesta16=respuesta_bool(16),
                        respuesta17=respuesta_bool(17),
                        respuesta18=respuesta_bool(18),
                        respuesta19=respuesta_bool(19),
                        respuesta20=escape(f['pregunta20']),
                        respuesta21=respuesta_bool(21),
                        respuesta22=respuesta(22),
                        respuesta23=respuesta(23),
                        respuesta24=respuesta(24),
                        respuesta25=respuesta(25),
                        respuesta26=respuesta(26),
                        respuesta27=respuesta(27),
                        respuesta28=respuesta(28),
                        respuesta29=respuesta(29),
                        respuesta30=respuesta(30),
                        respuesta31=respuesta(31),
                        respuesta32=respuesta(32),
                        respuesta33=respuesta(33),
                        respuesta34=respuesta(34),
                        respuesta35=respuesta_bool(35),
                        respuesta36=respuesta(36),
                        respuesta37=respuesta(37),
                        respuesta38=respuesta(38),
                        respuesta39=respuesta(39),
                        respuesta40=respuesta(40),
                        respuesta41=respuesta(41),
                        respuesta42=respuesta(42),
                        respuesta43=respuesta(43),
                        respuesta44=respuesta_bool(44),
                        respuesta45=respuesta(45),
                        respuesta46=respuesta(46),
                        respuesta47=respuesta(47),
                        respuesta48=respuesta(48),
                        respuesta49=respuesta(49),
                        respuesta50=respuesta(50),
                        respuesta51=respuesta(51),
                        respuesta52=respuesta(52),
                        respuesta53=respuesta_bool(53),
                        respuesta54=respuesta_bool(53),
                        respuesta55=respuesta_bool(53),
                        respuesta56=respuesta(56),
                        respuesta57=respuesta(57),
                        mejoras=escape(f['mejoras']),
                        aquienascender=escape(f['aquienascender']),
                        aquiendespedir=escape(f['aquiendespedir']),
                        comentarios=escape(f['comentarios']),
                        nombre=escape(f['nombre']))

                db.session.add(nueva_respuesta_interna)
                db.session.commit()
                db.session.close()

                return '<p>Gracias por su tiempo! Tendremos en cuenta sus respuestas</p>'
            else:
                return render_template('interna.html')
        else:
            return "<p>Error, codigo invalido.<br>Solicite uno nuevo por favor</p>"
    else:
        return "<p>El formulario ya fue completado.<br>Si esto es un error, comunicate al <a href=\"https://api.whatsapp.com/send?phone=595992297486\">(whatsapp) 0992297486</a></p>"






@app.route('/cliente/<uuid>', methods=['GET', 'POST'])
def survey2(uuid):
    # para entregar el formulario debo comprobar que ya no fue llenado antes... eso primero deberia comprobar!
    rentries_count = Respuestas.query.filter(Respuestas.id == uuid).count()
    #print("rentries_count is ",rentries_count)
    # aca primero busco si existe el entry con el uuid requerido... si no, digo que no hay y chau
    if (rentries_count == 0):
        tentries = Encuestados.query.filter(Encuestados.id == uuid).all()
        if len(tentries) == 1:
            print('the id is', tentries[0].id)  # it works
            if request.method == 'POST':
                # guardar aca informacion de la base de datos!
                # (aca tengo los resultados del cliente ya :D)
                f = request.form
                print(request.form)

                def respuesta(n):
                    return None if f['pregunta'+str(n)] == "null" else f['pregunta'+str(n)]

                nueva_respuesta = Respuestas(
                        id=escape(uuid),
                        ip=request.remote_addr,
                        respuesta1=respuesta(1),
                        respuesta2=respuesta(2),
                        respuesta3=respuesta(3),
                        respuesta4=respuesta(4),
                        respuesta5=respuesta(5),
                        respuesta6=respuesta(6),
                        respuesta7=respuesta(7),
                        respuesta8=respuesta(8),
                        respuesta9=respuesta(9),
                        respuesta10=respuesta(10),
                        respuesta11=respuesta(11),
                        respuesta12=respuesta(12),
                        respuesta13=respuesta(13),
                        respuesta14=respuesta(14),
                        respuesta15=respuesta(15),
                        sugerencias=escape(f['sugerencias']),
                        productos_usuales=escape(f['productos-solicitados']),
                        productos_sugeridos=escape(f['productos-sugeridos']),
                        nombre=escape(f['cliente']),
                        whatsapp=escape(f['telefono']),
                        vendedor=escape(f['vendedor']))

                db.session.add(nueva_respuesta)
                db.session.commit()
                db.session.close()

                return '<p>Gracias por su tiempo! Tendremos en cuenta sus respuestas</p>'
            else:
                return render_template('survey.html')
        else:
            return "<p>Error, codigo invalido.<br>Solicite uno nuevo por favor</p>"
    else:
        return "<p>El formulario ya fue completado.<br>Si esto es un error, comunicate al <a href=\"https://api.whatsapp.com/send?phone=595992297486\">(whatsapp) 0992297486</a></p>"

if __name__ == '__main__':
    app.run(debug=True)




