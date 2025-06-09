import tkinter as tk
from tkinter import ttk, messagebox
import requests

def obter_cotacao(moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/BRL-{moeda_destino}"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        chave = f"BRL{moeda_destino}"
        return float(dados[chave]['bid'])
    except:
        return None

def converter():
    try:
        valor = float(entrada_valor.get())
        moeda = combo_moeda.get().upper()
        cotacao = obter_cotacao(moeda)
        
        if cotacao:
            convertido = valor * cotacao
            resultado["text"] = f"R${valor:.2f} = {moeda} {convertido:.2f}"
            cotacao_label["text"] = f"Cotação: 1 BRL = {cotacao:.4f} {moeda}"
        else:
            messagebox.showerror("Erro", "Não foi possível obter a cotação.")
    except ValueError:
        messagebox.showwarning("Atenção", "Digite um valor numérico válido.")

# Interface
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("300x230")

# Widgets
tk.Label(janela, text="Valor em BRL:").pack(pady=5)
entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="Converter para:").pack(pady=5)
combo_moeda = ttk.Combobox(janela, values=["USD", "EUR", "ARS", "GBP", "BTC"])
combo_moeda.set("USD")
combo_moeda.pack()

tk.Button(janela, text="Converter", command=converter).pack(pady=10)
resultado = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado.pack()

cotacao_label = tk.Label(janela, text="", font=("Arial", 10))
cotacao_label.pack()

# Loop da janela
janela.mainloop()