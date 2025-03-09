from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

# Conectar a MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Cambia esto si tienes otro usuario
        password="",  # Pon tu contraseña si la configuraste
        database="gestion_agricola"
    )

# Ruta principal: Mostrar tratamientos
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tratamientos")
    tratamientos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tratamientos=tratamientos)

# Ruta para agregar tratamientos
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    responsable = request.form['responsable']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tratamientos (nombre, fecha, responsable) VALUES (%s, %s, %s)",
        (nombre, fecha, responsable)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 🔴 ***Mover esta función arriba*** 🔴
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tratamientos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# 🔹 Esto debe estar al final
if __name__ == '__main__':
    app.run(debug=True)


