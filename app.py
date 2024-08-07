import cv2
import pygame
pygame.init()
pygame.mixer.init()

# Create camera instance
cam=cv2.VideoCapture(0)

# Main loop 

while cam.isOpened(): # Check that the camera is On and ready to be used
    ret,frame1=cam.read() # t0
    reet,frame2=cam.read() # t1
    
    # Calcul de la difference entre les deux captures
    if ret:
        diff=cv2.absdiff(frame1,frame2)
        # Convert the difference into gray-level
        gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        # Blur the image \\ flouter image
        blur=cv2.GaussianBlur(gray,(5,5),0)
        #cv2.imshow('Blur',blur)
        # Appliquer le seuillage pour rendre tous les pixels superieur a 20 soit en255(blancs) et le reste 0(noirs)
        _, thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        # Dilation 
        dilated=cv2.dilate(thresh,None,iterations=3)
        # Find contours
        
        contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        # Traitement de chaque contour
        for c in contours:
            if cv2.contourArea(c)<8000:
                continue
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),3)
            sound=pygame.mixer.Sound('alert.wav')
            sound.play()
    if cv2.waitKey(10)==ord("q"):
        break
    cv2.imshow('Live-camera',frame1)
            
        
        