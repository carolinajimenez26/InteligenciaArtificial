import cv2
import sys
import csv
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #clasificadores Haar para detectar caras

def normalizeImage(image):
	if (image.shape[:2] > (512,512)):
		return cv2.resize(image, (512, 512))#,interpolation = cv2.INTER_CUBIC)

def train(x,l):
	images = []
	labels = []
	minSize = np.inf
	index = 0
	for image_path in x: #imagenes
		index += 1
		img = cv2.imread(image_path)
		#img = normalizeImage(img)
		faces = FindFaces(img)

		if (len(faces) != 0): # si ha detectado caras
			for (x, y, w, h) in faces:
				horizontal_offset = 0.15 * w
				vertical_offset = 0.2 * h
				face = np.array(img[y + vertical_offset: y + h, x + horizontal_offset: x - horizontal_offset + w])
				if (face.size < minSize):
					minSize = face.size
					min_img = face
				images.append(np.array(face).flatten())#solo nos interesa la cara
				labels.append(l[index-1])

	height, width = min_img.shape[:2]

	#deben tener el mismo tamaño para entrenar el algoritmo
	for i in range(0,len(images)):
		if (images[i].shape[:2] != min_img.shape[:2]):
			images[i] = cv2.resize(images[i], (width, height), interpolation = cv2.INTER_CUBIC)

	for image in images:
		cv2.imshow("Entrenados", image)
		cv2.waitKey(50)
		#print ("guat?:", image.size)
	cv2.destroyAllWindows()
	recognizer = cv2.face.createEigenFaceRecognizer()
	recognizer.train(np.array(images),np.array(labels))
	#recognizer.save("recognizer.xml")
	return recognizer, min_img

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
		scaleFactor = 1.1,
		minNeighbors = 10,
		minSize= (100,100),
		flags = cv2.CASCADE_SCALE_IMAGE
	) #saca las coordenadas de los rostros encontrados

	return faces

def ShowFaces(faces, image):
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0),2)

	cv2.imshow("", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def main():
	if len(sys.argv) != 3:
		print ("uso: python3 Reconocedor.py <Imagen> <rutaCSV>")
		sys.exit(1)

	image_dir = sys.argv[1]
	file_name = sys.argv[2]
	image = cv2.imread(image_dir)
	#image = normalizeImage(image)
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # se convierte a escala de grises

	# retorna la informacion del archivo csv en dos arreglos
	x,y = getInfo(file_name)

	recognizer,min_img = train(x,y) #entrena al algoritmo para que reconozca los rostros
	height, width = min_img.shape[:2]

	#busca en la imagen ingresada si hay un rostro conocido
	faces = FindFaces(img_gray) #busca solo las caras
	print ("faces : ", len(faces))
	if (len(faces) != 0): # si encuentra caras
		for (x, y, w, h) in faces:
			face = img_gray[y: y + h, x: x + w]
			if (face.shape[:2] != min_img.shape[:2]):
				face = cv2.resize(face, (width, height), interpolation = cv2.INTER_CUBIC)

			cv2.imshow("uhmm", face)
			cv2.waitKey(0)

			id, conf = recognizer.predict(face)
			print ("id: ", id)
			print ("conf: ", conf)

			if (conf < 10 and id != -1):#si encuentra a alguien con un parecido mayor a 50%
				#pinta el cuadrado en su cara
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0),2)

	#muestra la imagen analizada
	cv2.imshow("Detectados", image)
	cv2.waitKey(0)

if __name__ == "__main__":
    main()
