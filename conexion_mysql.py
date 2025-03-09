import mysql.connector

# Conectar a la base de datos
def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto si tienes otro usuario en MySQL
            password="",  # Pon tu contraseña si la configuraste
            database="gestion_agricola"
        )
        if conn.is_connected():
            print("✅ Conexión exitosa a MySQL")
        return conn
    except mysql.connector.Error as e:
        print(f"❌ Error conectando a MySQL: {e}")
        return None

# Probar la conexión
if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        conexion.close()
# Insertar un nuevo tratamiento en la base de datos
def insertar_tratamiento(nombre, fecha, responsable):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO tratamientos (nombre, fecha, responsable) VALUES (%s, %s, %s)"
        valores = (nombre, fecha, responsable)
        cursor.execute(sql, valores)
        conn.commit()
        print("✅ Tratamiento agregado con éxito")
        cursor.close()
        conn.close()

# Obtener todos los tratamientos
def obtener_tratamientos():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tratamientos")
        tratamientos = cursor.fetchall()
        for tratamiento in tratamientos:
            print(tratamiento)
        cursor.close()
        conn.close()
# Prueba: Insertar un tratamiento
insertar_tratamiento("Herbicida Verde", "2024-03-11", "Pedro López")
# Prueba: Listar tratamientos
obtener_tratamientos()

