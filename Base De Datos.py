import sqlite3

def Conectar():
    baseDeDatos= sqlite3.connect("Ahorcado.db")
    cursor =  baseDeDatos.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            descripcion TEXT NOT NULL)
''')
    baseDeDatos.commit()
    baseDeDatos.close()







