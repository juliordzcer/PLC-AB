import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Configuración de parámetros del sistema
wn = 1.0  # Frecuencia natural (rad/s)

# Tiempo para la simulación
t = np.linspace(0, 10, 1000)


# Selección de amortiguamiento subamortiguado
zeta = 0.5
system = lti([wn**2], [1, 2 * zeta * wn, wn**2])

# Calcular la respuesta al escalón
t_out, y_out = step(system, T=t)

# Parámetros clave para anotar
final_value = 1.0  # Valor final esperado
overshoot = (y_out.max() - final_value) / final_value * 100  # Sobreimpulso (%)
time_to_peak = t_out[np.argmax(y_out)]  # Tiempo al pico
settling_time_tolerance = 0.02  # Tolerancia para tiempo de establecimiento
settling_time = t_out[np.where(np.abs(y_out - final_value) <= settling_time_tolerance * final_value)[0][0]]
rise_time_indices = np.where((y_out >= 0.1 * final_value) & (y_out <= 0.9 * final_value))
rise_time = t_out[rise_time_indices[0][-1]] - t_out[rise_time_indices[0][0]]

# Graficar la respuesta subamortiguada con anotaciones
plt.figure(figsize=(10, 6))

# Respuesta
plt.plot(t_out, y_out, label='Process Value:PV', color='blue')
# Setpoint
plt.axhline(final_value, color='black', linestyle='--', linewidth=0.8, label='Setpoint:SP')  
# Tolerancia
plt.axhline(final_value + settling_time_tolerance * final_value, color='gray', linestyle='--', linewidth=0.8, label='Deadband:DB')
plt.axhline(final_value - settling_time_tolerance * final_value, color='gray', linestyle='--', linewidth=0.8)


# Anotaciones para parámetros clave

# Sobreimpulso

plt.axvline(time_to_peak, color='red', linestyle='--', linewidth=0.8)
# Codigo del texto
plt.annotate(f'Sobreimpulso', (time_to_peak, y_out.max()), xytext=(time_to_peak + 1, y_out.max()), 
             arrowprops=dict(arrowstyle='->'), fontsize=15, color='red')


plt.annotate('Tiempo de establecimiento', (9, final_value), xytext=(5, final_value - 0.2),
             arrowprops=dict(arrowstyle='->'), fontsize=15, color='orange')
plt.axvline(8, color='orange', linestyle='--', linewidth=0.8)
plt.axvline(10, color='orange', linestyle='--', linewidth=0.8)



plt.annotate('Tiempo de subida', (2.4185, 1), 
             xytext=(0.2, 1.1),
             arrowprops=dict(arrowstyle='->'), fontsize=15, color='green')

plt.axvline(0, color='green', linestyle='--', linewidth=0.8)
plt.axvline(2.4185, color='green', linestyle='--', linewidth=0.8)


plt.fill_betweenx([0, 1], 0, 2.4185, color='green', alpha=0.1, label='Tiempo de subida')
plt.fill_betweenx([.98, 1.02], 8, 10, color='orange', alpha=0.1, label='Tiempo de establecimiento')



# Puntos
plt.scatter(time_to_peak, y_out.max(), color='red')
plt.scatter(2.4185, 1, color='green')


# Configuración de la gráfica
plt.title('Análisis de Respuesta')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.legend(loc='lower right')  # La leyenda está bien ubicada
plt.xlim(0, t_out[-1])  # Asegura que el eje x empiece en 0
plt.ylim(0, max(y_out) * 1.1)  # Asegura que el eje y empiece en 0 y tenga espacio adicional
# plt.grid()
plt.show()


# # Encuentra los índices donde ocurre el cruce por el valor 1
# crossing_indices = np.where(np.diff(np.sign(y_out - final_value)))[0]

# # Interpolación lineal para determinar el tiempo exacto de cruce
# crossing_times = []
# for idx in crossing_indices:
#     t1, t2 = t_out[idx], t_out[idx + 1]
#     y1, y2 = y_out[idx], y_out[idx + 1]
#     crossing_time = t1 + (final_value - y1) * (t2 - t1) / (y2 - y1)
#     crossing_times.append(crossing_time)

# # Imprime los tiempos de cruce
# print("Tiempos en que la respuesta cruza por 1:", crossing_times)
