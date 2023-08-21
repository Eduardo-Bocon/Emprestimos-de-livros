from enum import Enum


class Genero(Enum):
    COMEDIA = "Comédia"
    ROMANCE = "Romance"
    AVENTURA = "Aventura"
    TERROR = "Terror"
    FICCAO_CIENTIFICA = "Ficção Cientifica"
    BIOGRAFIA = "Biografia"
    INFANTIL = "Infantil"
    OUTROS = "Outros"

    def __str__(self):
        return self.value
