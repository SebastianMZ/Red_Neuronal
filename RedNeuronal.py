#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class RedNeuronal(object):
	"""Clase que representa RNA tipo MLP"""
	def __init__(self, X, y, capasOcultas):
		super(RedNeuronal, self).__init__()
		#Datos de Entrada
		self.X = X
		#Datos de Salida
		self.y = y

		#Numero de Capas
		self.num_capas = len(capasOcultas) + 2
		#Tamanos de la RNA
		self.tamanos = [(np.shape(self.X)[1])] + self.num_capas + [(np.shape(self.y)[1])]
		self.construir_red()

	def construir_red():
		#Lista de matrices de pesos que toman cada salida de una capa a la salida
		self.pesos = []
		#Vectos Bias (Umbral) para cada capa
		self.bias = []
		#Vector de Entradas para cada capa
		self.entradas = []
		#Vectos de salidas de cada capa
		self.salidas = []
		#Vector de errores de cada capa
		self.errores = []

		for capa in range(self.num_capas-1):
			num_neuronasn = self.tamanos[capa]
			num_neuronasm = self.tamanos[capa+1]

			self.pesos.append(np.random.normal(0,1 (m,n)))
			self.bias.append(np.random.normal(0,1, (m,1)))
			self.entradas.append(np.zeros((n,1)))
			self.salidas.append(np.zeros((n,1)))
			self.errores.append(np.zeros((n,1)))

		#Es necesario completar las entradas, salidas y errores de la ultima capa
		self.entradas.append(np.zeros((n,1)))
		self.salidas.append(np.zeros((n,1)))
		self.errores.append(np.zeros((n,1)))





