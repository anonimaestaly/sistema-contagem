import tkinter as tk
from tkinter import messagebox

FUNDO = "#080914"
PAINEL = "#111329"
ROXO = "#746cff"
BRANCO = "#ffffff"
VERDE = "#65ff7a"


def iniciar_contagem():
    try:
        inicio = int(entrada_inicio.get())
        final = int(entrada_final.get())
        incremento = int(entrada_incremento.get())
    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números."
        )
        return

    if incremento <= 0:
        messagebox.showerror(
            "Erro",
            "O incremento precisa ser maior que zero."
        )
        return

    if inicio > final:
        messagebox.showerror(
            "Erro",
            "O número inicial não pode ser maior que o final."
        )
        return

    resultado.delete("1.0", tk.END)

    resultado.insert(
        tk.END,
        ">>> CONTAGEM INICIADA <<<\n\n"
    )

    numero = inicio

    while numero <= final:
        resultado.insert(
            tk.END,
            str(numero) + "\n"
        )

        numero += incremento

    resultado.insert(
        tk.END,
        "\n>>> MISSÃO CONCLUÍDA <<<"
    )

    status.config(
        text="STATUS: CONCLUÍDO",
        fg=VERDE
    )


def limpar():
    entrada_inicio.delete(0, tk.END)
    entrada_final.delete(0, tk.END)
    entrada_incremento.delete(0, tk.END)

    entrada_inicio.insert(0, "1")
    entrada_final.insert(0, "20")
    entrada_incremento.insert(0, "2")

    resultado.delete("1.0", tk.END)

    resultado.insert(
        tk.END,
        "Digite os valores e clique em INICIAR CONTAGEM."
    )

    status.config(
        text="STATUS: PRONTO",
        fg=VERDE
    )


def criar_campo(texto, valor):
    label = tk.Label(
        painel,
        text=texto,
        font=("Arial", 12, "bold"),
        fg=BRANCO,
        bg=PAINEL
    )

    label.pack(
        anchor="w",
        pady=(10, 5)
    )

    campo = tk.Entry(
        painel,
        font=("Arial", 18),
        justify="center",
        bg=FUNDO,
        fg=BRANCO,
        insertbackground=BRANCO,
        width=20
    )

    campo.pack(
        pady=(0, 15),
        ipady=8
    )

    campo.insert(0, valor)

    return campo


janela = tk.Tk()
janela.title("Sistema de Contagem")
janela.geometry("1000x650")
janela.minsize(850, 550)
janela.configure(bg=FUNDO)


titulo = tk.Label(
    janela,
    text="SISTEMA DE CONTAGEM",
    font=("Arial", 30, "bold"),
    fg=BRANCO,
    bg=FUNDO
)

titulo.pack(pady=(30, 25))


area = tk.Frame(
    janela,
    bg=FUNDO
)

area.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


painel = tk.Frame(
    area,
    bg=PAINEL,
    padx=25,
    pady=25
)

painel.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)


entrada_inicio = criar_campo(
    "NÚMERO INICIAL",
    "1"
)

entrada_final = criar_campo(
    "NÚMERO FINAL",
    "20"
)

entrada_incremento = criar_campo(
    "INCREMENTO",
    "2"
)


botao_iniciar = tk.Button(
    painel,
    text="INICIAR CONTAGEM",
    command=iniciar_contagem,
    font=("Arial", 12, "bold"),
    bg=ROXO,
    fg=BRANCO,
    activebackground=ROXO,
    activeforeground=BRANCO,
    relief="flat",
    cursor="hand2"
)

botao_iniciar.pack(
    fill="x",
    pady=(10, 8),
    ipady=10
)


botao_limpar = tk.Button(
    painel,
    text="LIMPAR DADOS",
    command=limpar,
    font=("Arial", 12, "bold"),
    bg=FUNDO,
    fg=BRANCO,
    activebackground=ROXO,
    activeforeground=BRANCO,
    relief="flat",
    cursor="hand2"
)

botao_limpar.pack(
    fill="x",
    pady=8,
    ipady=10
)


painel_resultado = tk.Frame(
    area,
    bg=PAINEL,
    padx=20,
    pady=20
)

painel_resultado.pack(
    side="left",
    fill="both",
    expand=True
)


titulo_resultado = tk.Label(
    painel_resultado,
    text="RESULTADO",
    font=("Arial", 18, "bold"),
    fg=BRANCO,
    bg=PAINEL
)

titulo_resultado.pack(
    pady=(0, 15)
)


resultado = tk.Text(
    painel_resultado,
    font=("Consolas", 14),
    bg=FUNDO,
    fg=VERDE,
    insertbackground=BRANCO,
    relief="flat",
    padx=15,
    pady=15
)

resultado.pack(
    fill="both",
    expand=True
)


resultado.insert(
    tk.END,
    "Digite os valores e clique em INICIAR CONTAGEM."
)


status = tk.Label(
    janela,
    text="STATUS: PRONTO",
    font=("Consolas", 10),
    fg=VERDE,
    bg=FUNDO
)

status.pack(pady=10)


janela.bind(
    "<Return>",
    lambda evento: iniciar_contagem()
)


janela.mainloop()