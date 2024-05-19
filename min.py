
import pygame,random


ancho= 800
largo=600

FPS=60
reloj=pygame.time.Clock()


pantalla= pygame.display.set_mode((ancho,largo))
pygame.display.set_caption("Salida")


fondo= pygame.image.load("fondo.jfif")
fondo= pygame.transform.scale(fondo,(ancho,largo))

si= pygame.image.load("si.png")
si_rect= si.get_rect()
si_rect.center=((ancho/2)-140,(largo/2)+64)

no= pygame.image.load("no.png")
no_rect= no.get_rect()
no_rect.center=((ancho/2)+140,(largo/2)+64)

pregunta= pygame.image.load("salirloke.png")
pregunta= pygame.transform.scale(pregunta,(400,200))
pregunta_rect= pregunta.get_rect()

cursor= pygame.image.load("cursor.png")
cursor_rect= cursor.get_rect()
cursor_rect.center=(cursor_rect.x,cursor_rect.y)

puntos=0
running= True

while running:

    left, middle, right = pygame.mouse.get_pressed()
 
    
    


    if cursor_rect.colliderect(si_rect) and left :

        pausa = True

        while pausa:

            fondo_2= pygame.image.load("lokear.jpg")
            fondo_2= pygame.transform.scale(fondo_2,(ancho,largo))
            pantalla.blit(fondo_2,(0,0))
            pygame.display.update()

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    pausa=False
                    running = False
        

    if cursor_rect.colliderect(no_rect) and left :
        no_rect.x=random.randint(0,600)
        no_rect.y=random.randint(0,500)
        pygame.display.update()
        

    

    for event in pygame.event.get():

        

        if event.type == pygame.MOUSEMOTION:

            mouse_pos = pygame.mouse.get_pos()
            
            cursor_rect.x = mouse_pos[0]
            cursor_rect.y = mouse_pos[1]


        if event.type == pygame.QUIT:

            running = False


    pantalla.blit(fondo,(0,0))
    pantalla.blit(si,si_rect)
    pantalla.blit(pregunta,((ancho/2)-200,(largo/2)-200))
    pantalla.blit(no,no_rect)
    pantalla.blit(cursor,cursor_rect)


    pygame.display.update()
    reloj.tick(FPS)



