from flask import Flask, render_template
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
class dato(db.Model):
    __tablename__ = 'dato'
    id_dato = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(255),nullable=False)
    direction = db.Column(db.String(255),nullable=False)
    pasatiempo = db.Column(db.String(255),nullable=False)
    id_cursos = db.Column(db.String(255),nullable=False)
    conocimientos = db.Column(db.String(255),nullable=False)
    

# def __repr__(self):
#     return '<dato %r>' % self.name_user
    
# def create_db():
#     db.create_all()
#     return 'Database created successfully'
# */
@app.route('/')
def index():
    tabla = dato.query.all()
    return render_template('index.html', tabla=tabla)

# Verificar si se ejecuta directamente este script
if __name__ == '__main__':
    app.run(debug=True)        