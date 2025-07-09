#1)Realizamos las importaciones
import nltk #Biblioteca principal que usamos
import string  # Para manejar puntuación
from nltk.tokenize import word_tokenize, sent_tokenize  # Tokenización de palabras y oraciones
from nltk.corpus import stopwords  # Stopwords para eliminar palabras comunes
from nltk.stem import WordNetLemmatizer  # Lematización para reducir palabras a su forma base
from nltk.corpus import wordnet  # Para mejorar la lematización
from nltk import FreqDist
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from sklearn.feature_extraction.text import TfidfVectorizer
import re

#CANALIZACION HACIENDO QUE TRAIGA SOLO LAS ORACIONES 


# Abrimos el archivo y leemos su contenido
with open("d:\\zoom9-04\\CanalizacionTP1\\CorpusLenguajes.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

# Usamos una expresión regular para extraer solo las oraciones entre paréntesis y comillas dobles
oraciones = re.findall(r'\("([^"]*?)"\)', contenido)
texto = " ".join(oraciones)

#Funcion tokenizar
def tokenizar(texto):
    # Tokenizamos el texto en palabras
    tokens = word_tokenize(texto)
    return tokens

texto_tokenizado =tokenizar(texto)
print("texto tokenizado : ",texto_tokenizado)


#Función para quitar stopwords
def quitarStopwords_eng(texto):
    ingles = stopwords.words("spanish")  # Cambié a español para el corpus de educación
    texto_limpio = [
        w.lower() for w in texto 
        if w.lower() not in ingles
        and w not in string.punctuation
        and not any(c in w for c in ["|", "--", "''", "``", "()", "_", "-"])  # Verifica caracteres no deseados
    ]
    return texto_limpio

print("-"*70)
texto_limpio = quitarStopwords_eng(texto_tokenizado)
#Printeo el texto sin las palabras vacias
print("Texto sin stopwords:", texto_limpio)

# Defino la función para obtener el pos de una palabra
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
#Defino la función para lematizar el texto
def lematizar(texto):
    texto_lema = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
    return texto_lema

#Inicio el lematizador
lemmatizer = WordNetLemmatizer()
print("-"*70)
print("Texto lematizado:", lematizar(texto_limpio))

#Tf - idf
vectorizer = TfidfVectorizer()
#De corpus use las oraciones del txt
X = vectorizer.fit_transform(oraciones)
#aca printeo la matriz
print("Matriz TF-IDF:")
print(X.toarray())
#aca printeo el vocabulario
print("\nVocabulario:")
print(vectorizer.get_feature_names_out())

# Obtener las 6 palabras más usadas en todo el corpus
frecuencia = FreqDist(lematizar(quitarStopwords_eng(texto_limpio)))
palabras_mas_usadas = frecuencia.most_common(6)
print(palabras_mas_usadas)
# Obtener la palabra menos utilizada
palabra_menos_usada = min(frecuencia, key=frecuencia.get)
# Imprimir la palabra menos utilizada
print(f"\nLa palabra menos utilizada es: '{palabra_menos_usada}'")

# Analizar palabras más repetidas en cada oración
for i, oracion in enumerate(oraciones):
    # Tokenizar y procesar cada oración
    tokens_oracion = lematizar(quitarStopwords_eng(word_tokenize(oracion)))
    frecuencia_oracion = FreqDist(tokens_oracion)
    
    # Obtener la palabra más repetida en la oración
    palabra_mas_repetida = frecuencia_oracion.most_common(1)
    
    # Imprimir el resultado
    if palabra_mas_repetida:
        print(f"\nEn la oración {i + 1}, la palabra más repetida es: '{palabra_mas_repetida[0][0]}' con una frecuencia de {palabra_mas_repetida[0][1]}") 
    
    
#Grafico sin quitar las stopwords
frecuencia=FreqDist(texto_tokenizado)
frecuencia.plot(20, show=True)
#Grafico quitando las stopwords y lematizado
frecuencia=FreqDist(lematizar(quitarStopwords_eng(texto_limpio)))
frecuencia.plot(20, show=True)