# 🧠 Trabajo Práctico 8: Búsquedas Booleanas con Python y NLTK

Este trabajo implementa un sistema de **búsqueda booleana (AND, OR, NOT)** en Python, utilizando procesamiento de lenguaje natural con **NLTK**, aplicado a dos conjuntos de documentos: uno sobre **Inteligencia Artificial** y otro sobre **Civilizaciones Antiguas**.

---

## 🔍 Objetivo

Permitir que el usuario realice búsquedas booleanas interpretables en lenguaje natural, devolviendo los documentos relevantes a partir de un **índice invertido**.

---

## 📄 Conjuntos de Documentos

### 📘 Inteligencia Artificial (`ia`)
- `doc1`: La inteligencia artificial está revolucionando la tecnología.
- `doc2`: El aprendizaje automático es clave en la inteligencia artificial.
- `doc3`: Procesamiento del lenguaje natural y redes neuronales.
- `doc4`: Las redes neuronales son fundamentales en deep learning.
- `doc5`: El futuro de la IA está en el aprendizaje profundo.

### 📕 Civilizaciones Antiguas (`civilizaciones`)
- `doc1`: Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.
- `doc2`: La civilización romana fue una de las más influyentes en la historia occidental.
- `doc3`: Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.
- `doc4`: La antigua Grecia sentó las bases de la democracia y la filosofía moderna.
- `doc5`: Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades.

---

## ⚙️ Funcionalidades implementadas

- 🔹 **Tokenización y limpieza** de documentos:
  - Conversión a minúsculas
  - Eliminación de stopwords, puntuación y tildes (acentos)
  - Lematización para mejorar la búsqueda (ej. "romano" vs "romana")

- 🔹 **Índice invertido**:
  - Asocia cada palabra clave con los documentos donde aparece

- 🔹 **Procesamiento de consultas booleanas**:
  - Permite usar `AND`, `OR`, `NOT` para combinar términos
  - Devuelve los documentos coincidentes

- 🔹 **Interacción dinámica con el usuario**:
  - Elige tema (`ia` o `civilizaciones`)
  - Escribe la consulta booleana
  - El sistema responde los documentos encontrados

---

## 🧪 Ejemplos de consultas válidas

### 🔍 Conjunto IA
- `inteligencia AND artificial` → `{'doc1', 'doc2'}`
- `redes OR aprendizaje` → `{'doc2', 'doc3', 'doc4', 'doc5'}`
- `inteligencia NOT automático` → `{'doc1'}`

### 🔍 Conjunto Civilizaciones
- `egipcios AND pirámides` → `{'doc1'}`
- `escritura OR astrónomos` → `{'doc1', 'doc3', 'doc5'}`
- `romano NOT griegos` → `{'doc2'}` *(requiere lematización para funcionar correctamente)*

---

## 🛠 Herramientas utilizadas

- **Python** como lenguaje principal  
- **NLTK** para:
  - Tokenizar texto
  - Eliminar stopwords
  - Lematizar palabras
- **Unidecode** para eliminar acentos
- Estructuras de datos como conjuntos y diccionarios para optimizar búsquedas

---

## ✅ Conclusión

Este trabajo permitió entender cómo construir un motor de búsqueda booleano básico con Python, aplicando técnicas de NLP para mejorar la precisión. La limpieza de texto y la lematización fueron claves para que las consultas se interpreten correctamente, incluso con variaciones gramaticales o acentos.
