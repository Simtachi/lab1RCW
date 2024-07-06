import cv2
import pygame
pygame.init
pygame.mixer.init()

#create camera instance 
cam = cv2.VideoCapture(0)

# Main loop
while cam.isOpened(): #Check that the camera is On and ready to be used
    ret, frame1 = cam.read() # t_0
    ret, frame2 = cam.read() # t_1
    #Calcul de la difference absolue entre deux captures
    if ret:
        diff = cv2.absdiff(frame1, frame2)
        #Convert the difference into grey-level
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        #Convert the gray image to GaussianBlur (floutage)
        '''Le flou gaussien permet de réduire le bruit et
        les détails dans l'image'''
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        # Seuillage (thresholding)
        '''
        Appliquer le seuillage binaire, tel que tous les pixels d'une valeur sup
        a 20 deviennent blanc (255), et tous les autres deviennent noir (0)
        '''
        _, tresh =cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
        # Dilatation 
        '''
        Augmente la région blance dans L'image, ce qui permet de connecter
        les régions contigues.
        '''
        dilated = cv2.dilate(tresh, None, iterations=3)
        # Find countours
        '''
            Trouver les contours des régions blanches dans l'image
        '''
        contours, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Traitement de chaque contour
        for c in contours:
            if cv2.contourArea(c) < 8000:
                continue
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 0, 255), 3)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('live-camera', frame1)