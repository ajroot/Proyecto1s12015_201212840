class Nodo:
"""Clase nodo de arbol"""

def _init_(self,key):
	"""Constructor _init_ self llamada a si mismo"""
	self.izquierdo=None
	self.derecho=None
	self.key=key
	
def _str_(self):
	return "%s" % self.key