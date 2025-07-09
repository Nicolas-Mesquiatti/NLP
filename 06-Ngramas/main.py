from funciones import *
#Cargo el corpus
with open("D:/Tecnicas De Procesamiento del habla/N-gramas/CorpusEducacion.txt", "r", encoding="latin-1") as archivo:
    corpus = archivo.read()
if __name__ == "__main__":
    tokens = tokenizar(corpus)
    print("Tokens:", tokens)
    
    #Convertir los tokens a minúsculas
    tokens_lower = [t.lower() for t in tokens]
    #print("2. Minúsculas:", tokens_lower)
    
    #Elimino la puntuación como ".",",", "!", etc.
    tokens_sin_punt = [t for t in tokens_lower if t not in string.punctuation]
    #print("3. Sin puntuación:", tokens_sin_punt)

    #Texto sin stopwords
    texto_limpio = quitarStopwords_eng(tokens)
    #print("Texto sin stopwords:", texto_limpio)

    #Lematizar el texto
    texto_lema = lematizar(texto_limpio)
    #print("Texto lematizado:", texto_lema)

    texto_procesado = " ".join(texto_lema)
    print("Texto procesado:", texto_procesado)
    #Llamo a la función para obtener n-gramas
    ngramas = obtener_ngramas(texto_procesado)
    graficar_ngramas(ngramas)
    graficar_comparacion_ngrams(ngramas)