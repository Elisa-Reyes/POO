import mysql.connector

try:
  conexion=mysql.connector.connect(
     host="127.0.0.1",
     user="root",
     password="",
     database="bd_coches"
  )
  cursor=conexion.cursor(buffered=True)
except:
    print("No fue posible conectarse con la BD")