import nltk
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

#Primero Tokenizamos
def tokenizar(texto):
    # Tokenizamos el texto en palabras
    tokens = word_tokenize(texto)
    return tokens

# Segundo quitamos las stopwords
def quitarStopwords_eng(texto):
    ingles = stopwords.words("spanish")  # Cambié a español para el corpus de educación
    texto_limpio = [
        w.lower() for w in texto 
        if w.lower() not in ingles
        and w not in string.punctuation
        and not any(c in w for c in ["|", "--", "''", "``", "()", "_", "-","...","2025"])  # Verifica caracteres no deseados
    ]
    return texto_limpio

# Tercero lematizamos
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
def lematizar(texto):
    texto_lema = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
    return texto_lema

#tenemos que inicializar el lemmatizer
lemmatizer = WordNetLemmatizer()

#Obtener n-gramas
def obtener_ngramas(oraciones_limpias):
    oraciones_limpias = oraciones_limpias.split(".")  # Divide en oraciones
    vectorizer = CountVectorizer(ngram_range=(2, 3), min_df=1, max_df=0.9)
    X = vectorizer.fit_transform(oraciones_limpias)  
    vocab = vectorizer.get_feature_names_out()
    counts = X.toarray().sum(axis=0)
    freqs = Counter(dict(zip(vocab, counts)))
    #print(list(freqs.keys()))
    print("\nCantidad de N-Gramas (bi-gramas y tri-gramas con al menos 2 repeticiones):",len(freqs))
    return freqs

def graficar_ngramas(freqs):
    # Obtener los 10 n-gramas más frecuentes
    top_10_ngrams = dict(freqs.most_common(10))

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(top_10_ngrams.keys(), top_10_ngrams.values(), color='skyblue')
   
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.title("Top 10 N-Gramas más frecuentes")
    plt.xlabel("N-Gramas")
    plt.ylabel("Frecuencia")

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def graficar_comparacion_ngrams(freqs, top_n=20):
    top = freqs.most_common(top_n)
    ngrams, values2 = zip(*top) if top else ([], [])
    np.arange(len(ngrams))
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.barh(ngrams[::-1], values2[::-1], color='skyblue')
    plt.title("Top 2-gramas y 3-gramas")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.show()


"""
def obtener_ngramas(texto_procesado, n):
    vectorizer = CountVectorizer(ngram_range=(n, n), min_df=2)
    ngram_freq = vectorizer.fit_transform(texto_procesado.split("\n"))
    ngram_names = vectorizer.get_feature_names_out()
    freqs = ngram_freq.toarray().sum(axis=0)
    return dict(zip(ngram_names, freqs))
def graficar_comparacion(ngrams_2, ngrams_3):
    plt.figure(figsize=(12, 6))
"""