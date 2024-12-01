import re

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class UsuarioService:
    def __init__(self):
        # Lista que vai armazenar os usuários (em um cenário real, isso seria um banco de dados)
        self.usuarios = []

    def cadastrar_usuario(self, nome, email, senha):
        """
        Função para cadastrar um usuário. Valida se o email é único e se a senha
        atende aos requisitos de segurança.
        """
        # Validar se o email já existe
        if not self._validar_email(email):
            raise ValueError("Email inválido ou já cadastrado.")
        
        # Validar a senha
        if not self._validar_senha(senha):
            raise ValueError("A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")
        
        # Criar o usuário e adicionar à lista
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def login(self, email, senha):
        """
        Função para realizar o login de um usuário. Verifica se o email e a senha
        estão corretos.
        """
        # Buscar o usuário pelo email
        usuario = self._buscar_usuario_por_email(email)
        if usuario and usuario.senha == senha:
            return usuario
        else:
            raise ValueError("Email ou senha incorretos.")

    def _validar_email(self, email):
        """
        Valida se o email é único e tem formato válido.
        """
        # Verificar se o email já está cadastrado
        if any(u.email == email for u in self.usuarios):
            return False
        # Validar o formato do email
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def _validar_senha(self, senha):
        """
        Valida se a senha tem pelo menos 8 caracteres e contém pelo menos um número.
        """
        return len(senha) >= 8 and any(char.isdigit() for char in senha)

    def _buscar_usuario_por_email(self, email):
        """
        Procura e retorna o usuário pelo email.
        """
        return next((u for u in self.usuarios if u.email == email), None)
