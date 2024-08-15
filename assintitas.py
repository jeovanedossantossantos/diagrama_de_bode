import os
import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import TransferFunction, bode

def generate_bode_plot():
    try:
        num = list(map(float, num_entry.get().split()))
        den = list(map(float, den_entry.get().split()))
        system = TransferFunction(num, den)
        w, mag, phase = bode(system)

        figura = plt.figure(figsize=(6,6),dpi=80)
        canva = FigureCanvasTkAgg(figura,root)
        canva.get_tk_widget().place(x = 10, y= 100)

        plt.subplot(2, 1, 1)
        plt.semilogx(w, mag, label='Bode Plot')
        plt.title('Gráficos')

        # Desenhando as assíntotas de magnitude
        w_asymp = np.array([w[0], w[-1]])
        mag_asymp = np.polyval(np.polyfit(np.log10(w), mag, 1), np.log10(w_asymp))
        plt.semilogx(w_asymp, mag_asymp, 'r--', label='Assíntotas de Magnitude')

        plt.xlabel('Frequência [rad/s]')
        plt.ylabel('Magnitude [dB]')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.semilogx(w, phase, label='Bode Plot')

        # Desenhando as assíntotas de fase
        phase_asymp = np.polyval(np.polyfit(np.log10(w), phase, 1), np.log10(w_asymp))
        plt.semilogx(w_asymp, phase_asymp, 'r--', label='Assíntotas de Fase')

        plt.xlabel('Frequência [rad/s]')
        plt.ylabel('Fase [Graus]')
        plt.legend()

        plt.tight_layout()
        plt.show(root)
    except ValueError:
        messagebox.showerror("Entrada Inválida", "Favor cheque os coeficientes")

root = tk.Tk()
root.title("Diagrama de Body em Python")
root.geometry("625x625")
root.resizable(False,False)
pastaApp=os.path.dirname(__file__)
img_path = os.path.join(pastaApp, "ondas.ico")
root.iconbitmap(img_path)
imgLogo = PhotoImage(file=pastaApp+"\\background.png")
l_logo=Label(root,image=imgLogo)
l_logo.place(x=0,y=0)

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

num_label = ttk.Label(mainframe, text="Coeficientes do Numerador (Separados por espaço):")
num_label.grid(row=0, column=0, sticky=tk.W)
num_entry = ttk.Entry(mainframe, width=40)
num_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

den_label = ttk.Label(mainframe, text="Coeficientes do Denominador (Separados por espaço):")
den_label.grid(row=1, column=0, sticky=tk.W)
den_entry = ttk.Entry(mainframe, width=40)
den_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

generate_button = ttk.Button(mainframe, text="Gerar Gráfico", command=generate_bode_plot)
generate_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
