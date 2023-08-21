from Pessoa import *
from Genero import *
from datetime import date

usuarios = list()
livros = list()
emprestimos = list()

today = date.today()

resposta = 0
possiveisRespostas = [1, 2, 3, 4, 5, 6, 7]

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
        nome = input("Digite o nome do novo usuario: ") # todo: limitar respostas
        telefone = input("Digite o telefone do novo usuario: ")
        email = input("Digite o email do novo usuario: ")
        usuarios.append(Pessoa(nome=nome, telefone=telefone, email=email))
        print("Usuario cadastrado!")
        usuarios[-1].mostrar_informacoes()

    elif resposta == 2:
        for usuario in usuarios:
            usuario.mostrar_informacoes()

    elif resposta == 3:
        tituloLivro = input("Qual livro? ")
        for livro in livros:
            if livro.titulo == tituloLivro:
                print("Livro encontrado.\n")
                resposta = int(input("1 - Colocar data atual.\n2 - Colocar data manualmente.\n")) # todo: colocar data manualmente
                if resposta == 1:
                    emprestimos.append(Emprestimo(livro, today.strftime("%d/%m/%y")))

        emprestimos[0].mostrar_informacoes()

    elif resposta == 4:
        for emprestimo in emprestimos:
            emprestimo.mostrar_informacoes()

    elif resposta == 5:
        titulo = input("Digite o titulo do novo livro: ")
        autor = input("Digite o autor do novo livro: ")
        genero = Genero.AVENTURA  # todo: escolher genero
        faixaEtaria = int(input("Digite a faixa etaria do novo livro: ")) # todo: revisar a faixa etaria
        livros.append(Livro(titulo=titulo, autor=autor, genero=genero, faixaEtaria=faixaEtaria))
        print("Livro cadastrado!")
        livros[-1].mostrar_informacoes()

    elif resposta == 6:
        for livro in livros:
            livro.mostrar_informacoes()

    elif resposta == 7:
        break
