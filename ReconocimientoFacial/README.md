# Reconocedor de rostros

### Pasos que se siguieron:

1. **Agregar las imágenes con las que se va a entrenar el algoritmo (las que van a ser reconocidas):**
Una carpeta por persona, donde estarán todas las imágenes de esta.

2. **Convertir a blanco y negro las imágenes del punto anterior, ejecutando el siguiente script:**
python B&W.py rutaImagenes

3. **Generar archivo .csv con la información de las imágenes:**
python create_csv.py > info_caras.txt

4. **Crear arreglos de las imágenes (sólo las caras) y su identificador:**
Con ayuda del archivo generado en el punto anterior.
Se utiliza CascadeClassifier de opencv para detectar los rostros existentes en una imagen; está implementación 
está basado en haar-like features.

5. **Entrenar la red neuronal con las imágenes y etiquetas obtenidas:**
Las que nos retorna el punto anterior.

_________________________________________

### Para ejecutar el programa:

python Reconocedor.py Rutaimagenes
