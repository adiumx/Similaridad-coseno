with open('Preprocesamiento.txt', encoding='utf8',mode='r') as input:
  for index, line in enumerate(input):
      with open('filename{}.txt'.format(index), encoding='utf8',mode='w') as output:
          output.write(line)