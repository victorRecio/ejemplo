from flask import Flask, render_template, request, redirect, url_for, flash 
app = Flask(__name__)

#from flask_mysqldb import MySQL
import pymysql.cursors

db = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="1234", db="almacen"
    #esto es prueba.
)
cur = db.cursor()
"""
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'ventasDB'
mysql = MySQL(app)
"""

#settings
app.secret_key = 'mysecretkey'

def index():
    return render_template('index.html')

def add_articulo():
    if request.method == 'POST':
        print("hola")
        """
        details = request.form
        firstName = details['nomb_art']
        price_art = details['price_art']
        description = details['desc_art']"""
        #details = request.form
        firstName  = request.form['nomb_art']
        price_art  = request.form['price_art']
        description = request.form['desc_art']
        print(firstName)
        print(price_art)
        print(description)
        return redirect(url_for('index'))
        
def edit_articulo(id):
    #cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_articulos where id = %s",(id))
    data = cur.fetchallone()
    cur.close()
    flash('Articulo select Sucessfully')
    return redirect(url_for('edit_articulo.html',art = data))


def up_articulo():
    #cur = mysql.connection.cursor()
    if request.method == "POST":
        details = request.form
        firstName = details['nomb_art']
        price_art = details['price_art']
        description = details['desc_art']
        cur.execute("""
                    UPDATE tbl_articulos
                    set nombre = %s,
                        precio = %s,
                        description = %s 
                    where id = %s
                    """,(firstName, price_art, description,id)
        )
        cur.connection.commit()
        cur.close()
        flash('Articulo Update Sucessfully')
        return redirect(url_for('index'))


def delete_articulo(id):
    #cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_articulos where id = {0}",format(id))
    cur.connection.commit()
    cur.close()
    flash('Articulo Remove Sucessfully')
    return redirect(url_for('index'))


def find_articulo():
    #cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_articulos where id = {0}",format(id))
    data = cur.fetchall()
    cur.close()
    flash('Articulo Find Sucessfully')
    #return ""
    return render_template('templates/articulos.html', art = data)