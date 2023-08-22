from Pessoa import *
from Genero import *
from datetime import date

usuarios = list()
livros = list()
emprestimos = list()

today = date.today()

resposta = 0
possiveisRespostas = [1, 2, 3, 4, 5, 6, 7]

def cadastrar_emprestimo():

    amigoEmprestimo = None
    livroEmprestimo = None

    while 1:
        tituloLivro = input("Digite o nome do livro ou digite menu para voltar ao menu.\n")
        if tituloLivro == "menu":
            main()
        encontrado = False
        for livro in livros:
            if livro.titulo == tituloLivro:
                print("Livro encontrado.")
                encontrado = True
                livroEmprestimo = livro
                break
        if encontrado:
            break
        else:
            print("livro não encontrado.")
    while 1:
        nomeAmigo = input("Digite o nome do amigo ou digite menu para voltar ao menu.\n")
        if nomeAmigo == "menu":
            main()
        encontrado = False
        for amigo in usuarios:
            if amigo.nome == nomeAmigo:
                print("Amigo encontrado.")
                amigoEmprestimo = amigo
                encontrado = True
                break
        if encontrado:
            break
        else:
            print("Amigo não encontrado.")
    resposta = int(input("1 - Colocar data atual.\n2 - Colocar data manualmente.\n"))
    if resposta == 1:
        amigoEmprestimo.add_emprestimo(Emprestimo(livroEmprestimo, today.strftime("%d/%m/%y")))
    elif resposta == 2:
        data = input("Coloque a data no formato dd/mm/aaaa. ")
        amigoEmprestimo.add_emprestimo(Emprestimo(livroEmprestimo, data))  # todo: checar input da data
    print(amigoEmprestimo.emprestimos[-1])


def main():
    while 1:

        while 1:
            try:
                resposta = int(input(
                    "O que deseja fazer?\n{} - Cadastrar um novo usuario.\n{} - Ver usuarios.\n{} - Cadastrar um novo "
                    "emprestimo.\n{} - Ver emprestimos.\n{} - Cadastrar novo livro.\n{} - Ver livros.\n{} - "
                    "Sair.\n".format(*possiveisRespostas)))
            except ValueError:
                print("Digite um NUMERO entre {} e {}".format(possiveisRespostas[0], possiveisRespostas[-1]))
            else:
                if resposta not in possiveisRespostas:
                    print("Numero invalido, digite um numero entre {} e {}".format(possiveisRespostas[0],
                                                                                   possiveisRespostas[-1]))
                else:
                    break

        if resposta == 1:
            nome = input("Digite o nome do novo usuario: ")  # todo: limitar respostas
            telefone = input("Digite o telefone do novo usuario: ")
            email = input("Digite o email do novo usuario: ")
            usuarios.append(Pessoa(nome=nome, telefone=telefone, email=email))
            print("Usuario cadastrado!")
            usuarios[-1].mostrar_informacoes()

        elif resposta == 2:
            for usuario in usuarios:
                usuario.mostrar_informacoes()

        elif resposta == 3:
            cadastrar_emprestimo()

        elif resposta == 4:
            for emprestimo in emprestimos:
                emprestimo.mostrar_informacoes()

        elif resposta == 5:
            titulo = input("Digite o titulo do novo livro: ")
            autor = input("Digite o autor do novo livro: ")
            genero = Genero.AVENTURA  # todo: escolher genero
            faixaEtaria = int(input("Digite a faixa etaria do novo livro: "))  # todo: revisar a faixa etaria
            livros.append(Livro(titulo=titulo, autor=autor, genero=genero, faixaEtaria=faixaEtaria))
            print("Livro cadastrado!")
            livros[-1].mostrar_informacoes()

        elif resposta == 6:
            for livro in livros:
                livro.mostrar_informacoes()

        elif resposta == 7:
            break

if __name__ == "__main__":
    main()


