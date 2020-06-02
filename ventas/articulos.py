from flask import Flask, render_template, request, redirect, url_for, flash 
app = Flask(__name__)

#from flask_mysqldb import MySQL
import pymysql.cursors

conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="1234", db="almacen"
)
cur = conn.cursor()
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


@app.route('/')
def hello_world():
    return 'Hola amigos de Geeky Theory!'
    
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    #cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbl_articulos')
    data = cur.fetchall()
    return render_template("articulos.html", art = data)
"""
app.route('/add_articulo',methods=['POST'])
def add_articulo():
    if request.method == "POST":
        details = request.form
        firstName = details['nomb_art']
        price_art = details['price_art']
        description = details['desc_art']

        #cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_articulos(nombre, precio, description) VALUES (%s, %s)", (firstName, price_art, desc_art))
        mysql.connection.commit()
        cur.close()
        flash('Articulo added Sucessfully')
        return redirect(url_for('index'))

@app.route('/edit_articulo/<id>',methods=['POST'])
def edit_articulo(id):
    #cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_articulos where id = %s",(id))
    data = cur.fetchallone()
    cur.close()
    flash('Articulo select Sucessfully')
    return redirect(url_for('edit_articulo.html',art = data))

@app.route('/up_articulo/<id>',methods=['POST'])
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
                    """,(firstName, price_art, desc_art,id)
        )
        mysql.connection.commit()
        cur.close()
        flash('Articulo Update Sucessfully')
        return redirect(url_for('index'))

@app.route('/delete_articulo/<string:id>',methods=['POST'])
def delete_articulo(id):
    #cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_articulos where id = {0}",format(id))
    mysql.connection.commit()
    cur.close()
    flash('Articulo Remove Sucessfully')
    return redirect(url_for('index'))

@app.route('/find_articulo',methods=['POST'])
def find_articulo():
    #cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_articulos where id = {0}",format(id))
    data = cur.fetchall()
    cur.close()
    flash('Articulo Find Sucessfully')
    return ""
    #return render_template('templates/articulos.html', art = data)
    

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
