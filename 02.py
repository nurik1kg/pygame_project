import pygame

window = pygame.display.set_mode((400,400))
pygame.display.set_caption('Hello, Pygame!')
screen= pygame.Surface((400,400))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
def Intersect (x1,x2,y1,y2):
    if (x1>x2-40) and (x1<x2+40)and (y1>y2-40) and (y1<y2+40):
        return 1
    else:
        return 0
    

hero = Sprite(180,360,'image/hero.gif')
zero = Sprite(0,0,'image/zet.jpg')
strela = Sprite(-50,350,'image/s.png')
strela.push=False
zero.right=True
zero.step = 1

done = True
pygame.key.set_repeat(1,1)
while done:
    """ Оброботка событий """
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    """ События - нажатие клавиш """
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
            if hero.x>10:
                hero.x-=1
        if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x+=1
        if e.key == pygame.K_UP:
            if hero.y>150:
                hero.y-=1
        if e.key == pygame.K_DOWN:
            if hero.y<350:
                hero.y+=1
        """ Запуск стрелы """
        if e.key == pygame.K_SPACE:
            if strela.push == False:
                strela.x=hero.x
                strela.y=hero.y
                strela.push = True
    """ Событие - движение мыш """
    if e.type == pygame.MOUSEMOTION:
        pygame.mouse.set_visible(False) # скрывает курсор
        m = pygame.mouse.get_pos()      # курсордун кординаттарын кайтарат
        if m[0]>10 and m[0]<350:
            hero.x = m[0]
        if m[1]>150 and m[1]<350:
            hero.y = m[1]
    """" событие - нажатие кнопки мыши """
    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            if strela.push == False:
                strela.x = hero.x
                strela.y = hero.y
                strela.push = True
            
    """ Заливка экран """            
    screen.fill((50,50,50))
    #obekt zero bashy
    if zero.right == True:
        zero.x+=zero.step
        if(zero.x > 360):
            zero.right = False

    else:
        zero.x-=zero.step
        if zero.x<0:
            zero.right = True
    """ перемещение стрелы """
    if strela.y <0:
        strela.push = False
        
    if strela.push == False:
        strela.y = 350
        strela.x = -50
    else:
        strela.y-=1
    """ Кагылышуулар """
    if Intersect(strela.x,zero.x,strela.y,zero.y) == True:
        strela.push = False
        zero.step += 0.2
    """ отрисование обектов """
    strela.render()
    zero.render()
    hero.render()
    window.blit(screen, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)
pygame.quit()
