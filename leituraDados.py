import serial
import csv
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuração da porta serial (ajuste para a porta correta)
porta_serial = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

# Nome do arquivo CSV
arquivo_csv = "dados_temperatura.csv"

# Criar cabeçalho no CSV caso o arquivo não exista
with open(arquivo_csv, mode="a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Timestamp", "Temperatura", "Umidade"])

# Variáveis globais para dados
tempos = []
temperaturas = []
umidades = []

# Criando interface gráfica (Tkinter)
root = tk.Tk()
root.title("Estação Meteorológica")

# Layout da interface
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

# Labels para exibir dados
lbl_temp_atual = ttk.Label(frame, text="Temperatura Atual: -- °C", font=("Arial", 14))
lbl_temp_atual.grid(row=0, column=0, sticky="w", pady=5)

lbl_temp_max = ttk.Label(frame, text="Temperatura Máx: -- °C", font=("Arial", 12))
lbl_temp_max.grid(row=1, column=0, sticky="w")

lbl_temp_min = ttk.Label(frame, text="Temperatura Mín: -- °C", font=("Arial", 12))
lbl_temp_min.grid(row=2, column=0, sticky="w")

lbl_temp_media = ttk.Label(frame, text="Temperatura Média: -- °C", font=("Arial", 12))
lbl_temp_media.grid(row=3, column=0, sticky="w")

# Função para exportar os dados para Excel
def exportar_para_excel():
    df = pd.read_csv(arquivo_csv)
    df.to_excel("dados_temperatura.xlsx", index=False)
    print("Arquivo Excel gerado com sucesso!")

# Função para exportar o gráfico como imagem
def exportar_grafico():
    fig.savefig("grafico_temperatura.png", dpi=300)
    print("Gráfico salvo como 'grafico_temperatura.png'!")

# Cria um estilo para os botões
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)  # Aumenta fonte e espaçamento interno

# Botões para exportação
btn_exportar_excel = ttk.Button(frame, text="Exportar para Excel", command=exportar_para_excel)
btn_exportar_excel.grid(row=5, column=0, pady=10, ipadx=10) # ipadx aumenta a largura do botão e pady aumenta a altura

btn_exportar_img = ttk.Button(frame, text="Salvar Gráfico", command=exportar_grafico)
btn_exportar_img.grid(row=6, column=0, pady=10, ipadx=10)

# Criar gráfico no Tkinter
fig, ax = plt.subplots(figsize=(10, 5))  # Aumenta o tamanho do gráfico
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10)

def atualizar_grafico(frame):
    """ Lê os dados do Arduino, armazena no CSV, atualiza o gráfico e a interface """
    global tempos, temperaturas, umidades

    try:
        linha = porta_serial.readline().decode('utf-8').strip()
        if linha:
            valores = linha.split(",")

            if len(valores) == 2:
                temperatura, umidade = map(float, valores)
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

                # Armazenar no CSV
                with open(arquivo_csv, mode="a", newline="") as arquivo:
                    escritor = csv.writer(arquivo)
                    escritor.writerow([timestamp, temperatura, umidade])

                # Atualizar listas
                tempos.append(timestamp)
                temperaturas.append(temperatura)
                umidades.append(umidade)

                # Manter apenas os últimos 20 valores
                if len(tempos) > 20:
                    tempos.pop(0)
                    temperaturas.pop(0)
                    umidades.pop(0)

                # Atualizar gráfico
                ax.clear()
                ax.plot(tempos, temperaturas, marker='o', linestyle='-', color='purple', label="Temperatura (°C)")
                ax.set_xticklabels(tempos, rotation=45, ha="right")
                ax.set_ylabel("Temperatura (°C)")
                ax.set_xlabel("Tempo")
                ax.set_title("Variação da Temperatura")
                ax.legend()
                plt.tight_layout()
                canvas.draw()

                # Atualizar interface
                lbl_temp_atual.config(text=f"Temperatura Atual: {temperatura:.2f} °C")

                if temperaturas:
                    lbl_temp_max.config(text=f"Temperatura Máx: {max(temperaturas):.2f} °C")
                    lbl_temp_min.config(text=f"Temperatura Mín: {min(temperaturas):.2f} °C")
                    lbl_temp_media.config(text=f"Temperatura Média: {sum(temperaturas) / len(temperaturas):.2f} °C")

    except ValueError:
        print(f"Erro ao processar: {linha}")

# Criar animação para atualizar o gráfico
ani = animation.FuncAnimation(fig, atualizar_grafico, interval=10000)

# Iniciar interface gráfica
root.mainloop()

# Fechar porta serial ao encerrar o programa
porta_serial.close()
