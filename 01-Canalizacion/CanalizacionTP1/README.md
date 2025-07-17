# Pipeline
**Trabajo Práctico 1: TF-IDF (Term Frequency-Inverse Document Frequency)**

Construir un pipeline de procesamiento de lenguaje natural para analizar el corpus CorpusLenguajes.txt, aplicando técnicas de limpieza, representación y visualización textual.
🔧 Etapas del Pipeline
- Preprocesamiento del texto:
  Eliminación de stopwords
  Lematización de palabras
- Vectorización del texto:
  Cálculo de la matriz TF-IDF
- Exploración del corpus:
 Visualización del corpus ya procesado
  Inspección de la matriz TF-IDF
  Generación del vocabulario extraído
- Análisis estadístico:
  Jerarquía de las 6 palabras más frecuentes
  Palabra menos utilizada en el corpus
  Palabras más repetidas dentro de una misma oración
- Visualización:
  Gráfico de distribución de frecuencia de las palabras


  
📁 Archivos utilizados
- CorpusLenguajes.txt: archivo fuente con los datos a analizar
- Script de Python para ejecutar todo el pipeline

Heramientas utilizadas
Python como lenguaje de programación principal.
- NLTK para:
  - eliminación de stopwords
  - lematización
  - tokenización
- scikit-learn (TfidfVectorizer) para generar la matriz TF-IDF y extraer el vocabulario.
- matplotlib y/o seaborn para visualizar la distribución de frecuencia en gráficos.
