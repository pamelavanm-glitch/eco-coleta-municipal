from flask import Flask, render_template, request
import sqlite3
import random
import os

import google.generativeai as genai
from PIL import Image

# ==========================================
# CONFIGURAÇÃO GEMINI
# ==========================================

genai.configure(api_key="GEMINI_API_KEY")

modelo = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
# FLASK
# ==========================================

app = Flask(__name__)

# ==========================================
# CRIA PASTA UPLOADS
# ==========================================

if not os.path.exists("uploads"):
    os.makedirs("uploads")

# ==========================================
# CRIA BANCO
# ==========================================

def criar_banco():

    conexao = sqlite3.connect("database.db")

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            descricao TEXT,
            protocolo TEXT,
            pontos INTEGER,
            analise_ia TEXT
        )
    """)

    conexao.commit()

    print("Banco criado com sucesso!")

    conexao.close()

# ==========================================
# HOME
# ==========================================

@app.route('/')
def home():
    return render_template('index.html')

# ==========================================
# CADASTRO
# ==========================================

@app.route('/cadastro', methods=['POST'])
def cadastro():

    nome = request.form['nome']
    endereco = request.form['endereco']
    descricao = request.form['descricao']

    protocolo = f"ECO{random.randint(1000,9999)}"

    # ==========================
    # RECEBE FOTO
    # ==========================

    foto = request.files['foto']

    caminho = os.path.join(
        "uploads",
        foto.filename
    )

    foto.save(caminho)

    imagem = Image.open(caminho)

    # ==========================
    # PROMPT GEMINI
    # ==========================

    prompt = f"""
    Analise esta imagem e identifique:

    1. Qual é o resíduo.
    2. Categoria do resíduo.
    3. Risco ambiental.
    4. Forma correta de descarte.
    5. Sugestão de EcoPontos.

    Informações fornecidas pelo cidadão:

    {descricao}

    Responda em português.
    """

    resposta = modelo.generate_content(
        [prompt, imagem]
    )

    analise = resposta.text

    # ==========================
    # CALCULAR ECOPONTOS
    # ==========================

    pontos = 20

    texto = analise.lower()

    if "pneu" in texto:
        pontos = 40

    elif "eletrôn" in texto or "eletron" in texto:
        pontos = 50

    elif "pilha" in texto:
        pontos = 20

    elif "óleo" in texto or "oleo" in texto:
        pontos = 30

    elif "entulho" in texto:
        pontos = 15

    # ==========================
    # SALVAR NO SQLITE
    # ==========================

    conexao = sqlite3.connect("database.db")

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO solicitacoes (
            nome,
            endereco,
            descricao,
            protocolo,
            pontos,
            analise_ia
        )

        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nome,
        endereco,
        descricao,
        protocolo,
        pontos,
        analise
    ))

    conexao.commit()
    conexao.close()

    # ==========================
    # RETORNO
    # ==========================

    return f"""
    <!DOCTYPE html>

    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <title>EcoColeta Municipal</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    </head>

    <body class="bg-light">

        <div class="container mt-5">

            <div class="card shadow">

                <div class="card-body">

                    <h2 class="text-success">
                        Solicitação registrada com sucesso!
                    </h2>

                    <hr>

                    <p>
                        <strong>Protocolo:</strong>
                        {protocolo}
                    </p>

                    <p>
                        <strong>EcoPontos:</strong>
                        {pontos}
                    </p>

                    <p>
                        <strong>Quantidade/Volume informado:</strong>
                        {descricao}
                    </p>

                    <h4 class="mt-4">
                        Análise da Inteligência Artificial
                    </h4>

                    <pre style="white-space: pre-wrap;">
{analise}
                    </pre>

                    <a href="/"
                       class="btn btn-success mt-3">

                       Nova Solicitação

                    </a>

                </div>

            </div>

        </div>

    </body>

    </html>
    """

# ==========================================
# EXECUÇÃO
# ==========================================

if __name__ == '__main__':
    criar_banco()
    app.run(debug=True)