from flask import Flask, render_template, request, redirect, url_for, flash
from usuario_service import UsuarioService

# Criação da instância do Flask, que será responsável por servir as páginas web
app = Flask(__name__)

# Definir uma chave secreta para o uso de mensagens de flash (alertas temporários)
app.secret_key = 'secretkey'  

# Instancia o serviço de usuários, que contém a lógica de cadastro e login
usuario_service = UsuarioService()

# Rota para a página inicial
@app.route('/')
def index():
    # Renderiza a página inicial (index.html) onde o usuário pode escolher entre cadastro ou login
    return render_template('index.html')

# Rota para a página de cadastro de usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    # Se o método HTTP for POST, o formulário foi enviado
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        try:
            # Chama o serviço de usuário para cadastrar o novo usuário
            usuario_service.cadastrar_usuario(nome, email, senha)
            # Mensagem de sucesso via flash (mensagem temporária)
            flash('Usuário cadastrado com sucesso!', 'success')
            # Redireciona o usuário para a página de login após o cadastro
            return redirect(url_for('login'))
        except ValueError as e:
            # Se houver algum erro, exibe a mensagem de erro
            flash(str(e), 'danger')

    # Se o método for GET (quando a página for acessada inicialmente), renderiza o formulário de cadastro
    return render_template('cadastro.html')

# Rota para a página de login de usuário
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se o método HTTP for POST, o formulário foi enviado
    if request.method == 'POST':
        # Obtém os dados do formulário de login
        email = request.form['email']
        senha = request.form['senha']
        
        try:
            # Tenta realizar o login com os dados fornecidos
            usuario = usuario_service.login(email, senha)
            # Mensagem de sucesso via flash
            flash('Login bem-sucedido!', 'success')
            # Redireciona o usuário para a página inicial após login
            return redirect(url_for('index'))
        except ValueError as e:
            # Se houver erro no login (email ou senha incorretos), exibe a mensagem de erro
            flash(str(e), 'danger')

    # Se o método for GET (quando a página for acessada inicialmente), renderiza o formulário de login
    return render_template('login.html')

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
