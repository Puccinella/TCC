import customtkinter as ctk

#botao função de ver
def verificacao():
    app.destroy()
    import index

def cadastro():
    app.destroy()
    import camera

#inicialização do projeto

app = ctk.CTk()
app.geometry("600x500")
app.minsize(480, 420)
app.title("Bem-vindo")

ctk.set_appearance_mode("dark")

app.configure(fg_color="#677183")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

frame_texto = ctk.CTkFrame(
    app,
    width=400,
    height=340,
    corner_radius=20,
    fg_color="#758194",
)
frame_texto.grid(row=0, column=0, padx=24, pady=24)
frame_texto.grid_propagate(False)
frame_texto.grid_columnconfigure(0, weight=1)
frame_texto.grid_rowconfigure((0, 5), weight=1)

label = ctk.CTkLabel(
    frame_texto,
    text="Bem-vindo!",
    fg_color="transparent",
    font=("Arial", 28, "bold"),
)
label.grid(row=1, column=0, padx=24, pady=(8, 4))

subtitulo = ctk.CTkLabel(
    frame_texto,
    text="Escolha uma opção para continuar",
    fg_color="transparent",
    font=("Arial", 15),
)
subtitulo.grid(row=2, column=0, padx=24, pady=(0, 20))

botaocadastro = ctk.CTkButton(
    frame_texto,
    text="Cadastrar",
    command=cadastro,
    font=("Arial", 18),
    height=46,
)
botaocadastro.grid(row=3, column=0, padx=40, pady=8, sticky="ew")

botao_verificacao = ctk.CTkButton(
    frame_texto,
    text="Verificação",
    command=verificacao,
    font=("Arial", 18),
    height=46,
)
botao_verificacao.grid(row=4, column=0, padx=40, pady=(8, 20), sticky="ew")

app.mainloop()

#tentei deixar mais legivel pra ler e entender