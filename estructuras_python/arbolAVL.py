class arbolAVL():

def _init_(self):"""_init_ es para inicializar (constructor)"""
		self.nodo=None
		self.altura=-1
		self.balance=0

def insertar(self,key):
	"""Insertar"""
	n=Nodo(key)
	
	"""para el primer arbolAVL"""
	if self.nodo== None:
		self.nodo=n
		self.nodo.izquierdo=arbolAVL()
		self.nodo.derecho=arbolAVL()
		"""Insertar llave en subarbol izquierdo"""
	elif key < self.nodo.key:
		self.nodo.izquierdo.insertar(key)
	"""insertar llave en subarbol derecho"""
	elif key < self.nodo.key:
		self.nodo.derecho.insertar(key)
		
		"""la llave fue insertada y existe en el arbol"""
		
		"""Rebalancear"""
		self.rebalance()
		

def rebalance(self):
"""rebalancear el arbol siempre despues de eliminar, insertar
o cualquier modificacion al arbol
------ primero hay que chequear si es necesario rebalancear
"""
	self.actualizar_alturas(recursivo=False)
	self.actualizar_balance(False)
	"""chequear cada nodo  si el factor de balance esta entre
	-1 0 1 no necesita rotacion"""
	while self.balance < -1 or self.balance > 1:
		"""subarbol izquierdo mayor que subarbol derecho"""
		if self.balance > 1:
		"""caso izquierda derecha rotar y,z a la izquierda"""
			if self.nodo.balance.izquierdo < 0:
				self.nodo.izquierdo.rotarizquierda()
				self.actualizar_alturas()
				self.actualizar_balance()
				
			self.rotarderecha()
			self.actualizar_alturas()
			actualizar_balance()
		#verificar si el subarbol derecho es mayor al izquierdo
		if self.balance < -1:
			#caso derecha izquierda rotar x,z a derecha
			if self.nodo.derecho.balance > 0:
			self.nodo.derecho.rotarderecha()
			self.actualizar_alturas()
			self.actualizar_balance()
		
		self.rotarizquierda()
		self.actualizar_alturas()
		self.actualizar_balance()

def actualizar_alturas(self recursivo=True):
	"""actualizar las alturas del arbol, la altura maxima es cuando
	la altura mayor es +1"""
	if self.nodo:
		if recursivo:
			if self.nodo.izquierdo:
				self.nodo.izquierdo.actualizar_alturas()
			if self.nodo.derecho:
				self.nodo.derecho.actualizar_alturas()
				
		self.altura=1+max(self.nodo.izquierdo.altura,self.nodo.derecho.altura)
	else:
		self.altura=-1
		
		
			

