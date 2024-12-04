from typing import NamedTuple
from datetime import datetime, date
from collections import defaultdict
import csv

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos", list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)

def genera_lista_str(texto, delimitador):
    trocitos = texto.strip().split(delimitador)
    transformado = map(lambda trocito: trocito.strip(), trocitos)

    return transformado

def lee_peliculas(fichero):
    res = []

    with open(fichero, "r", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter= ";")
        next(lector)

        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno.strip(), "%d/%m/%Y").date()
            generos = genera_lista_str(generos,",")
            duracion = int(duracion.strip())
            presupuesto = int(presupuesto.strip())
            recaudacion = int(recaudacion.strip())
            reparto = genera_lista_str(reparto,",")

            res.append(Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto))
    
    return res 

def pelicula_mas_ganancias(peliculas, genero=None):
    res = []
    for p in peliculas:
        if p.genero == genero or genero is None:
            ganancias = p.recaudacion - p.presupuesto

            res.append( (p.titulo, ganancias) )
    
    return max(res, key= lambda tupla: tupla[1])

def anyos_estrenos(peliculas,pelicula):
    res = []
    
    for p in peliculas:
        if pelicula in p.titulo:
            res.append(p.fecha_estreno.year())

    return res

def top_n_directores_mas_prolificos(peliculas, n=1):
    directores = defaultdict(int)

    for p in peliculas:
        directores[p.director] += 1
    
    return sorted(directores.items(), key= lambda tupla: tupla[1], reverse= True)[:n]