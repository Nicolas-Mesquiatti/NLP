import nltk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documentos
documentos = {
    "doc1": "El veloz zorro marrón salta sobre el perro perezoso.",
    "doc2": "Un perro marrón persiguió al zorro.",
    "doc3": "El perro es perezoso."
}

nombres_docs = list(documentos.keys())
textos = list(documentos.values())

# Vectorización con TF-IDF y stopwords en español
stopwords_es = stopwords.words('spanish')
vectorizador = TfidfVectorizer(stop_words=stopwords_es)
tfidf_matrix = vectorizador.fit_transform(textos)

# Similaridad coseno
similitud = cosine_similarity(tfidf_matrix)

# Mostrar resultados
print("📊 Matriz de similitud:")
print(np.round(similitud, 2))

# Graficar
# Graficar
plt.figure(figsize=(6, 5))

sns.heatmap(similitud, annot=True,
            xticklabels=nombres_docs,
            yticklabels=nombres_docs,
            cmap="Greys",  # <- cambio hecho acá
            fmt=".2f")

plt.title("Matriz de Similitud (Coseno)")
plt.show()
