import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraRaizCuadrada:
    def __init__(self, numero: float):
        self.numero = numero

    def calcular_raiz(self) -> float:
        if self.numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.numero)

# Función para manejar la lógica de la interfaz
def calcular_raiz():
    try:
        numero = float(entry_numero.get())
        calculadora = CalculadoraRaizCuadrada(numero)
        resultado = calculadora.calcular_raiz()
        label_resultado.config(text=f"Raíz cuadrada: {resultado:.4f}")
    except ValueError as e:
        messagebox.showerror("Entrada inválida", str(e))
    except Exception:
        messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Raíz Cuadrada")

# Crear y colocar los widgets
label_numero = tk.Label(root, text="Número:")
label_numero.grid(row=0, column=0, padx=10, pady=10)

entry_numero = tk.Entry(root)
entry_numero.grid(row=0, column=1, padx=10, pady=10)

button_calcular = tk.Button(root, text="Calcular Raíz", command=calcular_raiz)
button_calcular.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="Raíz cuadrada:")
label_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()

