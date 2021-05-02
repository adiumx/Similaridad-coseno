#oracion = "el ciclo escolar comienza en las escuelas. escuelas de todo el país comenzarán clases este lunes."
import snowballstemmer
stemmer = snowballstemmer.stemmer('spanish');

#print(stemmer.stemWords(oracion.split()));

import os
outfile = open("stemming.txt", "w")
basepath = './dataset'
lista = []

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            infile = open(entry, "r")
            for line in infile:
                listToStr = ' '.join(map(str, stemmer.stemWords(line.split())))
                outfile.write(listToStr+'\n')
