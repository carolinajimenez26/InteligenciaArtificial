#!/usr/bin/env python

# Para cambiar el color de las imagenes a blanco y negro

import sys
import os.path
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
                print filename
                #Se necesita la ruta completa para abrir la imagen
                dire = os.path.join(subject_path , filename)
                img = Image.open(dire).convert('L')
                img.show()
                img.save(dire)

            label = label + 1
