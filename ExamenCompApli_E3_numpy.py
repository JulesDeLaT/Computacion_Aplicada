import numpy as np

Cantidades = np.array([[0.25, 0.15, 0], [0.45, 0.5, 0.75], [0.3, 0.35, 0.25]])
Toneladas = np.array([1.5, 5, 3])

det_Cantidades = np.linalg.det(Cantidades)
print(det_Cantidades)
# Calcular la solución para cada variable utilizando la Regla de Cramer
x = np.zeros(3)
for i in range(3):
    Ai = Cantidades.copy()
    Ai[:, i] = Toneladas
    print(np.linalg.det(Ai))
    x[i] = np.linalg.det(Ai) / det_Cantidades
    print(x[i])

print("Toneladas tipo A: ", str(round(x[0],2)))
print("Toneladas tipo B: ", str(round(x[1],2)))
print("Toneladas tipo C: ", str(round(x[2],2)))