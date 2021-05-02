from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
infile = open("ProyectoF.txt", "r")
outfile = open("ProyectoF1.txt", "w")

vec1 = np.array([[2,0,1]])
vec2 = np.array([[1,1,1]])

texto = infile.readlines()

stop_words = get_stop_words('spanish')

vectorizer= CountVectorizer()
data=['yo quiero aquel gato','yo quiero un perro','yo quiero aquel perro','yo quiero aquel perico','yo quiero aquel gato','yo quiero gato']
x = vectorizer.fit_transform(data)


tfidf= TfidfVectorizer().fit_transform(texto)


ndarray = tfidf.toarray()
listOflist = ndarray.tolist()
str1=" ".join(str(x) for x in listOflist)
outfile.write(str1)
infile.close()
outfile.close()
#print(cosine_similarity(tfidf[0:1], tfidf).flatten())
