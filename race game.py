import pygame
import time 
import random

pygame.init()

display_wi = 834
display_he = 656
car_wi = 49

black = (0,0,0)
green = (0,200,0)
red = (255,0,0)
yellow = (255,255,0)
bright_green = (0,255,0)
grey = (128, 128, 128)
bright_grey = (192,192,192)


gameDisplay = pygame.display.set_mode((display_wi, display_he))
pygame.display.set_caption('My lovely racy game')
clock = pygame.time.Clock()

path = []
for i in range(1,28):
     if i>=10:
          a = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\' + str(i) + '.PNG')
     else:
          a = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\0' + str(i) + '.PNG')
     path.append(a)

line1 = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\line1.PNG')
line2 = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\line2.PNG')
mainCar = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\racing_car.PNG')
orangeCar = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\orange car.PNG')
blueCar = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\blue car.PNG')
yellowCar = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\yellow car.PNG')
greenCar = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\green car.PNG')
coin = pygame.image.load('E:\\LEARN\\Programming & Projects\\Python\\racing game\\cars\\coin.PNG')

cars = [blueCar, orangeCar, greenCar, yellowCar]
line = [line1, line2]

def cars_avoided(count):
     font = pygame.font.SysFont(None, 30)
     text = font.render("You avoided: "+str(count)+" cars", True, black)
     gameDisplay.blit(text,(0,0))

def cars_hit(count):
     font = pygame.font.SysFont(None, 30)
     text = font.render("You've hit: "+str(count)+" orange car", True, black)
     gameDisplay.blit(text,(0,30))

def coins_life(x, count, new_line):
     font = pygame.font.SysFont(None, 30)
     text = font.render("Remained Coins "+str(count)+" : ", True, black)
     gameDisplay.blit(text,(0,70))
     x = 0
     for i in range(count):
          if i%4 == 0:
               x = 0
               new_line += 30
               
          gameDisplay.blit(coin, (x+80, 75 + new_line))
          x += 27
     
          
          
def things(thingx, thingy, thingw, thingh, color):
     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def maincar(x, y):
     gameDisplay.blit(mainCar, (x, y))

def otherCars(x, y, car):
     gameDisplay.blit(car, (x, y))    

def text_objects(text, font):
     textSurface = font.render(text, True, (255,0,0))
     return textSurface, textSurface.get_rect()

def message_display(text):
     fontText = pygame.font.Font('freesansbold.ttf', 50)
     textSurf, textRect = text_objects(text, fontText)
     textRect.center = ((display_wi/2), (display_he/2))

    
     gameDisplay.blit(textSurf, textRect)
     pygame.display.update()
     time.sleep(1)


def crash(display_text):
     message_display(display_text)


