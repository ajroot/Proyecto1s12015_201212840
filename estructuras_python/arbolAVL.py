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
o cualquier modificacion al arbol"""
	

