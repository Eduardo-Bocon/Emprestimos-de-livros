from Emprestimo import *


class Pessoa:

    def __init__(self, nome:str, telefone:str, email:str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__emprestimos = list()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novoNome:str):
        self.__nome = novoNome

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, novoTelefone:str):
        self.__telefone = novoTelefone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novoEmail:str):
        self.__email = novoEmail

    @property
    def emprestimos(self) -> list[Emprestimo]:
        return self.__emprestimos

    def add_emprestimo(self, emprestimo:Emprestimo):
        self.__emprestimos.append(emprestimo)

    def remove_emprestimo(self, emprestimo:Emprestimo):
        if emprestimo in self.__emprestimos:
            self.__emprestimos.remove(emprestimo)

    def mostrar_informacoes(self):
        print("Nome: {}\nTelefone: {}\nEmail: {}\n".format(self.nome, self.telefone, self.email))