def button(msg,x,y,w,h,ic, ac,action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     
     if x+w > mouse[0] > x and y+h > mouse[1] > y:
          pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
          if click[0] == 1 and action != None:
               action()        
     else:
          pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
 
     smallText = pygame.font.Font("freesansbold.ttf",20)
     textSurf, textRect = text_objects(msg, smallText)
     textRect.center = ( (x+(w/2)), (y+(h/2)) )
     gameDisplay.blit(textSurf, textRect)

def changeLine(i):
     gameDisplay.blit(line[i], (834/2 - 14, 0))

def changePath(i):
     gameDisplay.blit(path[i], (0, 0))
     

def quitgame():
     pygame.quit()
     quit()
     
def game_intro():
     
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    game_confirmation()
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                         game_confirmation() 
                    if event.key == pygame.K_SPACE:
                         game_loop()
                         
          gameDisplay.fill((255,255,255))
  
          largeText = pygame.font.Font('freesansbold.ttf',60)
          welcome = pygame.font.Font('freesansbold.ttf',50)
          designer = pygame.font.Font('freesansbold.ttf',20)
  
          TextSurf, TextRect = text_objects("A Simple Racing Game", largeText)
          TextSurf1, TextRect1 = text_objects("-- Welcome --", welcome)
          TextSurf2, TextRect2 = text_objects("Designed by : BISMA", designer)
          
          TextRect.center = ((display_wi/2),(display_he/2 - 100))
          TextRect1.center = ((display_wi/2),(display_he/2))
          TextRect2.center = ((display_wi/2),(display_he - 100))
  
          gameDisplay.blit(TextSurf, TextRect)
          gameDisplay.blit(TextSurf1, TextRect1)
          gameDisplay.blit(TextSurf2, TextRect2)
          
  
          button("GO!",290,390,100,50,green,bright_green,game_loop)
          button("Quit",450,390,100,50,grey,bright_grey,quitgame)
          
          
          pygame.display.update()

def game_confirmation():
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    quitgame()
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                         quitgame()               
  
          gameDisplay.fill((255,255,255))
  
          largeText = pygame.font.Font('freesansbold.ttf',60)
  
          TextSurf, TextRect = text_objects("Are you sure? Come on !!", largeText)
          
          TextRect.center = ((display_wi/2),(display_he/2 - 100))
  
          gameDisplay.blit(TextSurf, TextRect)       
  
          button("Yes!",290,350,100,50,green,bright_green,game_close)
          button("No",450,350,100,50,grey,bright_grey,game_loop)
          
          
          pygame.display.update()

def game_over():
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    quitgame()
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                         quitgame()       
          
          gameDisplay.fill((255,255,255))
     
          largeText = pygame.font.Font('freesansbold.ttf',50)
                      
          TextSurf, TextRect = text_objects("Game Over !! wanna play again??", largeText)
          
          TextRect.center = ((display_wi/2),(display_he/2 - 100))
                    
          gameDisplay.blit(TextSurf, TextRect)       
                    
          button("Yes!",290,350,100,50,green,bright_green,game_loop)
          button("No",450,350,100,50,grey,bright_grey,game_close)
          pygame.display.update()
          

def game_close():
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                         pygame.quit()
                         quit()                
  
          gameDisplay.fill((255,255,255))
  
          largeText = pygame.font.Font('freesansbold.ttf',60)
  
          TextSurf, TextRect = text_objects("Thanks for being patient", largeText)        
          TextRect.center = ((display_wi/2),(display_he/2 - 100))
  
          TextSurf1, TextRect1 = text_objects("with this game !!", largeText)                    
          TextRect1.center = ((display_wi/2),(display_he/2-20))
          
          TextSurf2, TextRect2 = text_objects("good bye !!", largeText)                    
          TextRect2.center = ((display_wi/2),(display_he/2 + 60))            

          gameDisplay.blit(TextSurf, TextRect)
          pygame.display.update()
          
          time.sleep(1)
          gameDisplay.blit(TextSurf1, TextRect1)                  
          pygame.display.update()
          
          time.sleep(1)
          gameDisplay.blit(TextSurf2, TextRect2)             
          pygame.display.update()
          
          time.sleep(2)
          pygame.quit()
          quit()           


def game_loop():
     count1 = 0
     count2 = 0    
     
     new_line = 0
     
     #s=0
     #m=0
     
     x = display_wi / 2 - 25
     y = display_he - 100
     
     x_change = 0
     y_change = 0
     
     thing_startx = random.randrange(311, 445)
     thing_starty = -200
     thing_startx1 = random.randrange(311, 445)
     thing_starty1 = -200
     thing_speed = 5
     thing_width = 30
     thing_height = 30
     car = random.choice(cars)
     car1 = random.choice(cars)
     
     x_coin = 0
     count_coin = 4
          
     i = 0
     j = 0
     while 1:
         
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    game_confirmation()
                    
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                         game_confirmation()
                         
                    if event.key == pygame.K_LEFT:
                         x_change = -5
                    elif event.key == pygame.K_RIGHT:
                         x_change = 5
                    
                    elif event.key == pygame.K_UP:
                         y_change = -5
                    elif event.key == pygame.K_DOWN:
                         y_change = 5
                    
               if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                         x_change = 0
                    
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                         y_change = 0
                           
          x += x_change
          y += y_change
          
          if j == 27:
               j = 0
               changePath(j)
          else:
               changePath(j)
          j += 1            
          
          if i >= 2:
               i = 0
               changeLine(i)
          else:
               changeLine(i)
          i += 1    
          
          #things(thing_startx, thing_starty, thing_width, thing_height, color)
          #thing_starty += thing_speed        
      
          maincar(x, y)
          otherCars(thing_startx, thing_starty, car)
          otherCars(thing_startx1, thing_starty1, car1)
          thing_starty += thing_speed
          cars_avoided(count1)
          cars_hit(count2)
          coins_life(x_coin, count_coin, new_line)
          #counter(s,m)
          
          if x < 311 or x > 495 - car_wi:
               if count_coin <= 1:
                    time.sleep(0.5)
                    game_over()                   
               else:
                    crash('You Lost one coin !!')
               count_coin -= 1
               x = 834/2 - 35
               y = 530                              
              
          
          if thing_starty > display_he:
               thing_starty = 0
               thing_startx = random.randrange(311, 445)            
               car = random.choice(cars)                            
               thing_startx1 = random.randrange(311, 445)
               thing_starty1 = -200
               car1 = random.choice(cars)                            
               count1 += 1
               #thing_speed += 1
          
          if y < thing_starty+thing_height and car == orangeCar:            
               if x > thing_startx and x < thing_startx + thing_width or x+car_wi > thing_startx and x + car_wi < thing_startx+thing_width or \
                                       thing_startx > x and thing_startx+thing_width < x+car_wi:
                    count2 += 1                
                    count_coin += -1
                    if count_coin < 0:
                         crash('You have no coins...Game over')
                         time.sleep(2)
                         game_intro()                   
                    else:
                         crash('You lost one coin !!')
               
               otherCars(thing_startx, thing_starty, car)
               car = random.choice(cars)                            
               thing_starty = -200
               thing_startx = random.randrange(311, 445)               
               
               car1 = random.choice(cars)                            
               thing_startx1 = random.randrange(311, 445)
               thing_starty1 = -200
               x = 834/2 - 35
               y = 530                              

          pygame.display.update()


game_intro()
game_loop()

pygame.quit()
quit()