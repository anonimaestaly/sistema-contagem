import tkinter as tk
from tkinter import messagebox


# Cores da tela
FUNDO = "#080914"
PAINEL = "#111329"
ROXO = "#746cff"
BRANCO = "#ffffff"
VERDE = "#65ff7a"


def iniciar():
    try:
        inicio = int(campo_inicio.get())
        fim = int(campo_fim.get())
        passo = int(campo_passo.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite somente números.")
        return

    if passo <= 0:
        messagebox.showerror("Erro", "O incremento deve ser maior que zero.")
        return

    if inicio > fim:
        messagebox.showerror("Erro", "O início não pode ser maior que o final.")
        return

    caixa_resultado.delete("1.0", tk.END)

    # Mensagem que aparece antes da contagem
    caixa_resultado.insert(
        tk.END,
        ">>> CONTAGEM INICIADA <<<\n\n"
    )

    numero = inicio

    while numero <= fim:
        caixa_resultado.insert(
            tk.END,
            str(numero) + "\n"
        )

        numero = numero + passo

    # Mensagem que aparece depois da contagem
    caixa_resultado.insert(
        tk.END,
        "\n>>> MISSÃO CONCLUÍDA <<<"
    )

    status.config(text="STATUS: CONCLUÍDO")


def limpar():
    # Apaga os valores dos campos
    campo_inicio.delete(0, tk.END)
    campo_fim.delete(0, tk.END)
    campo_passo.delete(0, tk.END)

    # Apaga todo o resultado
    caixa_resultado.delete("1.0", tk.END)

    # Volta o status para o início
    status.config(text="STATUS: PRONTO")


# Janela
janela = tk.Tk()
janela.title("Sistema de Contagem")
janela.geometry("1000x650")
janela.configure(bg=FUNDO)


# Título
titulo = tk.Label(
    janela,
    text="SISTEMA DE CONTAGEM",
    font=("Arial", 30, "bold"),
    fg=BRANCO,
    bg=FUNDO
)
titulo.pack(pady=30)


# Área onde ficam os dois painéis
area = tk.Frame(janela, bg=FUNDO)
area.pack(fill="both", expand=True, padx=30, pady=10)


# Painel esquerdo
painel = tk.Frame(
    area,
    bg=PAINEL,
    padx=25,
    pady=20
)
painel.pack(side="left", fill="y", padx=(0, 15))


# Número inicial
tk.Label(
    painel,
    text="NÚMERO INICIAL",
    font=("Arial", 12, "bold"),
    fg=BRANCO,
    bg=PAINEL
).pack(anchor="w", pady=(10, 5))

campo_inicio = tk.Entry(
    painel,
    font=("Arial", 18),
    justify="center",
    bg=FUNDO,
    fg=BRANCO,
    insertbackground=BRANCO
)
campo_inicio.pack(pady=(0, 15), ipady=8)
campo_inicio.insert(0, "1")


# Número final
tk.Label(
    painel,
    text="NÚMERO FINAL",
    font=("Arial", 12, "bold"),
    fg=BRANCO,
    bg=PAINEL
).pack(anchor="w", pady=(10, 5))

campo_fim = tk.Entry(
    painel,
    font=("Arial", 18),
    justify="center",
    bg=FUNDO,
    fg=BRANCO,
    insertbackground=BRANCO
)
campo_fim.pack(pady=(0, 15), ipady=8)
campo_fim.insert(0, "20")


# Incremento
tk.Label(
    painel,
    text="INCREMENTO",
    font=("Arial", 12, "bold"),
    fg=BRANCO,
    bg=PAINEL
).pack(anchor="w", pady=(10, 5))

campo_passo = tk.Entry(
    painel,
    font=("Arial", 18),
    justify="center",
    bg=FUNDO,
    fg=BRANCO,
    insertbackground=BRANCO
)
campo_passo.pack(pady=(0, 15), ipady=8)
campo_passo.insert(0, "2")


# Botão iniciar
tk.Button(
    painel,
    text="INICIAR CONTAGEM",
    command=iniciar,
    font=("Arial", 12, "bold"),
    bg=ROXO,
    fg=BRANCO,
    relief="flat",
    cursor="hand2"
).pack(fill="x", pady=8, ipady=10)


# Botão limpar
tk.Button(
    painel,
    text="LIMPAR DADOS",
    command=limpar,
    font=("Arial", 12, "bold"),
    bg=ROXO,
    fg=BRANCO,
    relief="flat",
    cursor="hand2"
).pack(fill="x", pady=8, ipady=10)


# Painel direito
resultado = tk.Frame(
    area,
    bg=PAINEL,
    padx=20,
    pady=20
)
resultado.pack(side="left", fill="both", expand=True)


tk.Label(
    resultado,
    text="RESULTADO",
    font=("Arial", 18, "bold"),
    fg=BRANCO,
    bg=PAINEL
).pack(pady=(0, 15))


# Caixa onde aparecem os números
caixa_resultado = tk.Text(
    resultado,
    font=("Consolas", 14),
    bg=FUNDO,
    fg=VERDE,
    relief="flat",
    padx=15,
    pady=15
)
caixa_resultado.pack(fill="both", expand=True)


# Status
status = tk.Label(
    janela,
    text="STATUS: PRONTO",
    font=("Consolas", 10),
    fg=VERDE,
    bg=FUNDO
)
status.pack(pady=10)


# Enter também inicia
janela.bind("<Return>", lambda evento: iniciar())


janela.mainloop()
