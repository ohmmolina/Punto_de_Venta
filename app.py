import time
import sqlite3
'''Creando la db'''
connection = sqlite3.connect('PDV.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tiendas(nombre VARCHAR(30), giro VARCHAR(30), ubicacion VARCHAR(60))")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(ID_Personal INTEGER, nombre VARCHAR(30), pasw VARCHAR(20))")
connection.commit()

'''Creando la interfaz grafica'''
from tkinter import *
from tkinter import messagebox

'''VENTANAS'''
#Nueva ventana
def new_win(tipo='', titulo='', width=320, height=220):
   if tipo == 't':
      win = Tk()
   else:
      win = Toplevel()
   win.title(titulo)
   #Tamano de la ventana y centrada
   x_vent = win.winfo_screenwidth()
   y_vent = win.winfo_screenheight()
   ancho_vent = width
   alto_vent = height
   x_vent = x_vent//2 - ancho_vent//2
   y_vent = y_vent//2 - alto_vent//2
   position = str(ancho_vent) + "x" + str(alto_vent) + "+" + str(x_vent) + "+" + str(y_vent)
   win.geometry(position)
   return win

def add_store(tipo='', f=''):
   a_store = new_win(tipo,'Nueva Tienda')
   
   cursor.execute("SELECT * FROM usuarios")
   user = cursor.fetchall()
   cursor.execute("SELECT * FROM tiendas")
   store = cursor.fetchall()

   def save_store():
      nombre = nombre_txtb.get().upper()
      giro = giro_txtb.get()
      ubic = ubic_txtb.get()
      if nombre == '' or giro == '' or ubic == '':
         messagebox.showerror('Error','Ningun campo puede estar vacio.')
      elif nombre in store:
         messagebox.showerror('Error','Establecimiento ya registrado!')
      else:
         cursor.execute("INSERT INTO tiendas VALUES(?,?,?)",(nombre,giro,ubic))
         connection.commit()
         if user == []:
            add_user(a_store)
         elif f == '':
            main(a_store)
         else:
            a_store.destroy()


   header = Label(a_store, text='Agregue un nuevo establecimiento.')
   nombre_lab = Label(a_store, text='Nombre: ')
   giro_lab = Label(a_store, text='Giro: ')
   ubic_lab = Label(a_store, text='Ubicacion: ')

   nombre_txtb = Entry(a_store, font='helvetica 12')
   giro_txtb = Entry(a_store, font='helvetica 12')
   ubic_txtb = Entry(a_store, font='helvetica 12')

   save_but = Button(a_store, text='Anadir', command= lambda: save_store())
   
   header.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky='nesw')
   nombre_lab.grid(row=1, column=0, padx=15, pady=10)
   nombre_txtb.grid(row=1, column=1, padx=15, pady=10)
   giro_lab.grid(row=2, column=0, padx=15, pady=10)
   giro_txtb.grid(row=2, column=1, padx=15, pady=10)
   ubic_lab.grid(row=3, column=0, padx=15, pady=10)
   ubic_txtb.grid(row=3, column=1, padx=15, pady=10)
   save_but.grid(row=4, column=0, columnspan=2)
   
   if store == []:
      a_store.update()
      messagebox.showinfo('Sin tienda detectada!','No hay registro de ninguna tienda aun.')
   
   a_store.mainloop()
