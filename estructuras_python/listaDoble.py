class Nodo ():
	
	def __init__(self, dato, anterior, siguiente):
		self.dato = dato
		self.anterior = anterior
		self.siguiente = siguiente
		
		
class ListaDoble():
	
	def __init__(self):
		encabezado =None
		cola = None
	
	def append(self, dato):
		nuevoNodo = Nodo(dato, None, None)
		if self.encabezado is None:
			self.encabezado = self.cola = nuevoNodo
		else:
			nuevoNodo.anterior = self.cola
			nuevoNodo.siguiente = None
			self.cola.siguiente = nuevoNodo
			self.cola = nuevoNodo
			
	def borrar(self, valuarNodo):
		current_nodo=self.encabezado
		
		while current_nodo is not None:
			if current_nodo.dato == valuarNodo:
				if current_nodo.anterior is not None:
					current_nodo.anterior.siguiente = current_nodo.siguiente
					current_nodo.siguiente.anterior = current_nodo.anterior
				else:
					self.encabezado = current_nodo.siguiente
					current_nodo.siguiente.anterior = None
					
			current_nodo = current_nodo.siguiente
			
	def mostrar(self):
		print "mostrar lista de datos"
		current_nodo = self.encabezado
		while current_nodo is not None:
			"""current_nodo mostrara el dato del nodo"""
			print current_nodo.anterior.dato if hasattr(current_nodo.anteriorm, "dato") else None,
			print current_nodo.dato
			print current_nodo.siguiente.dato if hasattr(current_nodo.siguiente, "dato") else None
			
			current_nodo = current_nodo.siguiente
	
			