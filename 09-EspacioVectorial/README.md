# 📊 Trabajo Práctico 9: Similitud de Documentos con Modelo de Espacio Vectorial

Este trabajo implementa un modelo de comparación entre documentos basado en el **espacio vectorial**, utilizando la métrica de **similitud del coseno** sobre representaciones **TF-IDF**.

---

## 📄 Documentos analizados

Se trabajó con tres textos breves sobre animales:

- `doc1`: "El veloz zorro marrón salta sobre el perro perezoso."
- `doc2`: "Un perro marrón persiguió al zorro."
- `doc3`: "El perro es perezoso."

---

## 🔧 Pasos del procesamiento

1. **Preprocesamiento de texto**
   - Conversión a minúsculas
   - Eliminación de *stopwords*
   - Lematización de palabras
   - Tokenización con `nltk` en español

2. **Vectorización TF-IDF**
   - Se transformaron los textos a vectores numéricos que representan la importancia relativa de cada término en cada documento.

3. **Cálculo de similitud del coseno**
   - Se midió cuán similares son los documentos entre sí, con valores entre `0` (nada similar) y `1` (idénticos).

4. **Visualización**
   - Se construyó un **heatmap** (mapa de calor) para visualizar la matriz de similitud.

---

## 🧠 Resultados de similitud

| Comparación      | Similitud |
|------------------|-----------|
| `doc1` vs `doc2` | 0.47      |
| `doc1` vs `doc3` | 0.48      |
| `doc2` vs `doc3` | 0.23      |

- **Tonos oscuros** en el gráfico: mayor similitud  
- **Tonos claros**: menor similitud

---

## 📌 Conclusiones

- `doc1` y `doc2` comparten términos como **"zorro"**, **"perro"** y **"marrón"**, lo que explica su similitud del 47%.
- `doc1` y `doc3` tienen un 48% de similitud debido a términos compartidos como **"el"**, **"perro"** y **"perezoso"**.
- `doc2` y `doc3` son los menos parecidos (23%) ya que uno expresa acción (**"persiguió"**) y el otro un estado (**"es perezoso"**).

---

## 🛠 Herramientas utilizadas

- **Python** como lenguaje principal
- **NLTK** para:
  - Tokenización
  - Stopwords en español
  - Lematización
- **Scikit-learn** (`TfidfVectorizer`, `cosine_similarity`)
- **Matplotlib / Seaborn** para graficar la matriz de similitud

---

## 📁 Archivos involucrados

- `document_similarity.py` o `tp9_similitud.ipynb` (según el formato de entrega)
- Documentos procesados están en código (strings)

---
