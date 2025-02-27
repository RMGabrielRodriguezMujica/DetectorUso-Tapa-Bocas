import cv2
import os
import numpy as np

#dataPath = "C:\Users\yulia\OneDrive\Desktop\Repositorios\DetectorUso-Tapa-Bocas\Dataset_faces" #llamamos a la ubicacion de las imagenes de entrenamiento sin y con tapabocas

dataPath = "C:/Users/yulia/OneDrive/Desktop/Repositorios/DetectorUso-Tapa-Bocas/Dataset_faces"  # llamamos a la ubicacion de las imagenes de entrenamiento sin y con tapabocas
dir_list = os.listdir(dataPath)#se listan las carpeta dentro de este paquete 
print("Lista archivos:", dir_list)

labels = []
facesData = []
label = 0

for name_dir in dir_list:
    dir_path =dataPath + "/" + name_dir

    for file_name in os.listdir(dir_path):
        imagen_path = dir_path + "/" + file_name
        print(imagen_path)
        image = cv2.imread(imagen_path, 0)
        #cv2.imshow("Image", image)
        #cv2.waitKey(10)

        facesData.append(image)
        labels.append(label)
    label += 1

print("Etiqueta 0:", np.count_nonzero(np.array(labels) == 0))
print("Etiqueta 1:", np.count_nonzero(np.array(labels) == 1))

#LBPH FaceRecognizer
face_mask = cv2.face.LBPHFaceRecognizer_create()

#Entrenamiento
print("Entrenando...")
face_mask.train(facesData, np.array(labels))

#Almacenar modelo 
face_mask.write("face_mask_model.xml")
print("Modelo Almacenado")




 