import os
import math

def run():
    
  infile =  open("stemming.txt", 'r')
  documents = infile.readlines()

#---Calculate term frequency --

#First: tokenize words
  dictOfWords = {}

  for index, sentence in enumerate(documents):
    tokenizedWords = sentence.split(' ')
    dictOfWords[index] = [(word,tokenizedWords.count(word)) for word in tokenizedWords]
    

  #print(dictOfWords)
  #second: remove duplicates
  termFrequency = {}

  for i in range(0, len(documents)):
      listOfNoDuplicates = []
      for wordFreq in dictOfWords[i]:
          if wordFreq not in listOfNoDuplicates:
              listOfNoDuplicates.append(wordFreq)
          termFrequency[i] = listOfNoDuplicates
  #print(termFrequency)

  #Third: normalized term frequency
  normalizedTermFrequency = {}
  for i in range(0, len(documents)):
      sentence = dictOfWords[i]
      lenOfSentence = len(sentence)
      listOfNormalized = []
      for wordFreq in termFrequency[i]:
          normalizedFreq = wordFreq[1]/lenOfSentence
          listOfNormalized.append((wordFreq[0],normalizedFreq))
      normalizedTermFrequency[i] = listOfNormalized

  #print(normalizedTermFrequency)


  #---Calculate IDF

  #First: put al sentences together and tokenze words

  allDocuments = ''
  for sentence in documents:
      allDocuments += sentence + ' '
  allDocumentsTokenized = allDocuments.split(' ')

  #print(allDocumentsTokenized)

  allDocumentsNoDuplicates = []

  for word in allDocumentsTokenized:
      if word not in allDocumentsNoDuplicates:
          allDocumentsNoDuplicates.append(word)


  #print(allDocumentsNoDuplicates)

  #Second calculate the number of documents where the term t appears

  dictOfNumberOfDocumentsWithTermInside = {}

  for index, voc in enumerate(allDocumentsNoDuplicates):
      count = 0
      for sentence in documents:
          if voc in sentence:
              count += 1
      dictOfNumberOfDocumentsWithTermInside[index] = (voc, count)

  #print(dictOfNumberOfDocumentsWithTermInside)


  #calculate IDF

  dictOFIDFNoDuplicates = {}


  for i in range(0, len(normalizedTermFrequency)):
      listOfIDFCalcs = []
      for word in normalizedTermFrequency[i]:
          for x in range(0, len(dictOfNumberOfDocumentsWithTermInside)):
              if word[0] == dictOfNumberOfDocumentsWithTermInside[x][0]:
                  listOfIDFCalcs.append((word[0],math.log(len(documents)/dictOfNumberOfDocumentsWithTermInside[x][1])))
      dictOFIDFNoDuplicates[i] = listOfIDFCalcs

  #print(dictOFIDFNoDuplicates)

  #Multiply tf by idf for tf-idf

  dictOFTF_IDF = {}
  for i in range(0,len(normalizedTermFrequency)):
      listOFTF_IDF = []
      TFsentence = normalizedTermFrequency[i]
      IDFsentence = dictOFIDFNoDuplicates[i]
      for x in range(0, len(TFsentence)):
          listOFTF_IDF.append((TFsentence[x][0],TFsentence[x][1]*IDFsentence[x][1]))
      dictOFTF_IDF[i] = listOFTF_IDF
  
  print(dictOFTF_IDF[0])
  #Cosine similarity
  #for i in dictOFTF_IDF:
  v1=dictOFTF_IDF[0]
  v2=dictOFTF_IDF[0]
  
  aux = 0
  raiz1= 0
  raiz2= 0
  #print(v1[0][1])

  for i in range(len(v1)):
    aux=aux+(v1[i][1]*v2[i][1])
    raiz1=raiz1+(v1[i][1]**2)
    raiz2=raiz2+(v2[i][1]**2)
  raiz1=math.sqrt(raiz1)
  raiz2=math.sqrt(raiz2)
  raiz=raiz1*raiz2
  vector=[]
  print(aux/raiz)
  print(len(allDocumentsNoDuplicates))
  for index in allDocumentsNoDuplicates:
    print(index)
  listOfv1={}
  listOfv1.append((wordFreq[0],normalizedFreq))
  print(vector)
if __name__ == '__main__':
    run()