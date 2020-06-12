from flask import Flask, render_template, request, redirect, url_for, flash 
app = Flask(__name__)

import pymysql.cursors
#Modulos
import ventas.articulos as Articulos

#articulos.add_articulo();

db = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="1234", db="almacen"
    #esto es prueba.
)
cur = db.cursor()

#settings
app.secret_key = 'mysecretkey'


@app.route('/', methods=['GET', 'POST'])
    Articulos.index()
    #def index():
        #return render_template('index.html')

"""A qui Todo con Respecto a la Creacion y manipulacion de articulos"""

#try:
    @app.route('/add_articulo', methods=['POST'])
        Articulos.add_articulo()
    @app.route('/edit_articulo/<id>',methods=['POST'])
        Articulos.edit_articulo()
    @app.route('/up_articulo/<id>',methods=['POST'])
        Articulos.up_articulo()
    @app.route('/delete_articulo/<string:id>',methods=['POST'])
        Articulos.delete_articulo()
    @app.route('/find_articulo',methods=['POST'])
        Articulos.find_articulo()
#except Exception as err:
    #print(err)
    #print("Ooosp! Ocurrio un error")

if __name__ == '__main__':
    app.run(port = 3000, debug = True)    
