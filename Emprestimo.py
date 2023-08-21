from Livro import *


class Emprestimo:

    def __init__(self, livro: Livro, dataEmprestimo: str):
        self.__livro = livro
        self.__dataEmprestimo = dataEmprestimo

    @property
    def livro(self) -> Livro:
        return self.__livro

    @property
    def dataEmprestimo(self) -> str:
        return self.__dataEmprestimo

    @dataEmprestimo.setter
    def dataEmprestimo(self, novaData: str):
        self.__dataEmprestimo = novaData

    def mostrar_informacoes(self):
        print("Livro: {}\nData do emprestimo: {}\n".format(self.livro.titulo, self.dataEmprestimo))
