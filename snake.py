class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row,col=self.col)



import pygame
import sys
import random
pygame.init()
pygame.display.set_caption("Greedy Snake!")

w = 800
h = 600

ROW = 60
COL = 80
bg_color = (255, 255, 255)
head = Point(row = int(ROW/2), col = int(COL/2))
head_color = (128,0,0)
snakes_color = (200,200,200)
snakes=[
Point(row=head.row, col=head.col+1),
Point(row=head.row, col=head.col+2)
]
#更新食物
def new_food():
    while 1:
        pos = Point(row = random.randint(10,ROW-10), col =random.randint(10,COL-10))
        #pos2 = Point(row = random.randint(0,ROW-1), col =random.randint(0,COL-1))

        is_coll = False

        if head.row ==pos.row and head.col == pos.col:
            #if head.row ==pos2.row and head.col == pos2.col:
            is_coll = True

        for snake in snakes:
            if snake.row == pos.row and snake.col == pos.col:
                #if snake.row == pos1.row and snake.col == pos1.col:
                is_coll = True
                break

        if  not is_coll:
            break
    return pos



food = new_food()

food_color = (0,200,0)
screen = pygame.display.set_mode((w,h))



def rect(Point, color):
    cell_width = w/COL
    cell_height = h/ROW

    left = Point.col * cell_width
    top = Point.row * cell_height

    pygame.draw.rect(screen, color,(left, top, cell_width, cell_height))

    pass

clock = pygame.time.Clock()

direct = 'left'
quit = True
while quit:
    #监听鼠标键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            if event.key == 275:
                if direct == 'up' or direct == 'down':
                    direct ='right'
                #head.col += 0.1
            elif event.key == 276:
                if direct == 'up' or direct == 'down':
                    direct ='left'
                #head.col -= 0.1
            elif event.key == 273:
                if direct == 'left' or direct == 'right':
                    direct ='up'
                #head.row -= 0.1
            elif event.key == 274:
                if direct == 'left' or direct == 'right':
                    direct ='down'
                #head.row += 0.1

    eat = (head.row == food.row and head.col == food.col)

    if eat :
        food = new_food()
        food_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        head_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        bg_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        snakes_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #处理蛇的身体
    #1、把原来的蛇头插入到蛇身体的列表头
    snakes.insert(0,head.copy())
    #2、删掉列表里最后一个
    if not eat:
        snakes.pop()



    if direct =='left':
        head.col -= 1
    elif direct =='right':
        head.col += 1
    elif direct =='up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1

    dead = False

    if head.col<0 or head.row<0 or head.col>= COL or head.row>=ROW:
        dead = True

    for snake in snakes:
        if head.col == snake.col and head.row ==snake.row:
            dead = True
            break

    if dead:
        print("Game over")

        quit = False


    pygame.draw.rect(screen,bg_color,(0,0,w,h))
    rect(head,head_color)
    rect(food,food_color)
    for snake in snakes:
        rect(snake,snakes_color)

    #刷新显示最新屏幕
    pygame.display.flip()

    #设置帧频
    clock.tick(15)
    #每次循环都重新绘制屏幕
    #screen.fill(bg_color)
if __name__ == '__main__':
    main()
