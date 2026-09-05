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
        password="232009",
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

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id SERIAL PRIMARY KEY,
            prontuario VARCHAR(20) UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            id SERIAL PRIMARY KEY,
            pessoa_id INTEGER NOT NULL,
            embedding DOUBLE PRECISION[] NOT NULL,
            CONSTRAINT fk_pessoa
                FOREIGN KEY (pessoa_id)
                REFERENCES pessoas(id)
                ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log (
            id SERIAL PRIMARY KEY,
            pessoa_id INTEGER NOT NULL,
            status VARCHAR(10) NOT NULL,   -- 'entrada' ou 'saida'
            data_hora TIMESTAMP NOT NULL DEFAULT NOW(),
            CONSTRAINT fk_pessoa_log
                FOREIGN KEY (pessoa_id)
                REFERENCES pessoas(id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("deu certo")



def registrar_log(prontuario, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM pessoas WHERE prontuario = %s", (prontuario,))
    resultado = cursor.fetchone()
    if resultado is None:
        cursor.close()
        conn.close()
        return None

    pessoa_id = resultado[0]
    cursor.execute(
        "INSERT INTO log (pessoa_id, status) VALUES (%s, %s)",
        (pessoa_id, status)
    )
    conn.commit()
    cursor.close()
    conn.close()

def ultimo_status(prontuario):
    # isso aq retorna entrada, saida ou None se a pessoa nunca passou pela catraca para distinguir o status de entrada e saída
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT l.status FROM log l
        JOIN pessoas p ON p.id = l.pessoa_id
        WHERE p.prontuario = %s
        ORDER BY l.data_hora DESC
        LIMIT 1
    """, (prontuario,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None

if __name__ == "__main__":
    criar_tabelas()


criar_tabelas()

print ("deu certo")



#teste do cadastro
