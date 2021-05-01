import re

signos = ("?", "¿", "¡", "!", "(", ")", ",", ".", ";", ":", "...", "/", "'", "-", "%", "…", "–", "’", '"', "”", "“", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

infile2 = open("ProyectoF.txt", "r")
texto = infile2.readlines()
texto=texto.lower()

outfile = open("stopWords.txt", "r")
texto=texto.split()
stopWords = outfile.readlines()

texto.replace('a',' ')
infile2.close()
outfile.close()