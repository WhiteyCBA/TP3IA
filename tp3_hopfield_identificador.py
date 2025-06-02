
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import center_of_mass

# Activación binaria
def sign(x):
    return np.where(x >= 0, 1, -1)

# Entrenamiento Hebbiano
def entrenar_hebbs(patrones):
    n = patrones.shape[1]
    W = np.zeros((n, n))
    for p in patrones:
        W += np.outer(p, p)
    np.fill_diagonal(W, 0)
    return W / patrones.shape[0]

# Recuperación
def recuperar_patron(W, entrada, pasos=5):
    x = entrada.copy()
    for _ in range(pasos):
        x = sign(W @ x)
    return x

# Patrón original (centrado)
aro = np.array([
    [0,0,1,1,1,1,1,0,0,0],
    [0,1,-1,-1,-1,-1,-1,1,0,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [1,-1,0,0,0,0,0,-1,1,0],
    [0,1,-1,-1,-1,-1,-1,1,0,0],
    [0,0,1,1,1,1,1,0,0,0]
])

# Crear versión desplazada (descentrada)
descentrado = np.roll(aro, shift=2, axis=1)

# Aplanar y entrenar
patron = aro.flatten()
W = entrenar_hebbs(np.array([patron]))

# Introducir ruido en la imagen descentrada
entrada = descentrado.flatten()
np.random.seed(42)
indices = np.random.choice(len(entrada), size=20, replace=False)
entrada[indices] *= -1

# Recuperar patrón
recuperado = recuperar_patron(W, entrada)
rec_matrix = recuperado.reshape(10, 10)

# Calcular centro
y, x = center_of_mass(rec_matrix == 1)
print(f"Centro estimado del aro C: X={x:.2f}, Y={y:.2f}")

# Mostrar: descentrado, con ruido, recuperado centrado
plt.figure(figsize=(10, 3))
plt.subplot(1, 3, 1)
plt.imshow(descentrado, cmap='gray')
plt.title('Descentrado')

plt.subplot(1, 3, 2)
plt.imshow(entrada.reshape(10,10), cmap='gray')
plt.title('Con ruido')

plt.subplot(1, 3, 3)
plt.imshow(rec_matrix, cmap='gray')
plt.scatter([x], [y], color='red')
plt.title('Recuperado + Centro')

plt.tight_layout()
plt.show()
