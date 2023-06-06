# Secuencia de colores

import pygame, sys, time #cv2
import numpy as np
#import RPi.GPIO as GPIO

pygame.init()

SCREEN = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Menu")

#Variables de captura de camaras
#cap = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(2)

# Azul (Azul)
azulBajo1 = np.array([70,90,110],np.uint8)
azulAlto1 = np.array([130,150,160],np.uint8)
azulBajo2 = np.array([87,102,127],np.uint8)
azulAlto2 = np.array([123,144,150],np.uint8)
# Amarillo (Naranja)
amarilloBajo1 = np.array([110,70,60],np.uint8)
amarilloAlto1 = np.array([190,110,20],np.uint8)
amarilloBajo2 = np.array([128,87,72],np.uint8)
amarilloAlto2 = np.array([172,96,38],np.uint8)
# Rojos (Rosa)
redBajo1 = np.array([90,50,60],np.uint8)
redAlto1 = np.array([250,160,180],np.uint8)
redBajo2 = np.array([120,95,105],np.uint8)
redAlto2 = np.array([191,122,137],np.uint8)

# Font de texto
# font = cv2.FONT_HERSHEY_SIMPLEX

FlagD1 = 0
FlagD2 = 0
cont1 = 100
cont2 = 100

# Setup de botones
button_pushed = 0
button2_pushed = 0
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# def dibujar(mask,color,frame):
#   contornos,hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
#   global colRoj
#   global colBlu
#   global colYell
  
#   for c in contornos:
#     area = cv2.contourArea(c)
#     if area > 3000:
#       M = cv2.moments(c)
#       if (M["m00"]==0): M["m00"]=1
#       x = int(M["m10"]/M["m00"])
#       y = int(M['m01']/M['m00'])
#       nuevoContorno = cv2.convexHull(c)
#       cv2.circle(frame,(x,y),7,(0,255,0),-1)
#       cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
#       cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
      
#       if color == (0,0,255) and x > 0: #pal red dead redemtion 2
#           colRoj = 1
#           #print("Red")
          
#       if color == (0,255,255) and x > 0: #pal yelou melou
#           colYell = 1
#           #print("Yellow")
          
#       if color == (255,0,0) and x > 0: #pal blus clus
#           colBlu = 1
#           #print("Blue")

# def tomarFoto(cam):
#     # Variables de texto
#     cap_correcta = "Foto cam " + str(cam) + " tomada correctamente"
#     cap_incorrecta = "Error al acceder a cam " + str(cam)
#     cap_nom = "fotoR" + str(cam) + ".png"
#     cap_nom2 = "foto" + str(cam) + ".png"
    
#     # Checar cam
#     if cam == 0:
#         # Leer cam 0
#         leido, frame = cap.read()
#     elif cam == 2:
#         # Leer cam 2
#         leido, frame = cap2.read()
#     else:
#         # Cam no recoinocida, salir
#         print("Cam " + str(cam) + " no reconocida")
#         return 0
    
#     if leido == True:
#         # Foto tomada
#         print(cap_correcta)
#         cv2.imwrite(cap_nom2, frame)
#         # Definir variables según el tipo de cámara
#         if frame.shape[1] == 1920:
#             # Escala
#             scale_percent = 20
            
#         if frame.shape[1] == 1280:
#             # Escala
#             scale_percent = 30
            
#         # Analizar color
#         frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#         maskAzul = cv2.inRange(frameHSV,azulBajo1,azulAlto1)  
#         maskAmarillo = cv2.inRange(frameHSV,amarilloBajo1,amarilloAlto1)
#         maskRed = cv2.inRange(frameHSV,redBajo1,redAlto1)
#         #maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
#         #maskRed = cv2.add(maskRed1,maskRed2)
#         #print("Frame HSV: " + str(frameHSV))
#         #print("Mask Blue: " + str(maskAzul))
#         #print("Mask Yellou: " + str(maskAmarillo))
#         #print("Mask Red: " + str(maskRed))
#         # Dibujar
#         dibujar(maskAzul,(255,0,0),frame)
#         dibujar(maskAmarillo,(0,255,255),frame)
#         dibujar(maskRed,(0,0,255),frame)
#         # Escalar
#         width = int(frame.shape[1] * scale_percent / 100)
#         height = int(frame.shape[0] * scale_percent / 100)
#         dim = (width, height)
#         resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
#         # Guardar
#         cv2.imwrite(cap_nom, resized)
#     else:
#         # Foto no tomada
#         print(cap_incorrecta)
#     # Salir
#     return 1

# def actualizarFoto(cam):
#     # Variables de texto
#     cap_nom = "fotoR" + str(cam) + ".png"
    
#     # Elegir lado
#     if cam == 0:
#         # Lado izquierdo
#         lado = 53
#     elif cam == 2:
#         # Lado derecho
#         lado = 553
#     else:
#         # Cam no recoinocida, salir
#         print("Cam " + str(cam) + " no reconocida")
#         return
    
#     # Cargar imagen
#     BG = pygame.image.load(cap_nom)
    
#     # Actualiza background
#     SCREEN.blit(BG, (lado, 300))
#     pygame.display.update()


def menuPrincipal():
    print("Cool")

def cont(num, flagD):
    
    if num > 0:
        time.sleep(1)
        num -= 1
    
    #Jugador 1
    if flagD == 1:
        num -= 10
    
    return num 

def iniciarJuego():
    pygame.display.set_caption("Juego")
    Main = pygame.image.load("Background_juego.png")
    SCREEN.blit(Main, (0, 0))
    pygame.display.update()
    
    while True:
        # Checar boton de jugador 1
        # if GPIO.input(8) == GPIO.HIGH and button_pushed == 0:
        #     # Toma foto
        #     tom1 = tomarFoto(0)
        #     # Actualiza foto
        #     if tom1 == 1:
        #         actualizarFoto(0)
        #     else:
        #         print("No se actualizó")
        #     # Toma foto
        #     tom2 = tomarFoto(2)
        #     # Actualiza foto
        #     if tom2 == 1:
        #         actualizarFoto(2)
        #     else:
        #         print("No se actualizó")
        #     # Boton presionado
        #     button_pushed = 1
        # if GPIO.input(8) == GPIO.LOW:
        #     # Boton ya no presionado
        #     button_pushed = 0
        
        # # Checar boton de jugador 2
        # if GPIO.input(10) == GPIO.HIGH and button2_pushed == 0:
        #      # Toma foto
        #     tomarFoto(0)
        #     # Actualiza foto
        #     actualizarFoto(0)
        #     # Boton presionado
        #     button2_pushed = 1
        # if GPIO.input(10) == GPIO.LOW:
        #     # Boton ya no presionado
        #     button2_pushed = 0
        
        cont1p = cont(cont1, FlagD1)
        cont2p = cont(cont2, FlagD2)
        print("Contador1: " + str(cont1p))
        print("Contador2: " + str(cont2p))


iniciarJuego()

# cap.release()
# cap2.release()