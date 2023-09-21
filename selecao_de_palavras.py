import random
import mysql.connector

# Conecta ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="usuario_mysql",
    password="senha_mysql",
    database="jogo_da_forca"
)

cursor = conexao.cursor()

# Função para escolher uma palavra aleatória do banco de dados
def escolher_palavra():
    cursor.execute("SELECT palavra FROM palavras")
    palavras = [row[0] for row in cursor.fetchall()]
    return random.choice(palavras)

# Função para mostrar a palavra oculta com os acertos do jogador
def mostrar_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta
