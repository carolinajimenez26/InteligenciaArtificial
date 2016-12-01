import cv2
import sys
import csv
import numpy as np
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #clasificadores Haar para detectar caras

def train(x,labels):
	images = []
	minSize = np.inf
	index = 0
	for image_path in x: #imagenes

		index += 1
		image_pil = Image.open(image_path).convert('L')
		img = np.array(image_pil, 'uint8')
		faces = FindFaces(img)

		if (len(faces) == 0): # no faces
			#images.append(np.array([-1]))
			labels.pop(index-1)
		else:
			for (x, y, w, h) in faces:
				face = img[y: y + h, x: x + w]
				if (face.size < minSize):
					minSize = face.size
					min_img = face
				images.append(face)#solo nos interesa la cara

	height, width = min_img.shape[:2]
	#deben tener el mismo tamaño para entrenar el algoritmo
	"""for i in range(0,len(images)):
		if (images[i].any() == -1):
			print ("remove")
			images.remove(i)
			labels.remove(i)
		else:
			if (images[i].shape[:2] != min_img.shape[:2]):
				images[i] = cv2.resize(images[i], (width, height), interpolation = cv2.INTER_CUBIC)
	"""
	print ("images : ", len(images))
	print ("labels : ", len(labels))

	#recognizer = cv2.face.createEigenFaceRecognizer()
	#recognizer.train(images,np.array(labels))

def getInfo(file_name):
	images = []
	labels = []
	f = open(file_name, 'r') # opens the csv file
	try:
		reader = csv.reader(f)
		for row in reader:
			images.append(row[0].split(";")[0])
			labels.append(int(row[0].split(";")[1]))
	finally:
	    f.close()

	return images,labels

def FindFaces(image):

	faces = face_cascade.detectMultiScale(
		image,
		scaleFactor = 1.2,
		minNeighbors = 5,
		minSize= (30,30),
		flags = cv2.CASCADE_SCALE_IMAGE
	) #saca las coordenadas de los rostros encontrados

	return faces

def ShowFaces(faces, image):
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0),2)

	cv2.imshow("Detectados", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	if len(sys.argv) != 3:
		print ("uso: python3 Reconocedor.py <Imagen> <rutaCSV>")
		sys.exit(1)

	image_dir = sys.argv[1]
	file_name = sys.argv[2]
	image = cv2.imread(image_dir)
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # se convierte a escala de grises

	# retorna la informacion del archivo csv en dos arreglos
	x,y = getInfo(file_name)

	train(x,y)

if __name__ == "__main__":
    main()
