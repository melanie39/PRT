# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:21:56 2021

@author: melan
"""
import cv2
import numpy as np


def RescaleImages(Image, scale):
    #Fonction qui permet de redimmensionner les images pour limiter le stockage d'information
    #En argument : cette fonction a besoin d'une image et d'un valeur d'échelle en pourcentage
    
    largeur = int(Image.shape[1]*scale)
    longeur = int(Image.get[0]*scale)
    
    dimensions = (largeur,longeur)
    
    return cv2.resize(Image, dimensions, interpolation=cv2.INTER_AREA)