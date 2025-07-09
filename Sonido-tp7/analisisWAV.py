import librosa
import numpy as np
np.set_printoptions(threshold=np.inf)#para que se muestre el vector completo
import matplotlib.pyplot as plt
import pygame#utilizo pygame para reproducir el audio ya que #%% librosa no lo reproduce y eso es en spyder
import soundfile as sf
import pygame
import soundfile as sf


# Cargar el archivo de audio
audio_path = "AnalisisTextos.wav" 
y, sr = librosa.load(audio_path, sr=None)

# Mostrar el vector completo de la señal
#np.savetxt("vector_audio.txt", segmento)# Guardar el segmento en un archivo de texto

# 4) a)Vector de la señal segmentada
segmento = y[:50]  #Si traigo los primeros 50 elementos se escucha en silencio y me devuelve un vector de 50 ceros
print("Vector en inicio de audio , que se encuentra silencios :", segmento)

segmento = y[80000:80500]  # Devuelve valor de 500 elementos ya que no hay silencio
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
pygame.mixer.music.load("AnalisisTextos.wav")
pygame.mixer.music.play()

# Esperar hasta que termine la reproducción
while pygame.mixer.music.get_busy():
    continue


#7) Cambiar la frecuencia de muestreo del audio
# Inicializar pygame
#Printeo los khz de cada audio reproducidos
data_menos, sr_menos = sf.read("output_menos.wav")
data_mas, sr_mas = sf.read("output_mas.wav")
pygame.init()
pygame.mixer.init()

# Reproducir el archivo con frecuencia reducida
pygame.mixer.music.load("output_menos.wav")
pygame.mixer.music.play()
print("Reproduciendo: Audio con frecuencia reducida")
print("Frecuencia de muestreo reducida:", sr_menos, "Hz")
# Esperar a que termine
while pygame.mixer.music.get_busy():
    continue

# Reproducir el archivo con frecuencia aumentada
pygame.mixer.music.load("output_mas.wav")
pygame.mixer.music.play()
print("Reproduciendo: Audio con frecuencia aumentada")
print("Frecuencia de muestreo aumentada:", sr_mas, "Hz")

# Esperar a que termine
while pygame.mixer.music.get_busy():
    continue

print("Reproducción completada")


#8)Bajar la calidad del audio
# Reproducir el archivo de audio con calidad reducida En este caso, se reproduce el archivo "AnalisisTextos_modificado.wav" que tiene 16.0 kHz de frecuencia de muestreo

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("AnalisisTextos_modificado.wav")
pygame.mixer.music.play()

print("Reproduciendo archivo de calidad reducida...")

while pygame.mixer.music.get_busy():
    continue

print("Reproducción completada")

"""  -------------------------------------------------------
                    Graficos extras
     ------------------------------------------------------- 
"""

#Espectograma
# Convertir el audio a un espectrograma
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Visualizar el espectrograma
plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format="%+2.0f dB")
plt.title("Espectrograma")
plt.show()
# Guardar el espectrograma como imagen
#plt.savefig("espectrograma.png")


# Espectro de frecuencias del audio original .wav

# Aplicar la Transformada de Fourier (FFT)
fft = np.fft.fft(y)
frecuencias = np.fft.fftfreq(len(y), 1/sr)

# Tomar solo la mitad del espectro (frecuencias positivas)
fft_magnitud = np.abs(fft[:len(fft)//2])
frecuencias = frecuencias[:len(frecuencias)//2]

# Graficar el espectro
plt.figure(figsize=(10, 5))
plt.plot(frecuencias, fft_magnitud, color="blue")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de frecuencias de AnalisisTextos.wav")
plt.grid()
plt.show()

#GRAFICO ANALISISTEXTOS_MODIFICADO

#ESPECTOGRAMA DEL AUDIO MODIFICADO

# Cargar el audio modificado
y, sr = librosa.load("AnalisisTextos_modificado.wav", sr=None)

# Aplicar STFT y convertir la amplitud a escala logarítmica
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Crear la figura del espectrograma
plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format="%+2.0f dB")
plt.title("Espectrograma de AnalisisTextos_modificado.wav")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")
plt.show()

# Guardar el espectrograma como imagen (opcional)
# plt.savefig("espectrograma_modificado.png")

# Para hacer notar la diferencia entre el espectro de frecuencias del audio original y el modificado que tiene 16kHz de frecuencia de muestreo

# Aplicar la Transformada de Fourier (FFT)
fft = np.fft.fft(y)
frecuencias = np.fft.fftfreq(len(y), 1/sr)

# Tomar solo la mitad del espectro (frecuencias positivas)
fft_magnitud = np.abs(fft[:len(fft)//2])
frecuencias = frecuencias[:len(frecuencias)//2]

# Graficar el espectro
plt.figure(figsize=(10, 5))
plt.plot(frecuencias, fft_magnitud, color="red")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de frecuencias de AnalisisTextos_modificado.wav (16 kHz)")
plt.grid()
plt.show()
