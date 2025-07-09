import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("spanish")


# Descargar recursos de NLTK
#nltk.download('punkt')
#nltk.download('stopwords')

# === 1. Dos colecciones de documentos ===

colecciones = {
    "ia": {
        "doc1": "La inteligencia artificial está revolucionando la tecnología.",
        "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
        "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
        "doc4": "Las redes neuronales son fundamentales en deep learning.",
        "doc5": "El futuro de la IA está en el aprendizaje profundo."
    },
    "civilizaciones": {
        "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
        "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
        "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
        "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
        "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
    }
}

# === 2. Función para limpiar y tokenizar ===
import unicodedata

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def limpiar_tokenizar(texto):
    texto = quitar_tildes(texto.lower())
    tokens = word_tokenize(texto)
    stop_words = set(stopwords.words('spanish'))
    tokens_limpios = [
        stemmer.stem(palabra) for palabra in tokens
        if palabra not in stop_words and palabra not in string.punctuation
    ]
    return set(tokens_limpios)


# === 3. Función para construir el índice invertido ===

def construir_indice(documentos):
    indice = {}
    for doc_id, texto in documentos.items():
        tokens = limpiar_tokenizar(texto)
        for token in tokens:
            if token not in indice:
                indice[token] = set()
            indice[token].add(doc_id)
    return indice

# === 4. Función para obtener documentos de una palabra ===

def obtener_docs(termino, indice):
    return indice.get(termino, set())

# === 5. Procesar consulta booleana ===

def procesar_consulta(consulta, indice, documentos):
    consulta = quitar_tildes(consulta.lower())
    palabras = consulta.split()

    def normalizar(palabra):
        return stemmer.stem(palabra)

    if len(palabras) == 3:
        op1, operador, op2 = map(normalizar, palabras)
        docs1 = obtener_docs(op1, indice)
        docs2 = obtener_docs(op2, indice)
        if operador == 'and':
            return docs1 & docs2
        elif operador == 'or':
            return docs1 | docs2
        elif operador == 'not':
            return docs1 - docs2
    elif len(palabras) == 2 and palabras[0] == 'not':
        docs = obtener_docs(normalizar(palabras[1]), indice)
        return set(documentos.keys()) - docs
    else:
        return obtener_docs(normalizar(palabras[0]), indice)


# === 6. Interacción con el usuario ===

print("Buscador Booleano")
print("Temas disponibles: ia, civilizaciones")

tema = input("Seleccioná el tema para buscar: ").lower()
while tema not in colecciones:
    tema = input("Tema no válido. Elegí 'ia' o 'civilizaciones': ").lower()

documentos = colecciones[tema]
indice_invertido = construir_indice(documentos)

print(f" Índice creado para tema: {tema}")

# Bucle principal
while True:
    entrada = input("Ingrese una consulta booleana (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        break
    resultado = procesar_consulta(entrada, indice_invertido, documentos)
    print("📄 Documentos encontrados:", resultado)
