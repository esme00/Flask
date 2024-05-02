from flask import Flask, render_template,  request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy   # type: ignore

# Configurar la aplicación Flask
app = Flask(__name__)

# # # Configurar la conexión a la base de datos SQL Server
# # # Cambia 'driver', 'server', 'database', 'username' y 'password' por los valores adecuados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:esmeralda!@ESME/datos?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # Inicializar la extensión SQLAlchemy con la aplicación Flask
db = SQLAlchemy()
db.init_app(app)

# # # Definir un modelo de tabla para los datos
# # # Definir un modelo de tabla para los datos
class Dato(db.Model):
    __tablename__ = 'dato'
    id_dato = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(255),nullable=False)
    direction = db.Column(db.String(255),nullable=False)
    pasatiempo = db.Column(db.String(255),nullable=False)
    id_cursos = db.Column(db.String(255),nullable=False)
    conocimientos = db.Column(db.String(255),nullable=False)
    
@app.route('/agregar_dato', methods=['POST'])
def agregar_dato():
    if request.method == 'POST':
        if request.is_json:
            datos = request.json
        else:
            datos = request.form

        name_user = datos.get('name_user')
        password = datos.get('password')
        genero = datos.get('genero')
        direction = datos.get('direction')
        pasatiempo = datos.get('pasatiempo')
        id_cursos = datos.get('id_cursos')
        conocimientos = datos.get('conocimientos')

        nuevo_dato = Dato(name_user=name_user, password=password, genero=genero, direction=direction, pasatiempo=pasatiempo, id_cursos=id_cursos, conocimientos=conocimientos)

        db.session.add(nuevo_dato)
        db.session.commit()

        return jsonify({'mensaje': 'Dato agregado correctamente'}), 201

@app.route('/eliminar_dato', methods=['POST'])
def eliminar_dato():
    if request.method == 'POST':
        dato_id = request.form['dato_id']
        dato = Dato.query.get(dato_id)
        if dato:
            db.session.delete(dato)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return jsonify({'mensaje': 'El dato no existe'}), 404  

@app.route('/')
def index():
    tabla = Dato.query.all()
    return render_template('index.html', tabla=tabla)

# Verificar si se ejecuta directamente este script
if __name__ == '__main__':
    app.run(debug=True)        