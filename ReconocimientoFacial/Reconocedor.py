import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #clasificadores Haar para detectar caras

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
	if len(sys.argv) != 2:
		sys.exit(1)

	image_dir = sys.argv[1]
	image = cv2.imread(image_dir)
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # se convierte a escala de grises

	faces = FindFaces(img_gray)
	ShowFaces(faces,image)

if __name__ == "__main__":
    main()
