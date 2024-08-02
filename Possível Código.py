import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

def generate_bode_plot():
    try:
        num = list(map(float, num_entry.get().split()))
        den = list(map(float, den_entry.get().split()))
        system = TransferFunction(num, den)
        w, mag, phase = bode(system)

        plt.figure()

        plt.subplot(2, 1, 1)
        plt.semilogx(w, mag) 
        plt.title('Bode Plot')
        plt.xlabel('Frequency [rad/s]')
        plt.ylabel('Magnitude [dB]')

        plt.subplot(2, 1, 2)
        plt.semilogx(w, phase)
        plt.xlabel('Frequency [rad/s]')
        plt.ylabel('Phase [degrees]')

        plt.tight_layout()
        plt.show()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid coefficients")

root = tk.Tk()
root.title("Bode Plot Generator")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

num_label = ttk.Label(mainframe, text="Numerator Coefficients (space-separated):")
num_label.grid(row=0, column=0, sticky=tk.W)
num_entry = ttk.Entry(mainframe, width=40)
num_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

den_label = ttk.Label(mainframe, text="Denominator Coefficients (space-separated):")
den_label.grid(row=1, column=0, sticky=tk.W)
den_entry = ttk.Entry(mainframe, width=40)
den_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

generate_button = ttk.Button(mainframe, text="Generate Bode Plot", command=generate_bode_plot)
generate_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
