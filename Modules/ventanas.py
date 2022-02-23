###Modulo de creacion de las ventanas###

# Importar tkinter para interfaz
import tkinter as tk
from tkinter import messagebox

from bd import db_init

'''Crear la base de datos'''
datab = db_init()

'''Clase ventana (general)'''
class ventana:
   #Atributos generales
   titulo: str
   ancho: int
   alto: int
   root: int

   def __init__(self,titulo,ancho,alto):
      self.titulo = titulo
      self.ancho = ancho
      self.alto = alto

   #Crear ventana base
   def crear_base(self):
      self.root = tk.Tk()
      self.root.title(self.titulo)
      x_vent = self.root.winfo_screenwidth()
      y_vent = self.root.winfo_screenheight()
      x_vent = x_vent//2 - self.ancho//2
      y_vent = y_vent//2 - self.alto//2
      position = str(self.ancho) + "x" + str(self.alto) + "+" + str(x_vent) + "+" + str(y_vent)
      self.root.geometry(position)

   #Crear ventana flotante (necesita una ventana base)
   def crear_flotante(self):
      self.root = tk.Toplevel()
      self.root.title(self.titulo)
      x_vent = self.root.winfo_screenwidth()
      y_vent = self.root.winfo_screenheight()
      x_vent = x_vent//2 - self.ancho//2
      y_vent = y_vent//2 - self.alto//2
      position = str(self.ancho) + "x" + str(self.alto) + "+" + str(x_vent) + "+" + str(y_vent)
      self.root.geometry(position)
   
   def cerrar(self):
      self.root.quit()
      self.root.destroy()

'''Clases especificas'''

#Ventana para agregar tiendas
class add_tienda(ventana):
   nombre: str
   giro: str
   ubicacion: str
   #__init__ = al de ventana
   def crear(self):
      #Crear ventana
      self.crear_flotante()

      #Crear objetos ventanas
      ##Etiquetas
      header = tk.Label(self.root, text='Agregue un nuevo establecimiento.')
      nombre_lab = tk.Label(self.root, text='Nombre: ')
      giro_lab = tk.Label(self.root, text='Giro: ')
      ubic_lab = tk.Label(self.root, text='Ubicacion: ')
      ##Cajas de texto
      nombre_txtb = tk.Entry(self.root, font='helvetica 12')
      giro_txtb = tk.Entry(self.root, font='helvetica 12')
      ubic_txtb = tk.Entry(self.root, font='helvetica 12')

      #Funcion para guardar la info de la ventana
      def save():
         nombre = nombre_txtb.get()
         giro = giro_txtb.get()
         ubicacion = ubic_txtb.get()

         if nombre == '' or giro == '' or ubicacion == '':
            messagebox.showwarning('Casillas en blanco!','Ningun espacio puede estar vacio!')
         else:
            self.nombre = nombre
            self.giro = giro
            self.ubicacion = ubicacion
            self.guardar()               
            self.cerrar()

      ##Boton para guardar
      save_but = tk.Button(self.root, text='Anadir', command=lambda: save())
   
      #Posicionar objetos
      header.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky='nesw')
      nombre_lab.grid(row=1, column=0, padx=15, pady=10)
      nombre_txtb.grid(row=1, column=1, padx=15, pady=10)
      giro_lab.grid(row=2, column=0, padx=15, pady=10)
      giro_txtb.grid(row=2, column=1, padx=15, pady=10)
      ubic_lab.grid(row=3, column=0, padx=15, pady=10)
      ubic_txtb.grid(row=3, column=1, padx=15, pady=10)
      save_but.grid(row=4, column=0, columnspan=2)

      self.root.mainloop()

   def guardar(self):
      valores = [self.nombre, self.giro, self.ubicacion]
      global datab
      datab.ins_tienda(valores)

