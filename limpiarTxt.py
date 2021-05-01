infile = open("ProyectoF.txt", "r")
outfile = open("ProyectoLimpio.txt", "w")

data = infile.readlines()

for n,line in enumerate(data):
    if line.startswith("<cuerpo>"):
       data[n] = "\n"+line.rstrip()
    else:
       data[n]=line.rstrip()
outfile.write(' '.join(data))
infile.close()
outfile.close()