def add_user(close='',f=''):
   if close != '':
      close.destroy()

   cursor.execute("SELECT * FROM usuarios")
   user = cursor.fetchall()
   cursor.execute("SELECT * FROM tiendas")
   store = cursor.fetchall()

   a_user = new_win('t','Nuevo Usuario',380)

   if user == []:
      usuario = StringVar(a_user)
      usuario.set('admin')
      psw = StringVar(a_user)
      psw.set('admin')
      psw1 = StringVar(a_user)
      psw1.set('admin')
   else:
      usuario=''
      psw=''
      psw1=''

   def save_user():
      nombre = nombre_txtb.get()
      pasw = pasw_txtb.get()
      paswc = paswc_txtb.get()
      if nombre in user:
         messagebox.showerror('Error','El usuario ya existe.')
      elif pasw != paswc:
         messagebox.showerror('Error','Contrasenas no coinciden.')
      else:
         cursor.execute("SELECT * FROM usuarios")
         usuarios = cursor.fetchall()
         if user == []:
            id_ = 0
         else:
            id_=len(usuarios)
         cursor.execute("INSERT INTO usuarios VALUES(?,?,?)",(id_,nombre,pasw))
         connection.commit()
      if f == '':
         main(a_user)
      elif f == 'main':
         a_user.destroy()

   header = Label(a_user, text='Agregue un nuevo usuario.')
   nombre_lab = Label(a_user, text='Nombre: ', anchor='e')
   pasw_lab = Label(a_user, text='Contrasena: ')
   paswc_lab = Label(a_user, text='Confirmar Contrasena: ')

   nombre_txtb = Entry(a_user, font='helvetica 12', textvariable=usuario)
   pasw_txtb = Entry(a_user, font='helvetica 12', show='*', textvariable=psw1)
   paswc_txtb = Entry(a_user, font='helvetica 12', show='*', textvariable=psw)

   header.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky='nesw')
   nombre_lab.grid(row=1, column=0, padx=15, pady=10, sticky='e')
   nombre_txtb.grid(row=1, column=1, padx=15, pady=10, sticky='w')
   pasw_lab.grid(row=2, column=0, padx=15, pady=10, sticky='e')
   pasw_txtb.grid(row=2, column=1, padx=15, pady=10, sticky='w')
   paswc_lab.grid(row=3, column=0, padx=15, pady=10, sticky='e')
   paswc_txtb.grid(row=3, column=1, padx=15, pady=10, sticky='w')

   save_but = Button(a_user, text='Guardar', command= lambda: save_user())
   save_but.grid(row=4, column=1, padx=15, pady=10)
   #ver_pasw = Button(a_user, text='Mostrar Contrasena')
   #ver_pasw.grid(row=4, column=0, padx=15, pady=10)

   if user == []:
      a_user.update()
      messagebox.showinfo('Sin Usuarios','No hay usuarios registrados aun.')

   a_user.mainloop()
def main(close='',tienda='',usuario=''):
   if close != '':
      close.destroy()

   cursor.execute("SELECT * FROM usuarios")
   user = cursor.fetchall()
   cursor.execute("SELECT * FROM tiendas")
   store = cursor.fetchall()

   if tienda == '':
      tienda = store[0][0]
   if usuario =='':
      usuario = user[0][0]
   root = new_win('t',f'{tienda}',1300,700)
   


   header = Label(root, text=f'PUNTO DE VENTA {tienda}', bg='black', fg='white',padx=1300)
   #fecha y hora 1,0
   ahora = time.strftime('%d/%b/%y %H:%M')
   fecha_hora = Label(root, text=ahora, bg='black', fg='white',padx=1300) #no actualiza
   #boton ventas 2
   b_ventas = Button(root, text='VENTAS F1')
   #boton clientes 2
   b_clientes = Button(root, text='CLIENTES F2')
   #boton productos 2
   b_productos = Button(root, text='PRODUCTOS F3')
   #boton corte 2
   #boton agregar usuario 2
   b_add_user = Button(root, text='NUEVO USUARIO', command= lambda: add_user(f='main'))
   #boton seleccionar usuario 2
   #boton agregar tienda 2
   b_add_store = Button(root, text='NUEVA TIENDA', command= lambda: add_store(f='main'))
   #boton seleccionar tienda 2
   #etiquta 'Codigo del producto:' 3
   #entrada de busqueda de codigo 3
   #boton agregar producto 3
   #boton buscar 4
   #boton entradas 4
   #boton salidas 4
   #boton borra articulo 4
   #frame de ventas??
   #boton cambiar comanda
   #boton pendiente
   #boton eliminar comanda
   #boton cobrar
   #etiquetas de ultimo ticket + botones Frame??

   
   header.grid(row=0,column=0,columnspan=4)
   fecha_hora.grid(row=1,column=0,columnspan=4)
   b_ventas.place(x=0, y=42)
   b_clientes.place(x=68, y=42)
   b_productos.place(x=144, y=42)
   b_add_user.place(x=1106, y=42)
   b_add_store.place(x=1208, y=42)

   root.columnconfigure(0,weight=1)
   root.mainloop()

'''FRAMES'''

'''CONTROLES DE VISION DE VENTANAS'''

'''MAIN'''

cursor.execute("SELECT * FROM usuarios")
user = cursor.fetchall()
cursor.execute("SELECT * FROM tiendas")
store = cursor.fetchall()
if len(store) == 1: #Solo una tienda --> slct_user o add_user --> main
   main()
elif store == []:   #No hay tienda --> add_store --> slct_user o add_user --> main
   add_store('t')
else:                 #Mas de una tienda --> slct_store --> slct_user o add_user --> main
   print('else')
