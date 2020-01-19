import os
import pygame


def show_achievement(result, font, cur, con, screen):
    x, y = 205, 105 
    screen.blit(load_image('space.png'), (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (200, 100, 1000, 500))        
    pygame.draw.rect(screen, (255, 255, 255), (200, 100, 1000, 500))
    pygame.draw.rect(screen, (0, 0, 0), (200, 100, 1000, 500), 3) 
    pygame.draw.rect(screen, (255, 255, 255), (50, 50, 50, 60), 3)
    screen.blit(load_image('back.png'), (50, 50))    
    for i in range(len(result)):
        for elem in result[i]: 
            screen.blit(font.render(str(elem), 3, pygame.Color('black')), 
                        (x, y))
            x += 20
        x = 205
        y += 20
        
        
def load_image(name, colorkey=None):
    fullname = os.path.join('data1', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

    
def animation(screen, font): 
    Music_for_game('Audio1.mp3')
    pygame.draw.rect(screen, pygame.Color('white'), (298, 234, 780, 120))   
    font = pygame.font.Font(None, 150)
    text = font.render('Create    Planet', 5, pygame.Color('black'))
    text_x, text_y = 304, 244 
    screen.blit(text, (text_x, text_y))
    pygame.display.flip() 
        
        
class Music_for_game():
    def __init__(self, name):
        pygame.mixer.music.load(name)
        pygame.mixer.music.play()  
        
        
class Start_play():
    def __init__(self, font, screen):
        font = pygame.font.Font(None, 100)
        self.image = load_image("earth.png", True)
        self.image_of_game = load_image('логотип.png')
        self.image_of_rocket = load_image("ракета.png", True)
        self.planet_turquesa =  load_image("Turquesa.png")       
        self.image_of_button_start_game = load_image("Кнопка.png")
        self.image_of_button_achievement = load_image("Кнопка1.png")       
        self.view_of_screen(screen)
        
    def view_of_screen(self, screen):
        screen.blit(load_image('space.png'), (0, 0))
        screen.blit(self.image, (450, 120))
        screen.blit(self.image_of_game, (50, 70))
        screen.blit(self.image_of_rocket, (840, 420))
        screen.blit(self.image_of_button_start_game, (1150, 620))
        screen.blit(self.image_of_button_achievement, (50, 620)) 
        self.start_game = pygame.draw.rect(screen, (255, 255, 255), (1150, 620, 162, 91), 3)
        self.achievement = pygame.draw.rect(screen, (255, 255, 255), (50, 620, 200, 91), 3)
        
    def choose(self, screen, game_event):
        if game_event == 'choice':
            screen.fill((0, 0, 0))
            screen.blit(self.planet_turquesa, (50, 30))