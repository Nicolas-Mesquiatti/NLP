# **Análisis Digital de Audio con Python y FFmpeg**  
**Trabajo Práctico 7: Procesamiento y Visualización de Señales Sonoras**

Análisis del archivo `AnalisisTextos.mp3` mediante herramientas como **MediaInfo**, **FFmpeg** y **Python**. Se estudian propiedades del audio, se realiza un sampleo, se reproducen señales y se visualizan espectros.

---

## 🔍 1. Análisis inicial con MediaInfo

- **Formato**: MPEG audio  
- **Tasa de bits**: 256 kb/s  
- **Canales**: 1  
- **Frecuencia de muestreo**: 48.0 kHz

---

## 🔁 2. Sampleo del audio con FFmpeg

- Conversión a `.wav` (sin compresión)  
- Generación de otro `.wav` con:
  - **2 canales**
  - **Frecuencia de muestreo**: 16.0 kHz

---

## 📊 3. Reanálisis con MediaInfo

### WAV original:
- Formato: Wave  
- Tasa de bits: 768 kb/s  
- Canales: 1  
- Frecuencia: 48.0 kHz

### WAV modificado:
- Formato: Wave  
- Tasa de bits: 512 kb/s  
- Canales: 2  
- Frecuencia: 16.0 kHz

> 📌 *Conclusión:* A menor frecuencia de muestreo, el sonido se degrada. Aumentar los canales no mejora la calidad si la fuente era mono.

---

## 🐍 4. Análisis con Python

### Librerías usadas:
`librosa`, `numpy`, `matplotlib`, `pygame`, `soundfile`, `pydub`

### Funcionalidades implementadas:
- Carga de audios (`.mp3` y `.wav`)
- Extracción de:
  - Vector de señal segmentada
  - Cantidad de muestras
  - Frecuencia de muestreo
  - Duración en segundos
- Gráficos:
  - Forma de onda (completa y segmentada)
  - Espectro de frecuencias
  - Espectrograma (STFT con `n_fft = 4096` y `16384`)
- Reproducción de audio con `pygame`
- Resampleo del audio para modificar duración
- Reducción de calidad con `pydub`

> 🎧 *Conclusión técnica:* El `.wav` conserva más información que el `.mp3`, pero la diferencia es más notable en análisis gráfico que auditivo.

---

## ✅ Conclusiones generales

- La frecuencia de muestreo influye directamente en la calidad del audio.
- La representación visual permite detectar diferencias sutiles en señales.
- El uso de herramientas como Python, `ffmpeg` y `MediaInfo` facilita un análisis completo desde lo técnico hasta lo perceptual.

---

## 📁 Archivos utilizados

- `AnalisisTextos.mp3`
- `AnalisisTextos.wav`
- `AnalisisTextos_modificado.wav`
- Script de Python (`.ipynb` o `.py`) con todo el procesamiento

