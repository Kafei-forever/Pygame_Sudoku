import pygame,sys,os,Sudoku_position,beforehand
from pygame import *
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
BLACK=(0,0,0)
lime=(0,255,0)
GREEN=(0,128,0)
Light_blue=(173,216,230)
Aqua=(0,255,255)
WHITE=(255,255,255)
GRAY=(128,128,128)
RED=(255,0,0)
BLUE=(0,0,205)
Width=1000
Height=700
R_Width=R_Height=630
Grid=9
SCREEN=pygame.display.set_mode((Width,Height),0,32)
pygame.display.set_caption("sudoku")
grid_group=[]
grid_group_pos=[]
blocks = pygame.sprite.Group()
clock = pygame.time.Clock()
cancel_list=[]
def text(text,size,color,background):
    a=pygame.font.SysFont("arial",size)
    b=a.render(text,True,color,background)
    return b
def check_text(t,pos_x,pos_y,x,y):
    a=text(t, 30, WHITE,BLACK)
    if x<pos_x<x+a.get_rect()[2] and y<pos_y<y+a.get_rect()[3]:
        a = text(t, 30, WHITE, GREEN)
        SCREEN.blit(a, (x, y))
    else:
        SCREEN.blit(a, (x, y))
class grid():
    def __init__(self,position):
        self.pos=(position[0],position[1])
        self.selected=False
        self.available=True
        self.color1=Light_blue
        self.color2=GRAY
        self.size=R_Height/Grid
        self.rect=[self.pos[0] * R_Width/Grid,self.pos[1]* R_Height/Grid,self.size,self.size ]
        self.number=""
