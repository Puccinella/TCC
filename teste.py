import customtkinter as ctk

#inicialização do projeto

def centralizar_janela(app, largura, altura):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width // 2) - (largura // 2)
    y = (screen_height // 2) - (altura // 2)
    app.geometry(f"{largura}x{altura}+{x}+{y}")

app = ctk.CTk()
app.overrideredirect(True)
app.title("CTK example")

centralizar_janela(app, 300, 100)
ctk.set_appearance_mode("dark")

app.configure(fg_color="#677183")

app.maxsize(200,100)
app.resizable(False,False)

# Adicione um botão para fechar
btn_fechar = ctk.CTkButton(app, text="Fechar", command=app.destroy)
btn_fechar.pack()

texto = ctk.CTkLabel(app, text="Carregando...", fg_color="transparent", font=("arial", 20))
texto.pack()

#dentro do app ja
#frame1








#frame3


#oq falta
#conseguir centralizar os frames e os botoes, colocar uma imagem de fundo, colocar uma imagem no botao de cadastro e no botao de verificacao, colocar um titulo na tela, colocar um aviso de que a inicialização pode demorar, colocar um texto de boas vindas, colocar um texto de o que deseja fazer



app.mainloop()