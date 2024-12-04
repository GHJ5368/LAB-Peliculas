from peliculas import *

if __name__ == "__main__":
    datos = lee_peliculas("LAB-Peliculas\data\peliculas.csv")
    
    print(top_n_directores_mas_prolificos(datos, 4))

