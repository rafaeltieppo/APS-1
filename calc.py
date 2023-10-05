import tkinter as tk

def adicionar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 + num2)

def subtrair():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 - num2)

def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado.set(num1 * num2)

def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado.set(num1 / num2)
    else:
        resultado.set("Erro: Divisão por zero")

# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora")

# Entradas de números
tk.Label(janela, text="Número 1:").pack()
entry_num1 = tk.Entry(janela)
entry_num1.pack()

tk.Label(janela, text="Número 2:").pack()
entry_num2 = tk.Entry(janela)
entry_num2.pack()

# Variável para exibir o resultado
resultado = tk.StringVar()
resultado.set("Resultado: ")

# Botões de operação
btn_adicionar = tk.Button(janela, text="Adicionar", command=adicionar)
btn_adicionar.pack()

btn_subtrair = tk.Button(janela, text="Subtrair", command=subtrair)
btn_subtrair.pack()

btn_multiplicar = tk.Button(janela, text="Multiplicar", command=multiplicar)
btn_multiplicar.pack()

btn_dividir = tk.Button(janela, text="Dividir", command=dividir)
btn_dividir.pack()

# Exibição do resultado
label_resultado = tk.Label(janela, textvariable=resultado)
label_resultado.pack()

janela.mainloop()