from Genero import *


class Livro:

    def __init__(self, titulo:str, autor:str, genero:Genero, faixaEtaria:int, resumo="", personagemPrincipal=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__faixaEtaria = faixaEtaria
        self.__resumo = resumo
        self.__personagemPrincipal = personagemPrincipal

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, novoTitulo:str):
        self.__titulo = novoTitulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, novoResumo:str):
        self.__resumo = novoResumo

    @property
    def autor(self) -> str:
        return self.__autor

    @autor.setter
    def autor(self, novoAutor:str):
        self.__autor = novoAutor

    @property
    def personagemPrincipal(self) -> str:
        return self.__personagemPrincipal

    @personagemPrincipal.setter
    def personagemPrincipal(self, novoPersonagem:str):
        self.__personagemPrincipal = novoPersonagem

    @property
    def genero(self) -> Genero:
        return self.__genero

    @genero.setter
    def genero(self, novoGenero:Genero):
        self.__genero = novoGenero

    @property
    def faixaEtaria(self) -> int:
        return self.__faixaEtaria

    @faixaEtaria.setter
    def faixaEtaria(self, novaFaixaEtaria:int):
        self.__faixaEtaria = novaFaixaEtaria

    def mostrar_informacoes(self):
        print("Nome: {}\nAutor: {}\nGenero: {}\nFaixa etaria: {}\n".format(self.titulo, self.autor, self.genero, self.faixaEtaria))
