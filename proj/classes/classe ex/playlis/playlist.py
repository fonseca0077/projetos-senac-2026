class Playlist:

    nome:str

    def __init__(self, nome:str):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, nome_musica):
        self.musicas.append(nome_musica)

    def remover_musica(self, nome_musica): 
        if nome_musica in self.musicas:
            self.musicas.remove(nome_musica) 
        else:
            return "Não foi encontrada"    
        
    def mostrar_playlist(self):
        print(self.nome)
        for musica in self.musicas:
            print(musica)
