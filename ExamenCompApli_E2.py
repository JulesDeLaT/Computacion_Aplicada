import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.linear_model import LinearRegression as lr


df = pd.read_csv(r'C:\Users\sebas\Desktop\bci-workshop-master\python\archivo.csv')

#Medidas de tendencia
estaturaPromedio = df['Estatura'].mean()
tallaPromedio = df['Talla'].mean()
estaturaDesv = df['Estatura'].std()
tallaDesv = df['Talla'].std()

print(f'Promedio estatura: {estaturaPromedio:.2f} ')
print(f'Desviación estandar estatura: {estaturaDesv:.2f}')
print(f'Promedio talla: {tallaPromedio:.2f}')
print(f'Desviación estandar talla: {tallaDesv:.2f}')

# Ajuste Gaussiano
estaturaHist, estaturaBins = np.histogram(df['Estatura'], bins=20, density=True)
tallaHist, tallaBins = np.histogram(df['Talla'], bins=20, density=True)
estaturaValores = norm.fit(df['Estatura'])
tallaValores = norm.fit(df['Talla'])
estaturaGrafica = norm.pdf(estaturaBins[:-1], *estaturaValores)
tallaGrafica = norm.pdf(tallaBins[:-1], *tallaValores)

print(f'Mu estatura: {estaturaValores[0]:.2f}')
print(f'Sigma estatura: {estaturaValores[1]:.2f}')
print(f'Mu talla: {tallaValores[0]:.2f}')
print(f'Sigma talla: {tallaValores[1]:.2f}')

# Graficas Gaussianas e Histogramas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.hist(df['Estatura'], bins=20, density=True)
ax1.plot(estaturaBins[:-1], estaturaGrafica, 'r', lw=2)
ax1.set_xlabel('Estatura')
ax1.set_ylabel('Densidad')
ax1.set_title('Distribución de Estatura')

ax2.hist(df['Talla'], bins=20, density=True)
ax2.plot(tallaBins[:-1], tallaGrafica, 'r', lw=2)
ax2.set_xlabel('Talla')
ax2.set_ylabel('Densidad')
ax2.set_title('Distribución de Talla')

plt.show()

# Calcular la probabilidad de estar dentro de una desviación estándar
estaturaProb = norm.cdf(estaturaPromedio + estaturaDesv, estaturaPromedio, estaturaDesv) - norm.cdf(estaturaPromedio - estaturaDesv, estaturaPromedio, estaturaDesv)
tallaProb = norm.cdf(tallaPromedio + tallaDesv, tallaPromedio, tallaDesv) - norm.cdf(tallaPromedio - tallaDesv, tallaPromedio, tallaDesv)

print(f'Probabilidad estatura: {estaturaProb:.2f}')
print(f'Probabilidad talla: {tallaProb:.2f}')

#Ajuste lineal para datos completos
x = df['Estatura'].values.reshape(-1, 1)
y = df['Talla'].values.reshape(-1, 1)
modeloLineal = lr().fit(x, y)
totalR2 = modeloLineal.score(x, y)
totalCoef = modeloLineal.coef_[0][0]
totalInter = modeloLineal.intercept_

print(f'Relación lineal entre estatura y talla de calzado: y = {totalCoef:.2f}x + {float(totalInter):.2f} (R² = {totalR2:.2f})')

#Ajuste lineal para hombres y mujeres
hombresDf = df[df['Sexo'] == 'Masculino']
mujeresDf = df[df['Sexo'] == 'Femenino']

hombresX = hombresDf['Estatura'].values.reshape(-1, 1)
hombresY = hombresDf['Talla'].values.reshape(-1, 1)
modeloLinealHombres = lr().fit(hombresX, hombresY)
hombresR2 = modeloLinealHombres.score(hombresX, hombresY)
hombresCoef = modeloLinealHombres.coef_[0][0]
hombresInter = modeloLinealHombres.intercept_
print(f'Relación lineal para hombres: y = {hombresCoef:.2f}x + {float(hombresInter):.2f} (R² = {hombresR2:.2f})')

mujeresX = mujeresDf['Estatura'].values.reshape(-1, 1)
mujeresY = mujeresDf['Talla'].values.reshape(-1,1)
modeloLinealMujeres = lr().fit(mujeresX, mujeresY)
mujeresR2 = modeloLinealMujeres.score(mujeresX, mujeresY)
mujeresCoef = modeloLinealMujeres.coef_[0][0]
mujeresInter = modeloLinealMujeres.intercept_
print(f'Relación lineal para mujeres: y = {mujeresCoef:.2f}x + {float(mujeresInter):.2f} (R² = {mujeresR2:.2f})')






