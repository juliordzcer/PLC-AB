
import time
import threading
import matplotlib.pyplot as plt

class TankControlSystem:
    def __init__(self):
        # Entradas y salidas
        self.start = False
        self.reset = False
        self.stop = False
        
        self.tank_flow_meter = 0.0
        self.tank_level_meter = 0.0
        
        self.tank_fill_valve = 0.0
        self.tank_discharge_valve = 0.0
        
        # Configuración del PID
        self.setpoint = 50.0  # Nivel deseado (porcentaje)
        self.kp = 1.0
        self.ki = 0.1
        self.kd = 0.05
        
        self.integral = 0.0
        self.previous_error = 0.0
        
        # Semáforo
        self.semaphore = {"green": False, "yellow": False, "red": False}
        
        # Datos para graficar
        self.time_data = []
        self.setpoint_data = []
        self.level_data = []
        self.error_data = []
        self.start_time = time.time()
    
    def pid_controller(self):
        """Calcula la acción de control usando un controlador PID."""
        error = self.setpoint - self.tank_level_meter
        self.integral += error
        derivative = error - self.previous_error
        
        # PID output
        pid_output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        
        return pid_output, error
    
    def update_semaphore(self):
        """Actualiza el estado del semáforo basado en el estado del sistema."""
        if self.stop:
            self.semaphore = {"green": False, "yellow": False, "red": True}  # Sistema detenido
        elif self.reset:
            self.semaphore = {"green": False, "yellow": True, "red": False}  # Sistema reiniciando
        elif self.start:
            self.semaphore = {"green": True, "yellow": False, "red": False}  # Sistema funcionando
    
    def run(self):
        """Lógica principal del sistema de control."""
        while not self.stop:
            if self.start:
                # Calcular acción de control
                control_action, error = self.pid_controller()
                
                # Controlar las válvulas basadas en la acción del PID
                self.tank_fill_valve = max(0.0, min(100.0, control_action))
                self.tank_discharge_valve = max(0.0, min(100.0, -control_action))
                
                # Actualizar el nivel del tanque (simulación)
                self.tank_level_meter += (self.tank_fill_valve - self.tank_flow_meter) * 0.1
                self.tank_level_meter = max(0.0, min(100.0, self.tank_level_meter))
                
                # Almacenar datos para gráficas
                current_time = time.time() - self.start_time
                self.time_data.append(current_time)
                self.setpoint_data.append(self.setpoint)
                self.level_data.append(self.tank_level_meter)
                self.error_data.append(error)
            
            if self.reset:
                # Reiniciar los valores
                self.tank_fill_valve = 0.0
                self.tank_discharge_valve = 0.0
                self.tank_level_meter = 0.0
                self.integral = 0.0
                self.previous_error = 0.0
                self.reset = False
            
            # Actualizar el semáforo
            self.update_semaphore()
            
            # Simular un retardo del sistema
            time.sleep(0.1)
    
    def plot_results(self):
        """Genera las gráficas de los resultados."""
        plt.figure(figsize=(10, 6))
        
        # Gráfica del setpoint y el nivel del tanque
        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.setpoint_data, label="Setpoint", linestyle="--")
        plt.plot(self.time_data, self.level_data, label="Nivel del Tanque")
        plt.title("Nivel del Tanque vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Nivel (%)")
        plt.legend()
        plt.grid()
        
        # Gráfica del error
        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.error_data, label="Error", color="red")
        plt.title("Error vs Tiempo")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Error (%)")
        plt.legend()
        plt.grid()
        
        plt.tight_layout()
        plt.show()


# Crear y ejecutar el sistema de control
if __name__ == "__main__":
    tank_system = TankControlSystem()
    
    # Iniciar los hilos para el control
    control_thread = threading.Thread(target=tank_system.run)
    control_thread.start()
    
    try:
        # Simulación por un tiempo definido
        simulation_time = 20  # Segundos
        start_time = time.time()
        while time.time() - start_time < simulation_time:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Simulación interrumpida.")
    
    # Detener el sistema
    tank_system.stop = True
    control_thread.join()
    
    # Generar las gráficas
    tank_system.plot_results()
