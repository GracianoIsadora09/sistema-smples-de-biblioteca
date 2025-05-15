class Leitores:
    def __init__(self,leitor,cpf):
        self.leitor=leitor
        self.cpf=cpf
        self.ativo=True

    def cadastro(self):
        self.leitor =input("digite o seu nome")
        self.cpf= input("digite seu cpf")

class Autor:

    def __init__(self,nome,nacionalidade):
        self.nome=nome
        self.nacionalidade=nacionalidade


class Livro:
    def __init__(self,autor,titulo,ano):
        self.autor=autor
        self.titulo=titulo
        self.ano=ano
        self.disponivel = True
    
    def exibir_informação(self):
        print(f"Autor:{self.autor.nome} Titulo:{self.titulo} e o ano de publicação é: {self.ano}.")

    def emprestar(self,leitor,livro):
        self.leitor=leitor
        self.livro=livro
        
        if livro.disponivel:
            print("o livro está disponivel na biblioteca")
            livro.disponivel = False
        else:
            print("o livro não está disponível no momento")

class Multa:
    def calcular(self,dias_atraso):
     if dias_atraso > 0:
        taxa = dias_atraso * 0.60
        print(f"Você está com {dias_atraso} dias de atraso. A multa é R$ {taxa:.2f}")
     else:
        print("seu livro foi devolvido no prazo")

    def bloquear_usuario(self,vezes_atraso,usuario):
     if not hasattr(usuario, "ativo"):
         usuario.ativo = True

    if vezes_atraso > 4: # A quantidade de vezes máxima de atraso é 4
         usuario.ativo = False
         print(f"Vc já atrasou o numero de vezes máximo de atraso e não pode mais pegar livros")

        




