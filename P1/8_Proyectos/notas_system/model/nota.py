from conexionBD import *
class Notas():
    @staticmethod
    def crear(usuario_id,titulo,descripcion,fecha):
        try:
            cursor.execute(
                "insert into notas values(null,%s,%s,%s,%s)",
                (usuario_id,titulo,descripcion,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar(usuario_id):
            try:
                cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
                return cursor.fetchall()
            except:    
                return []

    @staticmethod
    def actualizar(titulo,descripcion,fecha,id):
        try:
            cursor.execute("update notas set titulo=%s,descripcion=%s,fecha=%s where id=%s",(titulo,descripcion,fecha,id))
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
        
