## Identificación de Imágenes con Red de Hopfield

Este proyecto implementa un prototipo de red neuronal de Hopfield para identificar y corregir la posición de un aro "C" dentro de una matriz binaria, incluso cuando la imagen presenta desplazamiento o ruido.

## Descripción

Se entrena una red de Hopfield con la forma ideal del aro centrado. Luego se presenta una versión descentrada (1 unidad hacia arriba y 2 a la derecha) y con ruido aleatorio. La red es capaz de recuperar el patrón original y ubicar el centro del aro.

---

## Contenido del Repositorio

| Archivo                         | Descripción                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| `tp3_hopfield_identificador.py` | Script principal con la red de Hopfield y visualización del proceso.       |
| `README.md`                     | Descripción general del proyecto.                                          |

---

## Cómo ejecutar

### Requisitos:
- Python 3.x
- Numpy
- Scipy
- Matplotlib

### Ejecución:
```bash
python tp3_hopfield_identificador.py
```

El programa mostrará tres imágenes:
1. Aro descentrado.
2. Aro descentrado con ruido.
3. Aro recuperado con centro detectado.

---

## Ejemplo

Centro estimado del aro C: `X=5.60`, `Y=4.30`  
Se visualiza la imagen corregida con un punto rojo en el centro.

---

## Autor

Ivan Bustamante  
Trabajo práctico para la materia de Inteligencia Artificial - Módulo 3  
2025

