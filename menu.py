import tkinter as tk
import sys
def cadastro():
    root.destroy()
    import camera
def verificacao():
    root.destroy()
    import index

root= tk.Tk()
root.geometry('800x400')
root.title('Sistema de segurança que nao tem nome ainda')
titulo = tk.Label(root,text='Seja bem vindo(a) ao sistema de segurança que a gente nao deu nome ainda :)', font=('helvetica',16))
titulo.pack()
texto=tk.Label(root,text='O que deseja fazer?', font=('helvetica',14))
texto.pack()
aviso=tk.Label(root,text='!A inicialização pode demorar, caso pareça ter congelado apenas espere!', font=('helvetica',11))
aviso.pack()
Bcadastro=tk.Button(root,text='Cadastrar',command=cadastro,height='4',width='30')
Bcadastro.pack(side='left')
Bverif=tk.Button(root,text='Verificação',command=verificacao,height='4',width='30')
Bverif.pack(side='right')


root.mainloop()