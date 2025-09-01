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
  print("Ya existe esa palabra en la base de datos :v")
 else:
    cursor.execute("INSERT INTO palabras (palabra, descripcion) VALUES (?, ?)", (palabra.lower(), descripcion))
 baseDeDatos.commit()
 baseDeDatos.close()
 print("Palabra Agregada :)")

def Eliminar_P(palabra):
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()

    cursor.execute("DELETE FROM palabras WHEN palabra = ?",(palabra.lower()))
    baseDeDatos.commit()
    baseDeDatos.close()
    print("La palabra fue eliminada")

def Obtener_P_A():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()
    cursor.execute("SELECT palabra,descripcion FROM palabras ORDER BY RANDOM()LIMIT 1")
    Resultado = cursor.fetchone()
    baseDeDatos.close()
    return Resultado

def Listar_P():
    baseDeDatos = sqlite3.connect("palabras.db")
    cursor = baseDeDatos.cursor()
    cursor.execute("SELECT palabra,descripcion FROM palabras")
    datos = cursor.fetchall()
    baseDeDatos.close()
    return datos

   if __name__ == "__main__":
     conectar()
     Agregar_P("Perro", "Animal doméstico conocido como el mejor amigo del hombre.")
        print("Palabra Aleatoria:", Obtener_P_A())





