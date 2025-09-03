import sqlite3

def conectar():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor =  baseDeDatos.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL UNIQUE,
            descripcion TEXT NOT NULL
)
''')
    baseDeDatos.commit()
    baseDeDatos.close()

def Agregar_P( palabra,descripcion ):

 baseDeDatos = sqlite3.connect("palabras.db")
 cursor = baseDeDatos.cursor()


 cursor.execute("SELECT * FROM palabras WHERE palabra = ?", (palabra.lower(),))
 exist = cursor.fetchone()

 if exist:
     print(" Ya existe esa palabra en la base de datos.")
 else:
     cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra.lower(), descripcion))
     baseDeDatos.commit()
     print(" Palabra Agregada correctamente")
 baseDeDatos.close()

def Eliminar_P(palabra):
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()

    cursor.execute("DELETE FROM palabras WHERE palabra = ?",(palabra.lower(),))
    if cursor.rowcount > 0:
        baseDeDatos.commit()
        print("La palabra fue eliminada correctamente")
    else:
        print("⚠️ No se encontró esa palabra en la base de datos.")
    baseDeDatos.close()

def Obtener_P_A():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()
    cursor.execute("SELECT palabra,descripcion FROM palabras ORDER BY RANDOM() LIMIT 1")
    resultado = cursor.fetchone()
    baseDeDatos.close()
    return resultado

def Listar_P():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()
    cursor.execute("SELECT palabra,descripcion FROM palabras")
    datos = cursor.fetchall()
    baseDeDatos.close()
    return datos

def Dar_Pista():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()
    cursor.execute("SELECT palabra, descripcion FROM palabras ORDER BY RANDOM() LIMIT 1")
    resultado = cursor.fetchone()
    baseDeDatos.close()

    if resultado:
        palabra,descripcion = resultado
        print("PISTA:")
        print("Descripción:", descripcion)
        print("La palabra empieza con la letra :", palabra[0])

    else:
     print("No hay palabras registradas para dar pistas.")


if __name__ == "__main__":
     conectar()
     Agregar_P("Perro", "Animal doméstico conocido como el mejor amigo del hombre.")
     print("Palabra Aleatoria:", Obtener_P_A())
     Agregar_P("Gato", "Animal domestico mas que escala")
     print("Palabra Aleatoria:", Obtener_P_A())
     Dar_Pista()
     print("Lista de palabras registradas:", Listar_P())
     Eliminar_P("perro")
     print("Lista actualizada:", Listar_P())
     Dar_Pista()