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
app.title("CTK example")

ctk.set_appearance_mode("dark")

app.configure(fg_color="#677183")

#teste
app.grid_columnconfigure((0,2), weight=1)

app.grid_columnconfigure(1, weight=2)

app.grid_rowconfigure(0, weight=1)

#criação dos frames
frame1 = ctk.CTkFrame(app, border_width=2, border_color="", fg_color="transparent")
frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame2 = ctk.CTkFrame(app, border_width=2, border_color="", corner_radius=20 ,fg_color="#758194")
frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

frame3 = ctk.CTkFrame(app, border_width=2, border_color="", fg_color="transparent")
frame3.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")



#dentro do app ja
#frame1


#frame2
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure((0,1,2), weight=1)

#criação de outro frame dentro do frame2

frame_texto = ctk.CTkFrame(frame2, border_width=2, border_color="", fg_color="transparent")
frame_texto.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


frame_texto.grid_columnconfigure(0, weight=1)



#botao e caixa de texto dentro do frame_texto
label = ctk.CTkLabel(frame_texto, text="Bem vindo(a)!", fg_color="transparent", font=("arial", 30), border_width=2, border_color="")
label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


botaocadastro = ctk.CTkButton(frame_texto, text="Cadastrar", command=cadastro, font=("arial", 25))
botaocadastro.grid(row=1, column=0, padx=20, pady=10, sticky="ew")


botao_verificacao = ctk.CTkButton(frame_texto, text="Verificação", command=verificacao, font=("arial", 25))
botao_verificacao.grid(row=2, column=0, padx=20, pady=10, sticky="ew")






#frame3


#oq falta
#conseguir centralizar os frames e os botoes, colocar uma imagem de fundo, colocar uma imagem no botao de cadastro e no botao de verificacao, colocar um titulo na tela, colocar um aviso de que a inicialização pode demorar, colocar um texto de boas vindas, colocar um texto de o que deseja fazer



app.mainloop()
