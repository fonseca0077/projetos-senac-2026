from playlist import Playlist

if __name__ == '__main__':

    playlist = Playlist('fonseca')
    playlist.adicionar_musica('she')
    playlist.adicionar_musica('introducion')
    playlist.remover_musica('introducion')
    playlist.mostrar_playlist()