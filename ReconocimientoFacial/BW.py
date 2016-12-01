#!/usr/bin/env python

# Para cambiar el color de las imagenes a blanco y negro

import sys
import os.path
import cv2
from PIL import Image

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "usage: create_csv <base_path>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                #Se necesita la ruta completa para abrir la imagen
                dire = os.path.join(subject_path , filename)

                img = cv2.imread(dire)
                gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                cv2.imwrite(dire, gris)
            label = label + 1
