# **Bases de Conocimiento en Prolog**  
**Trabajo Práctico 3: Representación del Conocimiento**

Resolución de ejercicios teóricos y prácticos utilizando **Prolog**. Se analiza la estructura de los términos, se identifican hechos, reglas y predicados, y se escriben consultas sobre bases de conocimiento.

---

🔧 **Etapas del análisis**

### **Ejercicio 1.1**
- Clasificación de secuencias de caracteres como:
  - **Átomos**
  - **Variables**
  - **No términos válidos**
- Evaluación individual y marcado de cada caso según la sintaxis de Prolog

### **Ejercicio 1.2**
- Identificación de:
  - **Átomos**
  - **Variables**
  - **Términos complejos**
  - **Secuencias no válidas**
- Para cada término complejo:
  - Se determina el **funtor**
  - Se especifica su **aridad**

### **Ejercicio 1.3**
- Análisis de una base de conocimientos con hechos y reglas
- Cálculo de:
  - **Cantidad de hechos**: 3  
  - **Cantidad de reglas**: 4  
  - **Cantidad total de cláusulas**: 7  
  - **Cantidad total de predicados**: 7
- Identificación de los **encabezados de reglas** y sus **objetivos**, como por ejemplo:
  - `person(X) :- man(X); woman(X).`
  - `loves(X, Y) :- father(X, Y).`
  - `father(Y, Z) :- man(Y), son(Z, Y).`
  - `father(Y, Z) :- man(Y), daughter(Z, Y).`

### **Ejercicio 1.4**
- Representación en Prolog de una **base de conocimientos** provista en lenguaje natural
- Traducción de hechos y relaciones utilizando la sintaxis formal del lenguaje

### **Ejercicio 1.5**
- Resolución de consultas sobre una base de datos existente
- Respuestas esperadas por Prolog ante cada consulta, incluyendo:
  - Evaluaciones que resultan en `true` o `false`
  - Unificación de variables como: `Y = ron`

---

📁 **Archivos utilizados**
- Documento de ejercicios con soluciones desarrolladas
- Base de conocimientos escrita en sintaxis de Prolog
- Ejemplos de consultas y sus respectivas respuestas

---

🛠 **Herramientas utilizadas**
- **Prolog** para representar conocimiento, definir reglas y ejecutar consultas  
- Análisis manual para interpretar resultados y evaluar lógica de programación declarativa

---

✅ Este trabajo práctico fortalece los conceptos fundamentales de **representación del conocimiento en lógica de primer orden**, permitiendo modelar relaciones y realizar inferencias a partir de reglas lógicas en Prolog.
