import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Tiempo de simulación
t = np.linspace(0, 10, 1000)

# Parámetros del sistema (para un sistema de primer orden simplificado)
K = 1.0  # Ganancia del sistema
tau = 1.0  # Constante de tiempo

# Definición de sistemas para los distintos controladores

# Controlador proporcional (P)
Kp = 1.0
system_P = lti([Kp * K], [tau, 1])

# Controlador proporcional-derivativo (PD)
Kd = 0.5
system_PD = lti([Kp * K, Kd], [tau, 1])

# Controlador proporcional-integral (PI)
Ki = 0.5
system_PI = lti([Kp * K, Ki], [tau, 1])

# Controlador proporcional-integral-derivativo (PID)
# El PID se puede representar correctamente con una transferencia de segundo orden
system_PID = lti([Kp * K, Ki, Kd], [tau, 1])  # Mantén el denominador balanceado

# Configuración de la figura
plt.figure(figsize=(12, 8))

# Respuesta para el controlador Proporcional (P)
t_out, y_out_P = step(system_P, T=t)
plt.subplot(2, 2, 1)
plt.plot(t_out, y_out_P, label="Control Proporcional (P)", color='blue')
plt.title("Control Proporcional (P)")
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='Valor final')
plt.legend()
plt.grid()

# Respuesta para el controlador Proporcional Derivativo (PD)
t_out, y_out_PD = step(system_PD, T=t)
plt.subplot(2, 2, 2)
plt.plot(t_out, y_out_PD, label="Control Proporcional Derivativo (PD)", color='red')
plt.title("Control Proporcional Derivativo (PD)")
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='Valor final')
plt.legend()
plt.grid()

# Respuesta para el controlador Proporcional Integral (PI)
t_out, y_out_PI = step(system_PI, T=t)
plt.subplot(2, 2, 3)
plt.plot(t_out, y_out_PI, label="Control Proporcional Integral (PI)", color='green')
plt.title("Control Proporcional Integral (PI)")
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='Valor final')
plt.legend()
plt.grid()

# Respuesta para el controlador Proporcional Integral Derivativo (PID)
t_out, y_out_PID = step(system_PID, T=t)
plt.subplot(2, 2, 4)
plt.plot(t_out, y_out_PID, label="Control Proporcional Integral Derivativo (PID)", color='purple')
plt.title("Control Proporcional Integral Derivativo (PID)")
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='Valor final')
plt.legend()
plt.grid()

# Ajustar espaciado entre subgráficas
plt.tight_layout()
plt.suptitle("Respuesta de un Sistema con Diferentes Tipos de Control", fontsize=16, y=1.02)
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import lti, step

# # Configuración de parámetros del sistema
# wn = 1.0  # Frecuencia natural (rad/s)

# # Tiempo para la simulación
# t = np.linspace(0, 10, 1000)

# # Valores de amortiguamiento
# zeta_values = {
#     "Sobreamortiguado (ζ > 1)": 1.5,
#     "Críticamente amortiguado (ζ = 1)": 1.0,
#     "Subamortiguado (0 < ζ < 1)": 0.5,
#     "Sin amortiguamiento (ζ = 0)": 0.0,
# }

# # Configuración de la figura
# plt.figure(figsize=(12, 8))

# # Generar y graficar cada caso
# for i, (label, zeta) in enumerate(zeta_values.items(), 1):
#     # Sistema de segundo orden
#     system = lti([wn**2], [1, 2 * zeta * wn, wn**2])
#     t_out, y_out = step(system, T=t)
    
#     # Graficar
#     plt.subplot(2, 2, i)
#     plt.plot(t_out, y_out, label=f'ζ = {zeta}')
#     plt.title(label)
#     plt.xlabel('Tiempo (s)')
#     plt.ylabel('Respuesta')
#     plt.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='Valor final')
#     plt.legend()
#     plt.grid()

# # Ajustar espaciado entre subgráficas
# plt.tight_layout()
# plt.suptitle("Ejemplo de Respuestas de un Sistema de Segundo Orden", fontsize=16, y=1.02)
# plt.show()



# # Selección de amortiguamiento subamortiguado
# zeta = 0.5
# system = lti([wn**2], [1, 2 * zeta * wn, wn**2])

# # Calcular la respuesta al escalón
# t_out, y_out = step(system, T=t)

# # Parámetros clave para anotar
# final_value = 1.0  # Valor final esperado
# overshoot = (y_out.max() - final_value) / final_value * 100  # Sobreimpulso (%)
# time_to_peak = t_out[np.argmax(y_out)]  # Tiempo al pico
# settling_time_tolerance = 0.02  # Tolerancia para tiempo de establecimiento
# settling_time = t_out[np.where(np.abs(y_out - final_value) <= settling_time_tolerance * final_value)[0][0]]
# rise_time_indices = np.where((y_out >= 0.1 * final_value) & (y_out <= 0.9 * final_value))
# rise_time = t_out[rise_time_indices[0][-1]] - t_out[rise_time_indices[0][0]]

# # Graficar la respuesta subamortiguada con anotaciones
# plt.figure(figsize=(10, 6))

# # Respuesta
# plt.plot(t_out, y_out, label='Respuesta', color='blue')
# # Setpoint
# plt.axhline(final_value, color='gray', linestyle='--', linewidth=0.8, label='Valor final')  
# # Tolerancia
# plt.axhline(final_value + settling_time_tolerance * final_value, color='orange', linestyle='--', linewidth=0.8, label='±2% Tolerancia')
# plt.axhline(final_value - settling_time_tolerance * final_value, color='orange', linestyle='--', linewidth=0.8)


# # Anotaciones para parámetros clave

# # Sobreimpulso
# plt.scatter(time_to_peak, y_out.max(), color='red', label='Pico máximo (Mp)')
# plt.axvline(time_to_peak, color='red', linestyle='--', linewidth=0.8)
# # Codigo del texto
# plt.annotate(f'Sobreimpulso: {overshoot:.1f}%', (time_to_peak, y_out.max()), xytext=(time_to_peak + 0.6, y_out.max()), 
#              arrowprops=dict(arrowstyle='->'), fontsize=10, color='red')


# plt.annotate('Tiempo de establecimiento (ts)', (settling_time, final_value), xytext=(settling_time + 1, final_value - 0.2),
#              arrowprops=dict(arrowstyle='->'), fontsize=10, color='orange')
# plt.axvline(settling_time, color='orange', linestyle='--', linewidth=0.8)

# plt.annotate('Tiempo de subida (tr)', (t_out[rise_time_indices[0][0]], y_out[rise_time_indices[0][0]]), 
#              xytext=(t_out[rise_time_indices[0][0]] + 0.5, y_out[rise_time_indices[0][0]] + 0.2),
#              arrowprops=dict(arrowstyle='->'), fontsize=10, color='green')

# plt.axvline(t_out[rise_time_indices[0][0]], color='green', linestyle='--', linewidth=0.8)
# plt.axvline(t_out[rise_time_indices[0][-1]], color='green', linestyle='--', linewidth=0.8)
# plt.fill_betweenx([0, final_value], t_out[rise_time_indices[0][0]], t_out[rise_time_indices[0][-1]], color='green', alpha=0.1, label='Tiempo de subida')

# # Configuración de la gráfica
# plt.title('Análisis de Respuesta Subamortiguada')
# plt.xlabel('Tiempo (s)')
# plt.ylabel('Respuesta')
# plt.legend()
# plt.grid()
# plt.show()