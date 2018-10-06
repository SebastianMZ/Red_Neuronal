import numpy as np
import RedNeuronal as rna


def test_regresion():
	#Primero se crean los datos
	n = 200
	X = np.linspace(0, 3*np,pi, num=n)
	X.shape=(n,1)
	#Datos Esperados
	y = np.sin(X)

	#Evaluaremos las red con distintas Tasas de Aprendizaje
	tasas =[0.1, 0.05, 0.025]
	predicciones = []

	for tasa in tasas:
		redNeuronal = rna.RedNeuronal(X, y, [20, 20])
		#Entrenamos a la Red Neuronal
		redNeuronal.train(3678, tasa_aprendizaje=tasa)

		predicciones.append([tasa, redNeuronal.predecir(X)])

		fig, ax = plt.subplots(1,1)
		if plots:
			ax.plot(X, y, label='Seno', linewidth=2, color='black')
			for datos in predicciones:
				ax.plot(X, datos[1], label='Learning Rate: ' +str(datos[0]))
