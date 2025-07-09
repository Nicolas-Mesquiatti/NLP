import librosa
import numpy as np
import matplotlib.pyplot as plt
import pygame
import soundfile as sf
import os
from pydub import AudioSegment
from pydub.playback import play
import librosa.display

# Cargar el archivo de audio
audio_path = "AnalisisTextos.mp3"  
y, sr = librosa.load(audio_path, sr=None)

# Mostrar el vector completo de la señal
#np.savetxt("vector_audio.txt", segmento)#Guardar el segmento en un archivo de texto

# 4) a)Vector de la señal segmentada
segmento = y[:50]  #Si traigo los primeros 50 elementos se escucha en silencio y me devuelve un vector de 50 ceros
print("Vector en inicio de audio , que se encuentra silencios :", segmento)
segmento = y[70000:70200]  # Devuelve valor de 200 elementos ya que no hay silencio
print("Nuevo segmento de la señal:", segmento)

# 4) b)Cantidad total de muestras
num_elementos = len(y)
print("Cantidad total de muestras:", num_elementos)

# 4) c)Frecuencia de muestreo
print("Frecuencia de muestreo:", sr, "Hz")

# 4) d) Duración del audio en segundos
duracion = librosa.get_duration(y=y, sr=sr)
print("Duración del audio:", duracion, "segundos")

# 5) Imprimir la señal segmentada
plt.plot(segmento)
plt.title("Forma de onda del segmento seleccionado")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()
# Graficar la forma de onda del audio completo
plt.figure(figsize=(12, 5))
librosa.display.waveshow(y, sr=sr)
plt.title("Forma de onda del audio completo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

# 6) Reproducir el audio utilizando pygame
# Inicializar pygame
pygame.init()
print("Reproduciendo archivo de audio original...")

# Cargar y reproducir el audio
pygame.mixer.init()
pygame.mixer.music.load("AnalisisTextos.mp3")
pygame.mixer.music.play()

# Esperar hasta que termine la reproducción
while pygame.mixer.music.get_busy():
    continue

# === 7. Modificar frecuencia de muestreo y reproducir ===

# Más lento
y_lento = librosa.resample(y, orig_sr=sr, target_sr=int(sr / 2))
sf.write("audio_mas_lento.wav", y_lento, int(sr / 2))

# Más rápido
y_rapido = librosa.resample(y, orig_sr=sr, target_sr=int(sr * 1.5))
sf.write("audio_mas_rapido.wav", y_rapido, int(sr * 1.5))

print("Archivos exportados con nueva frecuencia de muestreo.")


# === 8. Reducir calidad y reproducir ===
audio = AudioSegment.from_wav("AnalisisTextos.wav")
audio_baja_calidad = audio.set_frame_rate(8000).set_channels(1)
audio_baja_calidad.export("audio_baja_calidad.mp3", format="mp3", bitrate="32k")

print("Audio exportado en baja calidad (8000 Hz, 32 kbps).")

# === Reproducir los archivos con pygame ===

def reproducir_audio(archivo):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

print("Reproduciendo archivo de menor frecuencia de muestreo...")
reproducir_audio("audio_mas_lento.wav")

print("Reproduciendo archivo de mayor frecuencia de muestreo...")
reproducir_audio("audio_mas_rapido.wav")

print("Reproduciendo archivo de baja calidad...")
reproducir_audio("audio_baja_calidad.mp3")


#ESPECTROGRAMAS Y ESPECTROS DE FRECUENCIAS

# Calcular el espectrograma con STFT
D = np.abs(librosa.stft(y))
# Convertir a escala logarítmica para mejor visualización
D_db = librosa.amplitude_to_db(D, ref=np.max)
# Graficar el espectrograma
plt.figure(figsize=(12, 6))
librosa.display.specshow(D_db, sr=sr, x_axis="time", y_axis="log")
plt.colorbar(format="%+2.0f dB")
plt.title("Espectrograma de AnalisisTextos.mp3")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")
plt.show()

#Grafico de espectro de frecuencias
# Cargar el audio
y, sr = librosa.load("AnalisisTextos.mp3", sr=None)

# Calcular la Transformada de Fourier
fft = np.fft.fft(y)
frecuencias = np.fft.fftfreq(len(y), 1/sr)

# Tomar solo la mitad del espectro (frecuencias positivas)
fft_magnitud = np.abs(fft[:len(fft)//2])
frecuencias = frecuencias[:len(frecuencias)//2]

# Graficar el espectro
plt.figure(figsize=(10, 5))
plt.plot(frecuencias, fft_magnitud)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de frecuencias de AnalisisTextos.mp3")
plt.grid()
plt.show()
