import customtkinter as ctk

#botao função de ver
def verificacao():
    app.destroy()
    import camera

def cadastro():
    app.destroy()
    import index

#inicialização do projeto
app = ctk.CTk()
app.geometry("600x500")
app.title("CTK example")


#teste
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2), weight=1)

#criação dos frames 
frame1 = ctk.CTkFrame(app, border_width=2, border_color="white")
frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame2 = ctk.CTkFrame(app, border_width=2, border_color="red")
frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

frame3 = ctk.CTkFrame(app, border_width=2, border_color="blue")
frame3.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")



#dentro do app ja
#frame1
label = ctk.CTkLabel(frame1, text="Testes", fg_color="transparent", font=("arial", 20),  border_width=2, border_color="white")
label.grid(row=0, column=0, padx=10, pady=10)

botaocadastro = ctk.CTkButton(frame1, text="Cadastrar", command=verificacao)
botaocadastro.grid(row=1, column=0, padx=20, pady=10)

#frame2
label = ctk.CTkLabel(frame2, text="Testes", fg_color="transparent", font=("arial", 20), border_width=2, border_color="white")
label.grid(row=0, column=0, padx=10, pady=10)


#frame3
label = ctk.CTkLabel(frame3, text="Testes", fg_color="transparent", font=("arial", 20), border_width=2, border_color="white")
label.grid(row=0, column=0, padx=10, pady=10)

botao_verificacao = ctk.CTkButton(frame3, text="Verificação", command=cadastro)
botao_verificacao.grid(row=1, column=0, padx=20, pady=10)

#oq falta
#conseguir centralizar os frames e os botoes, colocar uma imagem de fundo, colocar uma imagem no botao de cadastro e no botao de verificacao, colocar um titulo na tela, colocar um aviso de que a inicialização pode demorar, colocar um texto de boas vindas, colocar um texto de o que deseja fazer



app.mainloop()