#Ventana para agregar usuarios
class add_user(ventana):
   nombre: str
   pasw: str

   #__init__ = al de ventana
      
   def crear(self):

      self.crear_flotante()
      
      #Crear etiquetas
      header = tk.Label(self.root, text='Agregue un nuevo usuario.')
      nombre_lab = tk.Label(self.root, text='Nombre: ', anchor='e')
      pasw_lab = tk.Label(self.root, text='Contrasena: ')
      paswc_lab = tk.Label(self.root, text='Confirmar Contrasena: ')
      #Crear cajas de texto
      nombre_txtb = tk.Entry(self.root, font='helvetica 12')
      pasw_txtb = tk.Entry(self.root, font='helvetica 12', show='*')
      paswc_txtb = tk.Entry(self.root, font='helvetica 12', show='*')
      #Posicionar objetos
      header.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky='nesw')
      nombre_lab.grid(row=1, column=0, padx=15, pady=10, sticky='e')
      nombre_txtb.grid(row=1, column=1, padx=15, pady=10, sticky='w')
      pasw_lab.grid(row=2, column=0, padx=15, pady=10, sticky='e')
      pasw_txtb.grid(row=2, column=1, padx=15, pady=10, sticky='w')
      paswc_lab.grid(row=3, column=0, padx=15, pady=10, sticky='e')
      paswc_txtb.grid(row=3, column=1, padx=15, pady=10, sticky='w')

      #Funcion para almacenar la info de la ventena
      def guardar(self):
         nombre = nombre_txtb.get()
         pasw = pasw_txtb.get()
         paswc = paswc_txtb.get()

         if nombre == '' or pasw == '' or paswc == '':
            messagebox.showwarning('Casillas en blanco!','Ningun espacio puede estar vacio!')
         elif pasw != paswc:
            messagebox.showerror('Contraseñas no coinciden','Revise que la contraseña sea la misma.')
         else:
            self.nombre = nombre
            self.pasw = pasw

      #Crear y posicionar objeto de guardar
      save_but = tk.Button(self.root, text='Guardar', command = lambda: guardar)
      save_but.grid(row=4, column=1, padx=15, pady=10)
      #ver_pasw = Button(add_user.root, text='Mostrar Contrasena')
      #ver_pasw.grid(row=4, column=0, padx=15, pady=10)

      self.root.mainloop()
   
   def guardar(self):
      valores = [self.nombre,self.pasw]
      datab.ins_usuario(valores)

#Ventana principal
class main_V(ventana):
   tienda: str
   def __init__(self,titulo,ancho,alto,tienda):
      super().__init__(titulo, ancho, alto)
      self.tienda = tienda
   
   # #Si no hay tienda, se debe crear una
   # def sin_tienda(self):
   #    self.crear_base()
   #    messagebox.showinfo('Sin tienda detectada!','No hay registro de ninguna tienda aun.')
   # Esto deberia estar en crear o por separado? Si esta separada se puede llamar a lista_tiendas desde main.py
   
   #Crear ventana
   def crear(self,tienda: str,ventana_tienda: add_tienda, ventana_usuario: add_user):
      #Funcion para cambiar valor de slc
      def select(s):
         global slc
         slc = s
         if slc == 1:
            ventana_tienda.crear()
         if slc == 2:
            ventana_usuario.crear()

      if tienda == []:
         self.crear_base()
         #Si no hay tiendas notifica
         messagebox.showinfo('Sin tienda detectada!','No hay registro de ninguna tienda aun.')
         return False
      else:
         self.crear_base()

         #Crear objetos en la ventana
         header = tk.Label(self.root, text=f'PUNTO DE VENTA {self.tienda.upper()}', bg='black', fg='white', padx=601, pady=8)
         b_ventas = tk.Button(self.root, text='VENTAS F1')
         b_clientes = tk.Button(self.root, text='CLIENTES F2')
         b_productos = tk.Button(self.root, text='PRODUCTOS F3')
         b_add_user = tk.Button(self.root, text='NUEVO USUARIO', command= lambda: select(2) )
         b_add_store = tk.Button(self.root, text='NUEVA TIENDA', command= lambda: select(1))
         #Posicionar objetos
         header.grid(row=0,column=0,columnspan=4)
         b_ventas.place(x=0, y=35)
         b_clientes.place(x=68, y=35)
         b_productos.place(x=144, y=35)
         b_add_user.place(x=1106, y=35)
         b_add_store.place(x=1208, y=35)
         #Visualizar ventana

         self.root.mainloop()      


#Inicializacion y configuracion de ventanas
# main = main_V("Punto de Venta", 1300, 650, 'tienda')
# a_t = add_tienda_V("Nueva Tienda", 320, 220)
# a_u = add_user_V("Nuevo Usuario",380,220)