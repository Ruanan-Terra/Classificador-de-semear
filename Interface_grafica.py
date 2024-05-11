import tkinter as tk
from tkinter import ttk
import joblib

# Carregar o modelo treinado
modelo = joblib.load('modelo.joblib')

# Carregar o codificador de rótulos
le = joblib.load('label_encoder.joblib')

def fazer_previsao():
    try:
        # Obter os dados inseridos pelo usuário
        nitrogenio = float(entries['Nitrogênio'].get())
        fosforo = float(entries['Fósforo'].get())
        potassio = float(entries['Potássio'].get())
        temperatura = float(entries['Temperatura'].get())
        umidade = float(entries['Umidade'].get())
        ph = float(entries['pH'].get())
        precipitacao = float(entries['Precipitação'].get())

        # Fazer a previsão com o modelo
        resultado = modelo.predict([[nitrogenio, fosforo, potassio, temperatura, umidade, ph, precipitacao]])
        
        # Converter o número da classe de volta para o nome da cultura correspondente
        cultura_recomendada = le.inverse_transform(resultado)[0]

        # Atualizar o rótulo com o resultado da previsão
        resultado_label.config(text=f'Cultura recomendada: {cultura_recomendada}')
    except ValueError:
        resultado_label.config(text='Por favor, insira valores numéricos válidos.')

# Criar a janela principal
root = tk.Tk()
root.title('Previsão de Cultura')

# Criar e posicionar os rótulos e campos de entrada
campos = ['Nitrogênio', 'Fósforo', 'Potássio', 'Temperatura', 'Umidade', 'pH', 'Precipitação']
entries = {}

for i, campo in enumerate(campos):
    tk.Label(root, text=campo + ':').grid(row=i, column=0, padx=5, pady=5)
    entries[campo] = tk.Entry(root)
    entries[campo].grid(row=i, column=1, padx=5, pady=5)

# Criar um botão para fazer a previsão
btn_prever = tk.Button(root, text='Prever', command=fazer_previsao)
btn_prever.grid(row=len(campos), column=0, columnspan=2, padx=5, pady=5)

# Criar um rótulo para exibir o resultado da previsão
resultado_label = tk.Label(root, text='')
resultado_label.grid(row=len(campos) + 1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
