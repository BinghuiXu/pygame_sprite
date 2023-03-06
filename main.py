import pygame
import random
import sys

'''set class sprite'''
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.gunshot=pygame.mixer.Sound("gunshot.mp3")

    def update(self):
        self.rect.center=pygame.mouse.get_pos()
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair,target_group,True)

'''set class sprite'''
class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load(picture_path)
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
    def update(self):
        self.rect.center=pygame.mouse.get_pos()


'''set parameters'''
screen_width=600
screen_height=400

'''generate target'''
target_group=pygame.sprite.Group()
for target in range(20):
    new_target=Target("target.png",random.randrange(0,screen_width),random.randrange(0,screen_height))
    target_group.add(new_target)

'''initialize game'''
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("exercise_sprite")
background=pygame.image.load("bg_green.png")
pygame.mouse.set_visible(False)

clock=pygame.time.Clock()


'''create game sprite: crosshair'''
crosshair=Crosshair("crosshair_red_large.png")#create single sprite
'''draw target'''
target_group.draw(screen)
'''sprite can only be drawed as a group'''
crosshair_group=pygame.sprite.Group()# create sprite group
crosshair_group.add(crosshair)# add sprite value


'''main loop'''
while True:
    '''detect event'''
    for event in pygame.event.get():  
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    '''movement achieve'''

    '''screen refresh under certain fps'''
    
    
    # screen.blit(background,(0,0))
    screen.fill((0,0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.flip()

    clock.tick(30)
