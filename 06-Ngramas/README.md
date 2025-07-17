# **Modelos de N-gramas**  
**Trabajo Práctico 6: Análisis de 2-gramas y 3-gramas**

Análisis del corpus **CorpusEducacion.txt**, que contiene opiniones de alumnos colombianos sobre la educación superior en 2025. Se comparan modelos de **2-gramas** y **3-gramas** mediante visualizaciones.

---

🔧 **Etapas del análisis**

- **Preprocesamiento del texto**:  
  - Tokenización  
  - Lematización  
  - Eliminación de stopwords  

- **Construcción de modelos N-grama**:  
  - Extracción y conteo de 2-gramas y 3-gramas  
  - Definición de frecuencia mínima de aparición: **min_df = 2**

- **Visualización**:  
  - Gráfico de barras comparativo mostrando las frecuencias de los N-gramas más comunes

- **Organización del código**:  
  - Estructuración en funciones para modularidad y claridad

---

📁 **Archivos utilizados**

- `CorpusEducacion.txt`: corpus con opiniones reales de estudiantes  
- Script o notebook con el código de procesamiento, análisis y visualización

---

🛠 **Herramientas utilizadas**

- **Python** con bibliotecas:  
  - `nltk` o `spaCy` para tokenización, lematización y stopwords  
  - `scikit-learn` para extracción y conteo de N-gramas  
  - `matplotlib` o `seaborn` para gráficos

---

✅ **Conclusión**  
El trabajo permite comparar y visualizar la frecuencia de N-gramas en un corpus real, facilitando la identificación de patrones y expresiones comunes en las opiniones sobre educación superior.
