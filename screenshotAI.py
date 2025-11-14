import pyautogui
import tkinter as tk

from tkinter import messagebox
import os

from mouseinfo import screenshot


def proximo_numero_arquivo(nome_base):
    contador = 1
    while True:
        nome = f'{nome_base}_{contador}.png'
        if not os.path.exists(nome):
            return nome
        contador += 1

def capturar_tela():
    nome_base = entrada_nome.get().strip()

    if nome_base == "":
        messagebox.showerror("Erro", "Digite um nome do arquivo")
        return
    nome_final = proximo_numero_arquivo(nome_base)

    try:
        screenshot = pyautogui.screenshot()
        caminho = os.path.join(os.getcwd(), nome_final)
        screenshot.save(caminho)

        messagebox.showinfo("Sucesso", f"Imagem salva como: \n{caminho}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n {e}")



janela = tk.Tk()
janela.title("Python Screenshots")
janela.geometry("300x200")
janela.resizable(False, False)

tk.Label(janela, text="Python Screenshots", font=("Arial", 12)).pack(pady=10)
entrada_nome = tk.Entry(janela, font=("Arial", 12), justify="center")
entrada_nome.insert(0, "captura") #Nome padrao
btn = tk.Button(janela,text="Capturar", font=("Arial", 12), command=capturar_tela)
btn.pack(pady=10)

janela.mainloop()

