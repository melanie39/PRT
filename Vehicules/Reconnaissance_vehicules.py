# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:54:16 2021

@author: melan
"""

import cv2 
import numpy as np


#Fichier pour la détection des voitures
cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

#Chargement de la vidéo
video_src = 'C:/PRT/videos/video2.avi'
cap = cv2.VideoCapture(video_src)


while True:
    #La fonction "read" retourne :
        #- ret : True/False : permet de détecter la fin de la vidéo
        #- img : Image de la vidéo
    ret, img = cap.read()
    
    if ret==False:
        break
    
    #Passage de la vidéo en niveau de gris pour faciliter la détection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors =2 )

    #Dessin des triangles autour des voitures
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
    #Affichage de la vidéo
    cv2.imshow('vidéo', img)  

    #Interruption de la vidéo et fermeture avant sa fin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Permet la fermeture automatique de la vidéo à la fin de son visionnage
cap.release() 
cv2.destroyAllWindows()
   

