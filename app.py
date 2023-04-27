import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

#from sqlalchemy.sql import func

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#        'sqlite:///' + os.path.join(basedir, 'database.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    nombre = db.Column(db.String(50))
    numero = db.Column(db.String(30))
    asesor = db.Column(db.String(20))

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

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        print(request.form)
        return 'Thank you for your responses!'
    else:
        return 'Solicite un codigo a su asesor'# render_template('survey.html')


@app.route('/cliente/<uuid>', methods=['GET', 'POST'])
def survey2(uuid):
    # para entregar el formulario debo comprobar que ya no fue llenado antes... eso primero deberia comprobar!
    rentries_count = Respuestas.query.filter(Respuestas.id == uuid).count()
    #print("rentries_count is ",rentries_count)
    # aca primero busco si existe el entry con el uuid requerido... si no, digo que no hay y chau
    if (rentries_count == 0):
        tentries = T.query.filter(T.id == uuid).all()
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




