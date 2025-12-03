
from model.conexionBD import *

class Nota:  
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        try:
          cursor.execute(
            "insert into notas values(null,%s,%s,%s,NOW())",
            (usuario_id,titulo,descripcion)
          )
          conexion.commit()
          return True
        except:
          return False

    @staticmethod
    def mostrar(usuario_id):
        try:
          cursor.execute(
            "select * from notas where usuario_id=%s",
            (usuario_id,)
          )
          return cursor.fetchall()
        except:    
          return []

    @staticmethod
    def actualizar(id, titulo, descripcion):
       try:
         cursor.execute(
            "update notas set titulo=%s,descripcion=%s where id=%s",
            (titulo,descripcion,id)
         )
         conexion.commit()
         return True
       except: 
         return False
    
    @staticmethod
    def eliminar(id):
        try:
          cursor.execute(
            "delete from notas where id=%s",
            (id,)
          ) 
          conexion.commit() 
          return True  
        except:    
          return False
        
