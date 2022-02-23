###Modulo que controla la base de datos###

import sqlite3
#Crear variables del modulo
class db():
   connection: int
   cursor: int
   
   def __init__(self):
      self.connection = sqlite3.connect('PDV.db')
      self.cursor = self.connection.cursor()

   '''Definicion e inicializacion de la base de datos'''
   def iniciar_db(self):
      #Crear la tabla tiendas
      self.cursor.execute("CREATE TABLE IF NOT EXISTS tiendas(nombre VARCHAR(30), giro VARCHAR(30), ubicacion VARCHAR(60))")
      #Crear la tabla usuarios
      self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(ID_Personal INTEGER, nombre VARCHAR(30), pasw VARCHAR(20))")
      self.connection.commit()

   '''Consultas'''
   def lista_tienda(self):
      self.cursor.execute("SELECT * FROM tiendas")
      lista_tiendas = list(self.cursor.fetchall())
      tiendas=[]

      #Revisar cantidad y convertir tuple a lista
      if len(lista_tiendas) == 0:
         pass
      elif len(lista_tiendas) == 1:
         for i in range(len(lista_tiendas)):
            tiendas.append(lista_tiendas[i])
      else:
         for i in range(len(lista_tiendas)):
            tmp=[]
            for j in range(len(lista_tiendas[i])):
               tmp.append(lista_tiendas[i][j])
            tiendas.append(tmp)
      
      return tiendas

   def lista_usuarios(self):
      self.cursor.execute("SELECT * FROM usuarios")
      usuarios = self.cursor.fetchall()
      return usuarios

   '''Inserts'''
   def ins_tienda(self,tienda): #0: nombre, 1: giro, 2: ubicacion
      self.cursor.execute("INSERT INTO tiendas VALUES(?,?,?)",(tienda[0],tienda[1],tienda[2]))
      self.connection.commit()
      
   def ins_usuario(self,usuario): #0: nombre, 1: psw
      self.cursor.execute("INSERT INTO usuarios VALUES(?,?,?)",(usuario[0],usuario[1]))
      self.connection.commit()

   '''Updates'''

   '''Deletes'''
   def del_tienda(self,tienda):
      self.cursor.execute(f"DELETE FROM tiendas WHERE nombre = {tienda}")
      self.connection.commit()

   def del_usuario(self,usuario):
      self.cursor.execute(f"DELETE FROM usuarios WHERE nombre = {usuario}")
      self.connection.commit()

def db_init():
   manager = db()
   manager.iniciar_db()
   return manager
