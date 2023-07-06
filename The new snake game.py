# pyinstaller --onefile -w Thenewsnakesgame.py

import pygame
import random
import sys

flag = 1

# initializing pygame + displaying window
def initialize():
    global gamewindow, screen_height, screen_width
    screen_width = 900
    screen_height = 600
    pygame.init()
    pygame.mixer.init()
    gamewindow = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snakes with Sancho')
    pygame.display.update()


def text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])
    # Game Variables


def snake_plot(gamewindow, color, sn_list, snake_size):
    for x,y in sn_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


# clock variable

clock = pygame.time.Clock()

# creating loop
def gameloop():
    global flag
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    snake_x = 100
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    in_vel = 4.5
    snake_size = 15
    fps = 60
    food_x = random.randint(30, screen_width/2)
    food_y = random.randint(30, screen_height/2)
    food_size = 15
    score = 0
    end_game = False
    game_over = False
    snake_length = 1
    sn_list = []
    f = open('Highscore.txt', 'r')
    high = f.read()
    high = int(high)
    f.close()
    counter = 0
    stationary = 1
    timer_value = 400
    time_out = 0
    pygame.mixer.music.load('gamestart.mp3')
    pygame.mixer.music.play()
    while time_out <200:
        bg = pygame.image.load('wallpaper.jpg')
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
        gamewindow.fill(white)
        gamewindow.blit(bg, (0,0))
        pygame.display.update()
        time_out+=1

    while not end_game:
        if game_over:
            if flag:
                flag = 0
                pygame.mixer.music.load('game_end.mp3')
                pygame.mixer.music.play()
            if score>high:
                high = score
                f = open('Highscore.txt', 'w')
                f.write(f'{high}')
                f.close()
            gamewindow.fill(black)
            text_screen('CLICK ENTER TO PLAY AGAIN', red, 170, 320)
            text_screen('FINAL SCORE : '+str(score), red, 300, 270)
            text_screen('HIGH SCORE : '+str(high), red, 300, 220)
            text_screen('GAME OVER' ,red, 350, 170)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flag = 1
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True
                if event.type == pygame.KEYDOWN:
                    stationary = 0
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +in_vel
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -in_vel
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -in_vel
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = +in_vel
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10
                food_x = random.randint(20, screen_width-20)
                food_y = random.randint(20, screen_height-20)
                pygame.mixer.music.load('game-start.mp3')
                pygame.mixer.music.play()
            if score>100 and score<=200:
                timer_value = 330
            if score>200 and score<=300:
                timer_value = 260
            if score>300 and score<=400:
                timer_value = 230
                in_vel = 5
            if score>400 and score<=500:
                timer_value = 200
                in_vel = 5.5
            if score>500 and score<=600:
                in_vel = 6.0
            if score>600 and score<=700:
                in_vel = 6.5
            if score>700 and score<=800:
                in_vel = 7
            if score>800 and score<=900:
                in_vel = 7.5
            if score>900:
                in_vel = 8
            
            if counter==timer_value and not stationary:
                counter = 0
                snake_length+=5
                print(f'{timer_value}, {in_vel}')
            counter+=1
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if snake_x>screen_width or snake_y>screen_height or snake_x<0 or snake_y<0:
                game_over = 1
            gamewindow.fill(black)
            text_screen("YOUR SCORE : "+str(score), blue, 20, 20)
            text_screen("HIGH SCORE : "+str(high), blue, 450, 20)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            sn_list.append(head)
            if len(sn_list)>snake_length:
                del sn_list[0]
            if head in sn_list[:-1]:
                game_over = 1
            snake_plot(gamewindow, white, sn_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__=='__main__':
    initialize()
    gameloop()