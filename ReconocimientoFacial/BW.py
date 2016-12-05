#!/usr/bin/env python

# Para cambiar el color de las imagenes a blanco y negro

import sys
import os.path
import cv2

if __name__ == "__main__":

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                #Se necesita la ruta completa para abrir la imagen
                image_path = os.path.join(subject_path , filename)

                img = cv2.imread(image_path)
                img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                cv2.imwrite(image_path, img_gray)
            label = label + 1
