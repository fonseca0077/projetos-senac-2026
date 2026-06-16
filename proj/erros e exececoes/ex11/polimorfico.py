class AnatomiaError(Exception):
    pass


class Instrumento:
    def tocar(self):
        raise AnatomiaError(
            "Classes abstratas não tocam som. Use uma classe concreta."
        )


class Guitarra(Instrumento):
    def tocar(self):
        return " A guitarra está tocando uma melodia."
    