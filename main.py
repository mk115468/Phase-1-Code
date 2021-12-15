#MUHAMMAD KHAN AND JUSTIN 
#PHASE 1 CODE PROJECT 
#DECEMBER 15 2021



#UNIT CONVERSION
unit=input("enter unit(km,lbs,f): ")
if unit=="km":
  km=int(input("enter Km value: "))
  Miles=km*.62
  print(Miles,"m")
if unit=="lbs":
  lbs=int(input("enter lbs value: "))
  lbs=lbs/2.205
  print(lbs,"KG")
if unit=="f":
  f=int(input("enter f value: "))
  f=(f-32) * 5/9 
  print(f,"C")


#RANDOM SHAPES
import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.display.set_mode()
scn_width = 640
scn_height = 480
screen = pygame.display.set_mode((scn_width, scn_height))
screen.fill(BLUE)

print(pygame.font.get_fonts())

font=pygame.font.SysFont("freesans",72)
text=font.render("PHASE",True,BLACK)
tw = text.get_width()
th = text.get_height()
screen_width = screen.get_width()
screen_height = screen.get_height()
screen.blit(text, [400, 0])

pygame.draw.circle(screen, WHITE, [50, 50], 50)
pygame.draw.rect(screen, BLACK, (285,220,50,75)) 

pygame.display.flip()


#LED BLINK
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setup(19,GPIO.OUT)
for i in range(10): 
  GPIO.output(19,GPIO.HIGH)
  time.sleep(.5)
  GPIO.output(19,GPIO.LOW)
  time.sleep(.5)
