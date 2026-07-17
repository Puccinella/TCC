#lembrem de instalar o psycopg2-binary para funcionar o banco de dados
#lembrem também de instalar o postgresql, criar o banco de dados, as tabelas configurar certo
#e colocar tudo certo no "conectar"
import psycopg2

def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="projeto_tcc",
        user="postgres",
        password="20558970",
        port="5432"
    )
    return conn

def cadastro(jc, embedding):
    pass

conn = conectar()
print ("deu certo")