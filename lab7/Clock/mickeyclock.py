import pygame,sys,datetime
from rotate import rot_center

# _image_library = {}
# def get_image(path):
#         global _image_library
#         image = _image_library.get(path)
#         if image == None:
#                 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#                 image = pygame.image.load(canonicalized_path)
#                 _image_library[path] = image
#         return image

pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w,h))
done = False

# images

back = pygame.image.load('C:\\Users\\GTA\\Desktop\\pp2\\lab7\\Clock\\mickeynohands.jpg')
minutes = pygame.image.load('C:\\Users\\GTA\\Desktop\\pp2\\lab7\\Clock\\minutes.png')
seconds = pygame.image.load('C:\\Users\\GTA\\Desktop\\pp2\\lab7\\Clock\\seconds.png')

back = pygame.transform.scale(back,(800,600))
minutes = pygame.transform.scale(minutes,(400,300))
seconds = pygame.transform.scale(seconds,(400,300))

# seconds = pygame.transform.flip(seconds,True,False)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# time   
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    
# angle    
    x = (-6*min)%360
    y = ((-1)*sec * 6)%360
    
# rotation     
    rot_right , x = rot_center(seconds,x,400,300)
    rot_left , y = rot_center(minutes,y,400,300)
    
# set
    screen.blit(back,(0,0))
    screen.blit(rot_right,x)
    screen.blit(rot_left,y)

    pygame.display.update()

    