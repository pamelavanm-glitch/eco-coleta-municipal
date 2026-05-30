# 🌱 EcoColeta Municipal

## 📌 Sobre o Projeto

O EcoColeta Municipal é um sistema web desenvolvido para auxiliar prefeituras no gerenciamento da coleta de resíduos especiais, promovendo o descarte correto de materiais que não podem ser destinados ao lixo comum.

A solução utiliza Inteligência Artificial para identificar resíduos por meio de imagens enviadas pelos cidadãos, fornecendo orientações sobre descarte adequado, riscos ambientais e incentivando a participação da população através de um sistema de EcoPontos.

---

## 🎯 Problema Resolvido

Muitos resíduos como pilhas, pneus, eletrônicos, óleo de cozinha e entulho são descartados incorretamente, causando impactos ambientais e riscos à saúde pública.

O sistema busca facilitar a comunicação entre cidadãos e prefeitura, permitindo a solicitação de coleta desses resíduos de forma simples e inteligente.

---

## 🚀 Funcionalidades

* Cadastro de solicitações de coleta.
* Upload de imagem do resíduo.
* Identificação automática do resíduo utilizando Inteligência Artificial.
* Análise ambiental realizada pela IA.
* Geração automática de protocolo.
* Sistema de EcoPontos.
* Armazenamento das solicitações em banco de dados SQLite.
* Interface web responsiva utilizando Bootstrap.

---

## 🤖 Inteligência Artificial

O sistema utiliza a API Gemini para:

* Identificar resíduos através de imagens.
* Classificar categorias de resíduos.
* Informar riscos ambientais.
* Recomendar o descarte correto.
* Auxiliar na atribuição de EcoPontos.

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python
* Flask

### Banco de Dados

* SQLite

### Inteligência Artificial

* Google Gemini API

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Manipulação de Imagens

* Pillow (PIL)

---

## 📂 Estrutura do Projeto

eco_coleta/

├── app.py

├── templates/

│ └── index.html

├── uploads/

├── database.db

├── requirements.txt

└── README.md

---

## 🔄 Fluxo do Sistema

1. O cidadão acessa o sistema.
2. Informa seus dados e a quantidade ou volume do resíduo.
3. Envia uma foto do material.
4. A Inteligência Artificial analisa a imagem.
5. O sistema gera uma classificação do resíduo.
6. Um protocolo é criado automaticamente.
7. EcoPontos são atribuídos ao cidadão.
8. A prefeitura recebe a solicitação para recolhimento.

---

## 🌎 Impacto Ambiental

A solução contribui para:

* Redução do descarte irregular.
* Aumento da reciclagem.
* Conscientização ambiental da população.
* Incentivo ao descarte correto por meio de recompensas.
* Melhoria da gestão municipal de resíduos.

---

## 💰 Sistema de EcoPontos

Os cidadãos acumulam pontos ao descartar resíduos corretamente.

Os pontos podem ser convertidos em benefícios como:

* Descontos em estabelecimentos parceiros.
* Benefícios municipais.
* Programas de incentivo ambiental.
* Possíveis descontos em taxas municipais, conforme regulamentação da prefeitura.

---

## ▶️ Como Executar o Projeto

### Instalar dependências

```bash
pip install flask
pip install google-generativeai
pip install pillow
```

### Executar o sistema

```bash
python app.py
```

### Acessar no navegador

```text
http://127.0.0.1:5000
```

## 👨‍💻 Autor

Projeto desenvolvido por Pamela Van Mierlo Miranda como projeto final do Laboratório de Imersão: Resolução de problemas com inteligência artificial, para o curso de ADS da Faculdades Pequeno Príncipe, integrando conceitos de:

* Lógica de Programação
* Banco de Dados
* Engenharia de Software
* Inteligência Artificial
* Desenvolvimento Web
* Sustentabilidade e Meio Ambiente
