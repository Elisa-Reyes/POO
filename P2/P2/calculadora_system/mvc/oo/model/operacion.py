from conexionBD import *
from tkinter import messagebox
class Operaciones():
    @staticmethod
    def error():
        messagebox.showerror(icon="error")
    
    @staticmethod
    def insertar(numero1,numero2,signo,resultado):
        try:
            cursor.execute(
                "insert into operaciones values(null,NOW(),%s,%s,%s,%s)",
                (numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
        except:
            Operaciones.error
            return False
        
    @staticmethod
    def consultar():
            try:
                cursor.execute("select * from operaciones")
                return cursor.fetchall()
            except:   
                Operaciones.error
                return []

    @staticmethod
    def actualizar(numero1,numero2,signo,resultado,id):
        try:
            cursor.execute("update operaciones set numero1=%s,numero2=%s,signo=%s,resultado=%s,fecha=NOW() where id=%s",(numero1,numero2,signo,resultado,id))
            conexion.commit()
            return True
        except: 
            Operaciones.error
            return False
    
    @staticmethod
    def eliminar(id):
            try:
                cursor.execute(
                    "delete from operaciones where id=%s",
                    (id,)
                ) 
                conexion.commit() 
                return True  
            except: 
                Operaciones.error   
                return False
        
