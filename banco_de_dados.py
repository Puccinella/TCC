#lembrem de instalar o psycopg2-binary para funcionar o banco de dados
#lembrem também de instalar o postgresql, criar o banco de dados, as tabelas configurar certo
#e colocar tudo certo no "conectar"
#no pgadmin usei os comandos para criar as tabelas:
#CREATE TABLE pessoas (
#    id SERIAL PRIMARY KEY,
#    prontuario VARCHAR(20) UNIQUE NOT NULL
#);
#CREATE TABLE embeddings (
#    id SERIAL PRIMARY KEY,
#    pessoa_id INTEGER NOT NULL,
#    embedding DOUBLE PRECISION[] NOT NULL,
#    CONSTRAINT fk_pessoa
#        FOREIGN KEY (pessoa_id)
#        REFERENCES pessoas(id)
#        ON DELETE CASCADE
#);
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

def cadastro(jc):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (prontuario) VALUES (%s) RETURNING id", (jc,))
    pessoa_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()
    return pessoa_id

def adicionar_foto(pessoa_id, embedding):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO embeddings (pessoa_id, embedding) VALUES (%s, %s)", (pessoa_id, embedding))
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

#se pa que isso vai ser a chave do nosso reconhecimento facial ->
def buscar_todos_embeddings():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT p.prontuario, e.embedding FROM pessoas p JOIN embeddings e ON p.id = e.pessoa_id")

    dados_pro_reconhecimento = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados_pro_reconhecimento


conn = conectar()
print ("deu certo")

#teste do cadastro
