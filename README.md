# 🎮 GameRate

Sistema simples de avaliação de jogos desenvolvido com Flask.
O usuário pode enviar o nome do jogo e uma nota de 1 a 10, e as avaliações aparecem em uma página dedicada.

O projeto focou principalmente em rotas, métodos GET e POST e renderização de templates.

## 📌 Funcionalidades

Envio de avaliação de jogos por meio de formulário:
- Nome do jogo
- Nota (1–10)
- Página que lista todas as avaliações enviadas
- Contagem total de avaliações
- Validação básica para evitar campos vazios
- Atualização dinâmica das avaliações após envio

## 🛠 Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- Jinja2 (templating do Flask)

## ⚙️ Como executar o projeto
 No Bash:

1️⃣ Clonar o repositório com
"git clone https://github.com/LucaSuzuki/GameRate.git"

2️⃣ Entrar na pasta do projeto digitando
"cd GameRate"

3️⃣ Instalar o Flask utilizando o comando
"pip install flask"

4️⃣ Executar o servidor 
"python main.py"

5️⃣ Abrir no navegador
http://127.0.0.1:5000

## 📖 Como funciona

O usuário acessa a página inicial e preenche o formulário com o nome do jogo e sua nota.

O formulário envia os dados para o servidor Flask.

O servidor armazena temporariamente as avaliações em uma lista e o usuário é automaticamente redirecionado para a página Ratings, onde todas as avaliações são exibidas.


## 🚀 Melhorias futuras

- Upload de imagens dos jogos
- Sistema de edição e remoção de avaliações

## 📚 Objetivo do projeto

Este projeto foi criado com o objetivo demonstrar conceitos de desenvolvimento web com Flask, incluindo:

- Criação de rotas
- Envio de dados via formulários
- Manipulação de métodos GET e POST
- Uso de templates com Jinja2

## 📔Bibliotecas necessárias
[Requirements](requirements.txt)