class block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(((R_Height/Grid)/2,(R_Height/Grid)/2))
        self.image.fill(Light_blue)
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=400
        self.number=""
    def update(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        if 0 < pos_x < R_Width and 0 < pos_y < R_Height:
            a=grid_group_pos.index((pos_x//(R_Width/Grid),pos_y//(R_Height/Grid)))
            if grid_group[a][1]==True and grid_group[a][2]==False:
                self.rect.x=pos_x//(R_Width/Grid)*(R_Width/Grid)+20
                self.rect.y=pos_y//(R_Height/Grid)*(R_Height/Grid)+20
                if grid_group[a][3]=="":
                    self.listen()
                    if self.number!="":
                        grid_group[a][3]=self.number
                        cancel_list.clear()
                        cancel_list.append(grid_group[a][0])
                        cancel_list.append(self.number)
                        self.number=""
    def listen(self):
        listen = pygame.key.get_pressed()
        if listen[pygame.K_KP1]:
            self.number = 1
        elif listen[pygame.K_KP2]:
            self.number = 2
        elif listen[pygame.K_KP3]:
            self.number = 3
        elif listen[pygame.K_KP4]:
            self.number = 4
        elif listen[pygame.K_KP5]:
            self.number = 5
        elif listen[pygame.K_KP6]:
            self.number = 6
        elif listen[pygame.K_KP7]:
            self.number = 7
        elif listen[pygame.K_KP8]:
            self.number = 8
        elif listen[pygame.K_KP9]:
            self.number = 9
class process():
    def __init__(self):
        for i in range(len(Sudoku_position.position)):
            a=grid(Sudoku_position.position[i])
            g=[a.pos,a.available,a.selected,a.number]
            b=a.pos
            grid_group_pos.append(b)
            grid_group.append(g)
        b = block()
        blocks.add(b)
        self.a = pygame.Rect(800, 600, 60,30)
        self.b = pygame.Rect(800, 650, 60,30)
        self.c = pygame.Rect(800, 550, 60,30)
        beforehand.ld.load()
    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT or beforehand.ld.available==False:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.a.collidepoint(x, y):
                    for i in range(len(grid_group)):
                        if grid_group[i][1] == True and grid_group[i][2] == False:
                            grid_group[i][3]=""
                if self.b.collidepoint(x, y):
                    check()
                if self.c.collidepoint(x,y):
                    for i in range(len(grid_group)):
                        if grid_group[i][0]==cancel_list[0]:
                            grid_group[i][3]=""
        SCREEN.fill(BLACK)
        for y in range(9):
            y += 1
            if y == 3 or y == 6:
                width = 3
            else:
                width = 1
            pygame.draw.line(SCREEN, WHITE, (0, y * R_Height / 9), (630, y * R_Height / 9), width)
            for x in range(9):
                x += 1
                if x == 3 or x == 6:
                    width = 3
                else:
                    width = 1
                pygame.draw.line(SCREEN, WHITE, (x * R_Width / 9, 0), (x * R_Width / 9, 630), width)
        pos_x, pos_y = pygame.mouse.get_pos()
        check_text("check",pos_x,pos_y,800,650)
        check_text("reset", pos_x, pos_y, 800, 600)
        check_text("cancel",pos_x,pos_y,800,550)
        #print(cancel_list)
def before():
    for i in range(len(beforehand.ld.data)):
        b=beforehand.ld.data[i][2]
        if beforehand.ld.data[i][:-1] in grid_group_pos:
            c=grid_group_pos.index(beforehand.ld.data[i][:-1])
            grid_group[c][1]=False
            grid_group[c][3]=beforehand.ld.data[i][2]
        a=text(str(b),40,lime,BLACK)
        SCREEN.blit(a,(beforehand.ld.data[i][0]*R_Width/Grid+20,beforehand.ld.data[i][1]*R_Height/Grid+20))
    for i in range(len(grid_group)):
        if grid_group[i][1]==True and grid_group[i][2]==False:
            a=text(str(grid_group[i][3]),40,Aqua,BLACK)
            SCREEN.blit(a,(grid_group[i][0][0]*R_Width/Grid+20,grid_group[i][0][1]*R_Height/Grid+20))
class display():
    def __init__(self):
        self.init=""
        self.start="Please enter"
        self.blank="Somewhere is empty"
        self.wrong="Somewhere in wrong"
        self.correct="Yes,you're right"
        self.init = self.start
        self.delay=50
        self.a=0
    def update(self):
        a=text(self.init,30,RED,BLACK)
        SCREEN.blit(a,(700,300))
        if self.init==self.correct:
            self.reload()
        if self.a>self.delay:
            for i in range(len(grid_group)):
                grid_group[i][3]=""
                grid_group[i][1]=True
                self.init=self.start
            beforehand.ld.reload()
            self.a=0
    def reload(self):
        self.a+=1
p=process()
d=display()
def check():
    blocks.empty()
    a=0
    for i in range(len(grid_group)):
       if grid_group[i][3]=="":
           d.init=d.blank
           b = block()
           blocks.add(b)
           break
       else:
           a+=1
    if a==81:
        a1=[];b1=[];c1=[]
        a2=[];b2=[];c2=[]
        a3=[];b3=[];c3=[]
        a4=[];b4=[];c4=[]
        a5=[];b5=[];c5=[]
        a6=[];b6=[];c6=[]
        a7=[];b7=[];c7=[]
        a8=[];b8=[];c8=[]
        a9=[];b9=[];c9=[]
        alla=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
        allb=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        allc=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
        for i in range(len(grid_group)):
            if grid_group[i][0][0]==0:
                a1.append(grid_group[i][3])
            if grid_group[i][0][0]==1:
                a2.append(grid_group[i][3])
            if grid_group[i][0][0]==2:
                a3.append(grid_group[i][3])
            if grid_group[i][0][0]==3:
                a4.append(grid_group[i][3])
            if grid_group[i][0][0]==4:
                a5.append(grid_group[i][3])
            if grid_group[i][0][0]==5:
                a6.append(grid_group[i][3])
            if grid_group[i][0][0]==6:
                a7.append(grid_group[i][3])
            if grid_group[i][0][0]==7:
                a8.append(grid_group[i][3])
            if grid_group[i][0][0]==8:
                a9.append(grid_group[i][3])
            if grid_group[i][0][1]==0:
                b1.append(grid_group[i][3])
            if grid_group[i][0][1]==1:
                b2.append(grid_group[i][3])
            if grid_group[i][0][1]==2:
                b3.append(grid_group[i][3])
            if grid_group[i][0][1]==3:
                b4.append(grid_group[i][3])
            if grid_group[i][0][1]==4:
                b5.append(grid_group[i][3])
            if grid_group[i][0][1]==5:
                b6.append(grid_group[i][3])
            if grid_group[i][0][1]==6:
                b7.append(grid_group[i][3])
            if grid_group[i][0][1]==7:
                b8.append(grid_group[i][3])
            if grid_group[i][0][1]==8:
                b9.append(grid_group[i][3])
            if 0<=grid_group[i][0][0]<=2 and 0<=grid_group[i][0][1]<=2:
                c1.append(grid_group[i][3])
            if 0<=grid_group[i][0][0]<=2 and 2<grid_group[i][0][1]<6:
                c2.append(grid_group[i][3])
            if 0<=grid_group[i][0][0]<=2 and 6<=grid_group[i][0][1]<9:
                c3.append(grid_group[i][3])
            if 2<grid_group[i][0][0]<6 and 0<=grid_group[i][0][1]<=2:
                c4.append(grid_group[i][3])
            if 2 < grid_group[i][0][0] < 6 and 2 < grid_group[i][0][1] < 6:
                c5.append(grid_group[i][3])
            if 2 < grid_group[i][0][0] < 6 and 6 <= grid_group[i][0][1] < 9:
                c6.append(grid_group[i][3])
            if 6 <= grid_group[i][0][0] < 9 and 0 <= grid_group[i][0][1] <= 2:
                c7.append(grid_group[i][3])
            if 6 <= grid_group[i][0][0] < 9 and 2 < grid_group[i][0][1] < 6:
                c8.append(grid_group[i][3])
            if 6 <= grid_group[i][0][0] < 9 and 6 <= grid_group[i][0][1] < 9:
                c9.append(grid_group[i][3])
        #print(alla,allb,allc)
        for i in range(9):
            if alla[i].count(i+1)==1:
                if allb[i].count(i+1)==1:
                    if allc[i].count(i+1)==1:
                        d.init = d.correct
                        b = block()
                        blocks.add(b)
                    else:
                        d.init = d.wrong
                        for x in range(9):
                            alla[x].clear()
                            allb[x].clear()
                            allc[x].clear()
                        for i in range(len(grid_group)):
                            if grid_group[i][1] == True and grid_group[i][2] == False:
                                grid_group[i][3] = ""
                        b = block()
                        blocks.add(b)
                        break
                else:
                    d.init = d.wrong
                    for x in range(9):
                        alla[x].clear()
                        allb[x].clear()
                        allc[x].clear()
                    for i in range(len(grid_group)):
                        if grid_group[i][1] == True and grid_group[i][2] == False:
                            grid_group[i][3] = ""
                    b = block()
                    blocks.add(b)
                    break
            else:
                d.init = d.wrong
                for x in range(9):
                    alla[x].clear()
                    allb[x].clear()
                    allc[x].clear()
                for i in range(len(grid_group)):
                    if grid_group[i][1] == True and grid_group[i][2] == False:
                        grid_group[i][3] = ""
                b = block()
                blocks.add(b)
                break
def main():
    while True:
        p.update()
        d.update()
        blocks.draw(SCREEN)
        blocks.update()
        before()
        pygame.display.flip()
if __name__ == "__main__":
    main()