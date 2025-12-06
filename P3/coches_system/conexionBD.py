import mysql.connector
from tkinter import messagebox

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_operaciones_basicas'
    )
    #Crear un objeto de tipo cursor que se pueda reutilizar nuevamente
    cursor=conexion.cursor(buffered=True)
except:
    messagebox.showinfo(message="no se pudo conectar")