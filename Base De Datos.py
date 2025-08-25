import sqlite3

def ConectarBase():
    baseDeDatos = sqlite3.connect("Juego_Ahorcado.db")
    cr = baseDeDatos.cursor()
    cr.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL UNIQUE,
            descripcion TEXT NOT NULL
 )
''')
    baseDeDatos.commit()
    baseDeDatos.close()



