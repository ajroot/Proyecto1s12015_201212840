# -*- coding: utf-8 -*-


class Nodo():
	def __init__(self,key):
		"""Constructor _init_ self llamada a si mismo"""
		self.izquierdo=None
		self.derecho=None
		self.key=key
	
	def __str__(self):
		return "%s" % self.key
	
	def __repr__(self):
		return str(self.key)


class arbolAVL():

	def __init__(self):
			self.nodo = None
			self.altura = -1
			self.balance = 0

	def insertar(self,key):
		"""Insertar"""
		n=Nodo(key)
		
		"""para el primer arbolAVL"""
		if not self.nodo:
			self.nodo = n
			self.nodo.izquierdo = arbolAVL()
			self.nodo.derecho = arbolAVL()
			"""Insertar llave en subarbol izquierdo"""
		elif key < self.nodo.key:
			self.nodo.izquierdo.insertar(key)
		elif key > self.nodo.key:
			self.nodo.derecho.insertar(key)
			
			"""la llave fue insertada y existe en el arbol"""
			
			"""Rebalancear"""
			self.rebalance()
			

	def rebalance(self):
		self.actualizar_alturas(recursivo=False)
		self.actualizar_balance(False)
		"""chequear cada nodo  si el factor de balance esta entre
		-1 0 1 no necesita rotacion"""
		while self.balance < -1 or self.balance > 1:
			"""subarbol izquierdo mayor que subarbol derecho"""
			if self.balance > 1:
				if self.nodo.izquierdo.balance < 0:
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

	def actualizar_alturas(self, recursivo = True):
		"""actualizar las alturas del arbol, la altura maxima es cuando
		la altura mayor es +1"""
		if self.nodo:
			if recursivo:
				if self.nodo.izquierdo:
					self.nodo.izquierdo.actualizar_alturas()
				if self.nodo.derecho:
					self.nodo.derecho.actualizar_alturas()
					
			self.altura = 1 + max(self.nodo.izquierdo.altura,self.nodo.derecho.altura)
		else:
			self.altura=-1
			
	def actualizar_balance(self, recursivo = True):
		if self.nodo:
			if recursivo:
				if self.nodo.izquierdo:
					self.nodo.izquierdo.actualizar_balance()
				if self.nodo.derecho:
					self.nodo.derecho.actualizar_balance()
					
			self.balance=self.nodo.izquierdo.altura - self.nodo.derecho.altura
		else:
			self.balance=0
		
	def rotarderecha(self):
			nuevaRaiz = self.nodo.izquierdo.nodo
			nuevo_izquierdo_sub = nuevaRaiz.derecho.nodo
			viejaRaiz = self.nodo

			self.nodo = nuevaRaiz
			viejaRaiz.izquierdo.nodo = nuevo_izquierdo_sub
			nuevaRaiz.derecho.nodo = viejaRaiz
			
	def rotarizquierda (self):
		"""rotar izquierda"""
		nuevaRaiz = self.nodo.derecho.nodo
		nuevo_izquierdo_sub = nuevaRaiz.izquierdo.nodo
		viejaRaiz = self.nodo
		
		self.nodo = nuevaRaiz
		viejaRaiz.derecho.nodo = nuevo_izquierdo_sub
		nuevaRaiz.izquierdo.nodo = viejaRaiz

	def borrar (self, key):
		if self.nodo != None:
			if self.nodo.key == key:
				if not self.nodo.izquierdo.nodo and not self.nodo.derecho.nodo:
					self.nodo = None
				elif not self.nodo.izquierdo.nodo:
					self.nodo = self.nodo.derecho.nodo
				elif not self.nodo.derecho.nodo:
					self.nodo = self.nodo.izquierdo.nodo
				else:
					sucesor= self.nodo.derecho.nodo
					while sucesor and sucesor.izquierdo.nodo:
						sucesor = sucesor.izquierdo.nodo
						
					if sucesor:
						self.nodo.key = sucesor.key
						
						self.nodo.derecho.borrar(sucesor.key)
			
			elif key < self.nodo.key:
				self.nodo.izquierdo.borrar(key)
				
			elif key > self.nodo.key:
				self.nodo.derecho.borrar(key)
				
			self.rebalance()
			
	def recorrerEnOrden(self):
		result = []

		if not self.nodo:
			return result
			
		result.extend(self.nodo.izquierdo.recorrerEnOrden())
		result.append(self.nodo.key)
		result.extend(self.nodo.derecho.recorrerEnOrden())
		
		return result
		
	def mostrar(self, nodo=None, nivel = 0):
		if not nodo:
			nodo = self.nodo
		
		if nodo.derecho.nodo:
			self.mostrar(nodo.derecho.nodo, nivel + 1)
			print ('\t' * nivel), ('     \\')
		
		print ('\t' * nivel), nodo
		
		if nodo.izquierdo.nodo:
			print ('\t' * nivel), ('   \\')
			self.mostrar(nodo.izquierdo.nodo, nivel + 1)
		