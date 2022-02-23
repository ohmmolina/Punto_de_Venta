import ventanas as v

lst_tiendas = v.datab.lista_tienda()

if lst_tiendas == []:
   nombre_tienda = []
else:
   nombre_tienda = lst_tiendas[0][0]

principal = v.main_V("Punto de Venta", 1300, 650, nombre_tienda)
add_t = v.add_tienda("Nueva Tienda", 320, 220)
add_u = v.add_user("Nuevo Usuario",380,220)

if principal.crear(lst_tiendas,add_t,add_u) == False:
   add_t.crear()
   nombre_tienda = v.datab.lista_tienda()
   nombre_tienda = nombre_tienda[0][0]
   print(type(nombre_tienda))
   principal.cerrar()
   principal.crear(nombre_tienda,add_t,add_u)