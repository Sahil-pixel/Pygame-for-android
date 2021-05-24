
# import pygame module in this program
import pygame
from os import environ
from sys import platform as _sys_platform




def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif _sys_platform in ('linux', 'linux2','linux3'):
        return "linux"
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'


pygame.init()


white = (255, 255, 255)

X =720 
Y = 1080

display_surface = pygame.display.set_mode((X, Y ),pygame.FULLSCREEN)

# set the pygame window name
pygame.display.set_caption('Pygame To Apk')

if platform()=="android":
    path="/data/data/org.test.pgame/files/app/"
elif platform()=="linux":
    path="./"

image = pygame.image.load(path+"image.png")

# infinite loop
while True :

    
    display_surface.fill(white)

    
    display_surface.blit(image, (0, 0))

    
    for event in pygame.event.get() :

        
        if event.type == pygame.QUIT :

            
            pygame.quit()

           
            quit()

       
        pygame.display.update()
            
