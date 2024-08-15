import os
import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import TransferFunction, bode
import time

#Horário de inicialização:
print("Programa iniciado em:", time.strftime("%H:%M:%S"), time.strftime("%d/%m/%Y"))

def gera_grafico():
    global valor_check
    global figura
    try:
        num = list(map(float, num_entry.get().split()))
        den = list(map(float, den_entry.get().split()))
        system = TransferFunction(num, den)
        w, mag, phase = bode(system)

        figura = plt.figure(figsize=(6,6),dpi=80)
        canva = FigureCanvasTkAgg(figura,root)
        canva.get_tk_widget().place(x = 10, y= 100)
        
        plt.subplot(2, 1, 1)
        plt.semilogx(w, mag) 
        plt.title('Gráficos')

        plt.xlabel('Frequência [rad/s]')
        plt.ylabel('Magnitude [dB]')

        plt.subplot(2, 1, 2)
        plt.semilogx(w, phase)
        plt.xlabel('Frequência [rad/s]')
        plt.ylabel('Fase [Graus]')

        plt.tight_layout()
        canva.draw() 

    except ValueError:
        messagebox.showerror("Entrada Inválida", "Favor cheque os coeficientes")
        
    if valor_check.get() == 1:
        diretorio = filedialog.askdirectory()
        print(valor_check.get())
        if diretorio:
            nome_arquivo = filedialog.asksaveasfilename(initialdir=diretorio, defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if nome_arquivo:
                figura.savefig(nome_arquivo) 
                print("Resultado salvo com sucesso!")
            else:
                print("Salvamento cancelado.")

        
def bodecalculo():
    bodejanela =  tk.Toplevel()
    bodejanela.title("Para que serve o diagrama de Body?")
    bodejanela.geometry("1280x720")
    bodejanela.resizable(False,False)
    bodejanela.configure(bg="#333333")
    pastaApp=os.path.dirname(__file__)
    img = PhotoImage(file=pastaApp+"\\bode.png")
    label = tk.Label(bodejanela, image=img)
    label.image = img
    label.pack()

    bodejanela.mainloop()

def ajuda():
    ajudajanela =  tk.Toplevel()
    ajudajanela.title("Como usar o programa?")
    ajudajanela.geometry("1280x720")
    ajudajanela.resizable(False,False)
    ajudajanela.configure(bg="#333333")
    pastaApp=os.path.dirname(__file__)
    img = PhotoImage(file=pastaApp+"\\ajuda.png")
    label = tk.Label(ajudajanela, image=img)
    label.image = img
    label.pack()

    ajudajanela.mainloop()

root = tk.Tk()
root.title("Diagrama de Body em Python")
root.geometry("625x635")
root.resizable(False,False)
pastaApp=os.path.dirname(__file__)
img_path = os.path.join(pastaApp, "ondas.ico")
root.iconbitmap(img_path)
imgLogo = PhotoImage(file=pastaApp+"\\background.png")
l_logo=Label(root,image=imgLogo)
l_logo.place(x=0,y=0)

barrademenus=tk.Menu(root)
menuprincipal= tk.Menu(barrademenus, tearoff  = 0)
barrademenus.add_cascade(label = "Início", menu= menuprincipal)
menuprincipal.add_command(label  = "Sobre o Diagrama de Body",command=bodecalculo)
menuprincipal.add_separator()
menuprincipal.add_command(label  = "Como usar o programa?",command=ajuda)
menuprincipal.add_separator()
menuprincipal.add_command(label  = "Fechar",command=root.quit)
root.config(menu=barrademenus)

num_label = ttk.Label(root, text="Coeficientes do Numerador (Separados por espaço):",background="#1F6AA5",foreground= "#000", font = 15, width=43)
num_label.grid(row=1, column=0, sticky=tk.W)
num_entry = ttk.Entry(root, width=40)
num_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

den_label = ttk.Label(root, text="Coeficientes do Denominador (Separados por espaço):",background="#1F6AA5",foreground= "#000", font = 15)
den_label.grid(row=2, column=0, sticky=tk.W)
den_entry = ttk.Entry(root, width=40)
den_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

generate_button = ttk.Button(root, text="Gerar Gráfico", command=gera_grafico)
generate_button.grid(row=3, column=0, columnspan=2)

valor_check = tk.IntVar()
valor_check1 = tk.Checkbutton(root, text="Salvar Gráfico", variable=valor_check)
valor_check1.grid(row=4, column=0, columnspan=2)

root.mainloop()