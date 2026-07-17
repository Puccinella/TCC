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
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (prontuario, embedding) VALUES (%s, %s)", (jc, embedding))
    conn.commit()

    cursor.close()
    conn.close()

def buscar_pessoa(jc):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE prontuario = %s", (jc,))
    pessoa = cursor.fetchone()

    cursor.close()
    conn.close()
    return pessoa

def deletar_pessoa(jc):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pessoas WHERE prontuario = %s", (jc,))
    conn.commit()

    cursor.close()
    conn.close()

conn = conectar()
print ("deu certo")

#teste do cadastro
cadastro("JC303020",[0.1, 0.2, 0.3, 0.4, 0.5])  
pessoa = buscar_pessoa("JC303020")
print("Pessoa encontrada:", pessoa)