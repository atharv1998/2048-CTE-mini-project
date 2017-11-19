import pygame
import random
import copy
pygame.init()
RED =   (255,   0,   0)
WHITE = (255, 255, 255)
global screen,key
key=0
temp=0
board=[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
board[random.randint(0,3)][random.randint(0,3)]=2
def random1():
    while(True):
        a=random.randint(0,3)
        b=random.randint(0,3)
        if(board[a][b]==' '):
            board[a][b]=2
            print(a )
            print(b)
            break
random1()
def grid():
    global screen
    for i in range(0,5):
        pygame.draw.line(screen,RED,[0,100*i],[400,100*i],1)
    for j in range(0,5):
        pygame.draw.line(screen,RED,[100*j,0],[100*j,400],1)
    pygame.display.flip()
def nos():
    global screen,board
    pygame.font.init()
    for i in range(0,4):
        for j in range(0,4):
            no=str(board[i][j])
            myfont = pygame.font.SysFont('dejavuserif',37)
            label = myfont.render(no,10, RED)
            print(board)
            screen.blit(label, (5+j*100,20+i*100))
    pygame.display.flip()
def keys():
    global key,temp
    a=pygame.key.get_pressed()
    for i in range(0,len(a)):
        if(a[i]==1):
            if(i==273):
                    if(key!='up'and temp!='up'):
                        key='up'
                        temp='up'
                        print(key)
                    else:
                        key=0
            elif(i==276):
                    if(key!='left'and temp!='left'):
                        key='left'
                        temp='left'
                        print(key)
                    else:
                        key=0

            elif(i==275):
                    if(key!='right'and temp!='right'):
                        key='right'
                        temp='right'
                        print(key)
                    else:
                        key=0
            elif(i==274):
                    if(key!='down'and temp!='down'):
                        key='down'
                        temp='down'
                        print(key)
                    else:
                        key=0

def display():

    global screen
    size = [502, 502]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2048")
    done = False
    screen.fill(WHITE)
    pygame.display.flip()
    grid()
    nos()
    while (done==False):
        logic()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True


def logic():
    global board,key
    if (key=='up'):
        random1()
        screen.fill(WHITE)
        grid()
        nos()
        for k in range(0,4):
            for j in range(0,3):
                for i in range(0,4):
                    if(board[i][j]==' 'and board[i][j+1]!=board[i][j]):
                        board[i][j]=board[i][j+1]
                        board[i][j+1]=' '
                    elif(board[i][j+1]==board[i][j] and board[i][j]!=' '):
                        board[i][j]=2*int(board[i][j+1])
                        board[i][j+1]=' '
    if (key=='down'):
        random1()
        screen.fill(WHITE)
        grid()
        nos()
        for k in range(0,4):
            for j in range(2,-1,-1):
                for i in range(0,4):
                    if(board[i][j]==' 'and board[i][j+1]!=board[i][j]):
                        board[i][j+1]=board[i][j]
                        board[i][j-1]=' '
                    elif(board[i][j-1]==board[i][j]and board[i][j]!=' '):
                        board[i][j]=2*int(board[i][j-1])
                        board[i][j-1]=' '
    if (key=='left'):
        random1()
        screen.fill(WHITE)
        grid()
        nos()
        for k in range(0,4):
            for i in range(0,3):
                for j in range(0,4):
                    if(board[i][j]==' 'and board[i+1][j]!=board[i][j]):
                        board[i][j]=board[i+1][j]
                        board[i+1][j]=' '
                    elif(board[i+1][j]==board[i][j]and board[i][j]!=' '):
                        board[i][j]=2*int(board[i+1][j])
                        board[i+1][j]=' '
    if (key=='right'):
        random1()
        screen.fill(WHITE)
        grid()
        nos()
        for k in range(0,4):
            for i in range(2,-1,-1):
                for j in range(0,4):
                    if(board[i][j]==' 'and board[i+1][j]!=board[i][j]):
                        board[i+1][j]=board[i][j]
                        board[i][j]=' '
                    elif(board[i+1][j]==board[i][j]and board[i][j]!=' '):
                        board[i+1][j]=2*int(board[i][j])
                        board[i][j]=' '
    pygame.display.flip()
    keys()

display()
