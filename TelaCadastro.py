from cachorro import Cachorro
from gato import Gato
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


lista=[]
def cadastroAnimal():
    nome=entryNome.get()
    idade=entryIdade.get()
    raca=entryRaca.get()
    porte=entryPorte.get()
    tipo=varTipo.get()

    if tipo=="Cachorro":
        if nome=="":
            messagebox.showinfo("Erro", "Modelo deve ser preenchido")
        c=Cachorro(nome, idade, porte)
        salvar(c)
    else:
        g=Gato(nome, idade, raca)
        salvar(g)
    messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso")

def salvar(obj):
    lista.append(obj)

def atualizarListabox():
        listbox.delete(0, tk.END)
        for obj in lista:
            listbox.insert(tk.END, obj.mostrar())

janela = tk.Tk()
janela.title("Cadastro de animais")
janela.geometry("800x300")


janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row = 0, column = 0, sticky = "nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista")

label1=tk.Label(tab1, text="Nome:", font=("",15))
label1.grid(row=1, column=0, sticky="w", padx=10)

entryNome=tk.Entry(tab1, font=("",15))
entryNome.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label2=tk.Label(tab1, text="Idade:", font=("",15))
label2.grid(row=2, column=0, sticky="w", padx=15)

entryIdade=tk.Entry(tab1, font=("",15))
entryIdade.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

label3=tk.Label(tab1, text="Raça:", font=("",15))
label3.grid(row=3, column=0, sticky="w", padx=10)

entryRaca=tk.Entry(tab1, font=("",15))
entryRaca.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

label4=tk.Label(tab1, text="Porte:", font=("",15))
label4.grid(row=4, column=0, sticky="w", padx=10)

entryPorte=tk.Entry(tab1, font=("",15))
entryPorte.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo", font=("", 15)).grid(row=0, column=0, sticky='w', padx=10)
varTipo = tk.StringVar(value="Cachorro")
tk.Radiobutton(tab1, text="Cachorro", font=("", 15), variable=varTipo, value="Cachorro").grid(row=0, column=1, sticky='w', padx=10)

tk.Label(tab1, text="Tipo", font=("", 15)).grid(row=0, column=0, sticky='w', padx=10)
tk.Radiobutton(tab1, text="Gato", font=("", 15), variable=varTipo, value="Gato").grid(row=0, column=1, sticky='e', padx=10)

tk.Button(tab1, text="Cadastrar", font=("", 15), command=cadastroAnimal).grid(row=5, columnspan=2)



listbox=tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizarListabox).grid(row=1, column=0)



janela.mainloop()