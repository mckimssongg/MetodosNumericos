# Script completo para resolver el problema usando el método de la falsa posición

import matplotlib.pyplot as plt
import numpy as np
from math import log, tan

# Definición de la función
def f(x):
    return log(x + 1) + tan(2 * x)

# Método de la falsa posición con 5 decimales de precisión
def false_position_detailed(a, b, iterations):
    details = []
    f_a = f(a)
    f_b = f(b)
    
    # Verificar si hay una raíz en el intervalo
    if f_a * f_b >= 0:
        print("No se puede asegurar que haya una raíz en el intervalo dado.")
        return None
    
    # Realizar iteraciones
    for i in range(iterations):
        # Guardar detalles de la iteración actual
        details.append({
            'iteration': i + 1,
            'a': round(a, 5),
            'b': round(b, 5),
            'f(a)': round(f_a, 5),
            'f(b)': round(f_b, 5)
        })
        
        x_new = b - ((f_b * (a - b)) / (f_a - f_b))
        f_new = f(x_new)
        
        # Actualizar los valores de a o b
        if f_a * f_new < 0:
            b = x_new
            f_b = f_new
        else:
            a = x_new
            f_a = f_new
        
        # Guardar x_new y f(x_new) en los detalles de la iteración
        details[-1]['x_new'] = round(x_new, 5)
        details[-1]['f(x_new)'] = round(f_new, 5)
    
    return details

# Parámetros iniciales
a = 1.0
b = 1.5
iterations = 3

# Obtener las primeras 3 aproximaciones de la raíz con detalles
x_new_values_details = false_position_detailed(a, b, iterations)

# Método de la falsa posición
def false_position(a, b, iterations):
    x_new_values = []
    f_a = f(a)
    f_b = f(b)
    
    # Verificar si hay una raíz en el intervalo
    if f_a * f_b >= 0:
        print("No se puede asegurar que haya una raíz en el intervalo dado.")
        return None
    
    # Realizar iteraciones
    for i in range(iterations):
        x_new = b - ((f_b * (a - b)) / (f_a - f_b))
        f_new = f(x_new)
        
        # Actualizar los valores de a o b
        if f_a * f_new < 0:
            b = x_new
            f_b = f_new
        else:
            a = x_new
            f_a = f_new
        
        x_new_values.append(x_new)
    
    return x_new_values

# Parámetros iniciales
a = 1.0
b = 1.5
iterations = 3

# Obtener las primeras 3 aproximaciones de la raíz
x_new_values = false_position(a, b, iterations)

# Graficar la función y la raíz
if x_new_values:
    x_values = np.linspace(1, 1.5, 500)
    y_values = [f(x) for x in x_values]
    last_x_new = x_new_values[-1]
    last_y_new = f(last_x_new)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='$f(x) = \ln(x + 1) + \\tan(2x)$', linewidth=2)
    plt.scatter([last_x_new], [last_y_new], color='red')
    plt.text(last_x_new, last_y_new, f'  Root ≈ {last_x_new:.5f}', fontsize=12, color='red')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Graph of the Function and its Root')
    plt.xlabel('x')
    plt.ylabel('$f(x)$')
    plt.legend()
    plt.grid(True)
    plt.show()

# Imprimir las aproximaciones de la raíz
print(f"Las primeras {iterations} aproximaciones de la raíz son: {x_new_values}")
