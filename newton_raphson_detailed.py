import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, lambdify
import pandas as pd

# Definición de la función y su derivada
x = symbols('x')
f_expr = 2 * x**4 + 2 * x**3 - 3 * x**2 + 0.15
f_prime_expr = diff(f_expr, x)

# Convertir las expresiones simbólicas a funciones de Python
f = lambdify(x, f_expr, 'numpy')
f_prime = lambdify(x, f_prime_expr, 'numpy')

# Método de Newton-Raphson con 5 decimales de precisión
def newton_raphson_detailed(x0, iterations):
    details = []
    for i in range(iterations):
        f_x0 = f(x0)
        f_prime_x0 = f_prime(x0)
        details.append({
            'iteration': i + 1,
            'x0': round(x0, 5),
            'f(x0)': round(f_x0, 5),
            "f'(x0)": round(f_prime_x0, 5)
        })
        x_new = x0 - (f_x0 / f_prime_x0)
        x0 = x_new
        details[-1]['x_new'] = round(x_new, 5)
        details[-1]['f(x_new)'] = round(f(x_new), 5)
    return details

# Parámetros iniciales
x0 = 1.0
iterations = 3

# Obtener las primeras n(iterations) aproximaciones de la raíz con detalles
newton_details = newton_raphson_detailed(x0, iterations)

# Guardar los detalles en un DataFrame de pandas
newton_df = pd.DataFrame(newton_details)

# Guardar el DataFrame en un archivo de Excel
excel_path = 'Newton_Raphson_Method_Details.xlsx'
newton_df.to_excel(excel_path, index=False)

# Graficar la función y la raíz
if newton_details:
    last_x_new = newton_details[-1]['x_new']
    last_y_new = f(last_x_new)
    
    x_values = np.linspace(-1, 2, 500)
    y_values = [f(val) for val in x_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='$f(x) = 2x^4 + 2x^3 - 3x^2 + 0.15$', linewidth=2)
    plt.scatter([last_x_new], [last_y_new], color='red')
    plt.text(last_x_new, last_y_new, f'  Root ≈ {last_x_new:.5f}', fontsize=12, color='red')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Graph of the Function and its Root')
    plt.xlabel('x')
    plt.ylabel('$f(x)$')
    plt.legend()
    plt.grid(True)
    plt.show()
