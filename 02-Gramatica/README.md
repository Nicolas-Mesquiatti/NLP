# **Gramáticas Libres de Contexto**  
**Trabajo Práctico 2: Lenguajes y Autómatas**

Análisis formal de una **gramática libre de contexto (GLC)**, respondiendo preguntas teóricas sobre sus componentes, derivaciones y cadenas generadas.

---

🔧 **Etapas del análisis**

### **Identificación de la gramática G**
- **Variables**: R, S, T, X  
- **Terminales**: a, b  
- **Símbolo inicial**: R

### **Generación y verificación de cadenas**
- Producción de **cadenas válidas** (como `aab`, `bba`, `aababa`)
- Verificación de **derivaciones directas** e **indirectas**
- Evaluación de afirmaciones como:  
  - `T ⇒ aba`  
  - `XXX ⇒* aba`  
  - `S ⇒* ε`


- **Variables**: R, S, T, X  
- **Terminales**: a, b  
- **Símbolo inicial**: R

### **Análisis solicitado**
- Determinación de la **cantidad de variables y terminales**
- Identificación del **símbolo inicial**
- Generación de **tres cadenas válidas** del lenguaje L(G)
- Obtención de la **cadena mínima posible**
- Evaluación lógica de afirmaciones de derivación directa (`⇒`) e indirecta (`⇒*`), tales como:
  - `T ⇒ aba`
  - `T ⇒* aba`
  - `T ⇒ T`
  - `T ⇒* T`
  - `XXX ⇒* aba`
  - `X ⇒* aba`
  - `T ⇒* XX`

---

📁 **Archivos utilizados**
- Documento con desarrollo de ejercicios teóricos y análisis de la gramática  
- Resolución paso a paso de cada ítem solicitado

---

🛠 **Herramientas utilizadas**
- **Análisis manual** de producciones y derivaciones  
- Representación simbólica de cadenas y reglas de producción  
- Uso de notación formal: `⇒` (derivación directa) y `⇒*` (derivación en varios pasos)

---

✅ Este trabajo práctico fortalece la comprensión del **funcionamiento interno de las GLC**, analizando cómo se generan cadenas y evaluando propiedades sintácticas del lenguaje formal.
