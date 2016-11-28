import cv2
import sys

imagen_dir = sys.argv[1]

rostroCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #clasificadores Haar para detectar caras
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #detectar ojos

imagen = cv2.imread(imagen_dir)
filtro = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # se convierte a escala de grises
equ = cv2.equalizeHist(filtro) # para que distintas condiciones de iluminacion no afecten
							   #la deteccion del rosto en la imagen.

#cv2.imshow("Escala de grises", equ)

rostros = rostroCascade.detectMultiScale(
	filtro,
	scaleFactor = 1.2,
	minNeighbors = 5,
	minSize= (30,30),
	flags = cv2.CASCADE_SCALE_IMAGE
) #saca las coordenadas de los rostros encontrados

# Dibuja las cosas encontradas
for (x, y, w, h) in rostros:

	#se dibujan los rectangulos de los rostros encontrados
	cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0),2)

	roi_gray = filtro[y:y+h, x:x+w] # saca la cara de la imagen a escala de grises
	roi_color = imagen[y:y+h, x:x+w] # saca la cara de la imagen original
	eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
	print ("eyes : ", eyes)
	for (ex,ey,ew,eh) in eyes:
		#se dibujan los rectangulos de los ojos encontrados
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

cv2.imshow("Detectados", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
