class Nodo:
	def __init__ (self, dato):
		self.dato = dato
		self.siguiente = self.anterior = None
		
class lista:
	def __init__(self):
		self.encabezado = self.cola = None
	
	def insertarPrimerNodo(self, nuevoNodo):
		self.encabezado = self.cola = nuevoNodo
		self.encabezado.anterior = self.cola.siguiente= None
		
	def insertarNodoCola(self, dato):
		nuevoNodo = Nodo(dato)
		if self.encabezado == None:
			self.insertarPrimerNodo(nuevoNodo)
			
		else:
			self.cola.siguiente=nuevoNodo
			nuevoNodo.anterior = self.cola
			self.cola = nuevoNodo
			
		self.cola.siguiente = None
	
	def insertarInicio (self, dato):
		nuevoNodo = Nodo(dato)
		if self.encabezado == None:
			self.insertarInicio(nuevoNodo)
			
		else:
			self.encabezado.anterior = nuevoNodo
			nuevoNodo.siguiente = self.encabezado
			self.encabezado = nuevoNodo
			
	def eliminarInicio(self):
		self.anterior = self.siguiente = self.encabezado = self.cola = None
	
	def eliminarUltimo(self):
		nodo = self.cola
		if self.encabezado == None:
			print "lista Vacia"
			return
		elif self.encabezado == self.cola:
			self.eliminarInicio()
			return
		else:
			self.cola = nodo.anterior
			self.cola.siguiente = None
			
	def eliminarEncabezado(self):
		nodo = self.encabezado
		if self.encabezado == None:
			print "lista vacia"
			return
		
		if self.encabezado == self.cola:
			self.eliminarInicio()
			return
		
		if self.encabezado != self.cola:
			nodo =nodo.siguiente
			nodo.anterior = None
			self.encabezado = nodo
			
	def eliminarNodo(self, elemento):
		nodo = self.encabezado
		encontrado = False
		if self.encabezado == self.cola and self.encabezado.dato != elemento:
			print "elemento no encontrado"
			return
		if self.encabezado.dato == elemento:
			self.eliminarEncabezado()
			
		while nodo.siguiente !=None:
			if nodo.siguiente.dato == elemento:
				encontrado = True
				break
			else:
				nodo= nodo.siguiente
			
		if encontrado:
			if nodo.siguiente.siguiente != None:
				temp = nodo.siguiente
				nodo.siguiente = temp.siguiente
				nodo = temp.siguiente.anterior
				
			else:
				self.eliminarUltimo()
		else:
			print "elemento no encontrado"
			
	def mostrar(list):
		nodo = list.encabezado
		if list.encabezado == None:
			print "vacia"
			while nodo is not None:
				print "%d" %(nodo.dato)
				nodo = nodo.siguiente
				if nodo is not None:
					print "asdf"
				
		
		
		