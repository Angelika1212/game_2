import sys
import pygame
import random
import sqlite3
from change_planet import cheek_the_level_of_water, cheek_temperature, change_on
from db import DATA_BASE, add_sentence
from gui import show_achievement, load_image, Music_for_game, animation, Start_play
from sprites import AnimatedSprite, update_coords


pygame.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()    


def load_planet():
    screen.blit(load_image('space.png'), (0, 0))
    first_Planet(planet_name, auspiciousness, temperature, screen)
                
        
class Function():
    def __init__(self):
        self.image = load_image('температура.png', True)
        self.x_pos, self.y_pos = 50, 150
        self.widget = []
        self.view_of_screen()
        
    def view_of_screen(self):
        for j in range(2):
            self.widget.append([])
            for i in range(5):
                self.widget[j].append('rect')
                self.widget[j][i] = pygame.draw.rect(screen, (255, 255, 255), (self.x_pos, self.y_pos, 120, 100), 3)
                self.y_pos += 105
                if i == 3:
                    self.y_pos += 50
            self.x_pos, self.y_pos = 1200, 150
        self.x_pos, self.y_pos = 390, 645
        self.widget.append([])
        for i in range(4):
            self.widget[2].append('rect')
            self.widget[2][i] = pygame.draw.rect(screen, (255, 255, 255), (self.x_pos, self.y_pos, 140, 80), 3)
            self.x_pos += 150
        pygame.draw.rect(screen, (255, 255, 255), (100, 50, 300, 50), 3)
        pygame.draw.rect(screen, (255, 255, 255), (1020, 50, 300, 50), 3)
        self.draw_images()
        
    def draw_images(self):
        global list_of_mountain, planet_name, magnetic_field, mountain
        screen.blit(self.image, (50, 50))
        screen.blit(load_image('условия.png', True), (1022, 10))
        screen.blit(load_image('тучи.png'), (60, 162))
        screen.blit(load_image('солнце.png'), (70, 259))
        screen.blit(load_image('гроза.png'), (55, 369))
        screen.blit(load_image('ветер.png'), (53, 474))
        screen.blit(load_image('смерч.png'), (1220, 159))
        screen.blit(load_image('землетрясение.jpg'), (1210, 260))
        screen.blit(load_image('цунами.jpg'), (1210, 369))
        screen.blit(load_image('горы.jpg'), (1215, 494))
        screen.blit(load_image('метеорит.jpg'), (70, 629))
        screen.blit(load_image('РНК.jpg'), (1220, 639)) 
        screen.blit(load_image('РНК.png'), (1261, 579))
        if planet_name[:2] not in '6080100':  
            for i in range(len(list_of_mountain)):
                screen.blit(mountain, list_of_mountain[i])
        self.load_text()
        
    def load_text(self):
        screen.blit(load_image('текст1.png'), (394, 652)) 
        screen.blit(load_image('текст2.png'), (554, 652)) 
        screen.blit(load_image('текст3.png'), (694, 652)) 
        screen.blit(load_image('текст4.png'), (850, 652)) 
               
    def coordination(self, row, element):
        global game_event, temperature, mountain, auspiciousness, life 
        global magnetic_field, pos_xy, oxygen, water, flag_of_earthquake, text, \
               flag_of_text, flag_of_meteorite, list_of_mountain, speed_of_wind
        if row == 0:
            if element == 0:
                game_event += 'planet rain'
                temperature -= 10           
                if 120 < temperature < 200:
                    water += 10
                    text = f'{water}% воды на планете'
                    flag_of_text = True 
                elif temperature > 240:
                    water -= 5
                    text = 'Из-за высокой температуры \nвода испаряется.'
                    flag_of_text = True                    
            elif element == 1:
                if temperature != 300:
                    temperature += 10
                    game_event += 'planet sun'
            elif element == 2:
                game_event += 'planet lightning-fast'
                if water > 20 and oxygen >= 20:
                    life += 5
            elif element == 3:
                game_event += 'planet wind'
                speed_of_wind += 2
            elif element == 4:
                flag_of_meteorite = True
        elif row == 1:
            if element == 0:
                game_event += 'planet tornado'
                speed_of_wind += 20
            elif element == 1:
                flag_of_earthquake = True
            elif element == 2:
                if water >= 20:
                    water += 30
                else:
                    text = 'На вашей планете Turquesa\nочень мало воды для\nцунами.'
                    flag_of_text = True      
            elif element == 3:
                if speed_of_wind >= 20:
                    text = 'На вашей планете слишком \nсильный ветер.'
                    flag_of_text = True 
                else:
                    screen.blit(mountain, pos_xy[3])
                    list_of_mountain.append(pos_xy[3])
                    if 450 <= pos_xy[3][0] <= 800:
                        pos_xy[3][0] += 30
                        if 200 <= pos_xy[3][1] < 550:
                            pos_xy[3][1] += 50
            elif element == 4:
                if auspiciousness >= 70:
                    life += 10
                    Plot().evolution()
                else:
                    text = 'На вашей планете недостаточно\nблагоприятные условия'
                    'для \nжизни.'
                    flag_of_text = True 
        elif row == 2:
            if element == 0:
                if temperature > 0:
                    temperature -= 10 
                    first_Planet(planet_name, auspiciousness, temperature, screen)
            elif element == 1:
                if magnetic_field == 'weak':
                    magnetic_field = 'more strong'
                if magnetic_field == 'more strong':
                    magnetic_field = 'strong'
                if magnetic_field == 'strong':
                    magnetic_field = 'the strongest' 
                text = f'Магнитное поле:{magnetic_field}'
                flag_of_text = True                 
            elif element == 2:
                if oxygen != 100:
                    oxygen += 10
            elif element == 3:
                UFO()
            
    def develop_life(self):
        global life, auspiciousness 
        if life > 0 and auspiciousness >= 70:
            life += 5
        elif auspiciousness < 70 and life > 0:
            life -= 10
            
    def cheek_auspiciousness(self):
        global temperature, auspiciousness, life, speed_of_wind 
        global magnetic_field, water, oxygen, flag_of_earthquake, planet_name
        if magnetic_field == 'strong' or  magnetic_field == 'the strongest':
            if 5 <= speed_of_wind < 20 and 120 <= temperature <= 200:
                if 20 <= oxygen <= 80 and water >= 20:
                    auspiciousness += 5  
                    first_Planet(planet_name, auspiciousness, temperature, screen)
        else:
            if auspiciousness > 10:
                if speed_of_wind > 20 or temperature < 120 or temperature > 200 \
                   or oxygen > 80:
                    auspiciousness -= 5
                    first_Planet(planet_name, auspiciousness, temperature, screen)               

                      
def change_pos_of_sprite(name):
    global pos_xy
    x, y = pygame.mouse.get_pos()
    if 'rain' in name:
        x, y = pygame.mouse.get_pos()
        number_of_sprite = 0
    if 'lightning-fast' in name:
        x, y = pygame.mouse.get_pos()
        number_of_sprite = 1
    if 'wind' in name:
        x, y = pygame.mouse.get_pos()
        number_of_sprite = 2
    if 'tornado' in name:
        x, y = pygame.mouse.get_pos()
        number_of_sprite = 4   
    if 420 <= x <= 900:
        if 90 <= y <= 600:
            pos_xy[number_of_sprite][0], pos_xy[number_of_sprite][1] = x, y
    
    
def events(): 
    global game_event, planet_name, rain, lightning, wind, tornado, \
           auspiciousness, temperature
    if 'rain' in game_event:
        first_Planet(planet_name, auspiciousness, temperature, screen)
        rain.update(screen)
        clock.tick(10)
    if 'sun' in game_event:
        first_Planet(planet_name, auspiciousness, temperature, screen)        
    if 'lightning-fast' in game_event:
        first_Planet(planet_name, auspiciousness, temperature, screen)
        lightning.update(screen)
        clock.tick(5)
    if 'wind' in game_event:
        first_Planet(planet_name, auspiciousness, temperature, screen)
        wind.update(screen)
        clock.tick(5)
    if 'tornado' in game_event:
        first_Planet(planet_name, auspiciousness, temperature, screen)
        tornado.update(screen)
        clock.tick(5)    
         
         
def earthquakes(): 
    global flag_of_earthquake, earthquake, planet_name, auspiciousness, temperature
    if flag_of_earthquake:
        first_Planet(planet_name, auspiciousness, temperature, screen)
        earthquake.update(screen)
        clock.tick(5)
        pygame.display.update()
    else:
        pass
    
    
def meteorites():   
    global flag_of_meteorite, meteorite, planet_name, auspiciousness, temperature
    first_Planet(planet_name, auspiciousness, temperature, screen)
    meteorite.update(screen)
    clock.tick(10)
    pygame.display.update()    


def UFO(): 
    global ufos, planet_name, auspiciousness, flag_of_UFO, temperature
    x, y = 180, 150
    for i in range(9):
        y -= 10
        first_Planet(planet_name, auspiciousness, temperature, screen)
        screen.blit(ufos, (x, y))
        clock.tick(5)
        pygame.display.update()         
    while x < 610:
        x += 20
        first_Planet(planet_name, auspiciousness, temperature, screen)
        screen.blit(ufos, (x, y))
        clock.tick(5)
        pygame.display.update() 
    flag_of_UFO = True
        
        
def cheek_UFO(): 
    global flag_of_UFO, ufos, auspiciousness, planet_name, text, flag_of_text, temperature
    if flag_of_UFO:
        if auspiciousness > 20:
            flag_of_UFO = True
            screen.blit(ufos, (620, 60))
            pygame.display.update()
        elif auspiciousness <= 20:
            pos_x, pos_y = 620, 60
            for i in range(2):
                pos_y -= 10
                first_Planet(planet_name, auspiciousness, temperature, screen)
                screen.blit(ufos, (pos_x, pos_y))
                clock.tick(5)
                pygame.display.update()
            for i in range(10):
                pos_y -= 10
                pos_x += 20
                first_Planet(planet_name, auspiciousness, temperature, screen)
                screen.blit(ufos, (pos_x, pos_y))
                clock.tick(5)
                pygame.display.update()  
            flag_of_UFO = False 
            text = 'Инопланетяне покинули\nпланету из-за неблаго-\nприятных условий'
            flag_of_text = True             
        
                         
class Plot():
    def __init__(self):
        self.line = []
        self.rect_for_plot = pygame.draw.rect(screen, pygame.Color('white'), 
                                              (175, 150, 320, 400)) 
        
    def surface_for_plot(self, text, x=176, y=152): 
        if '\n' in text:
            self.line = text.split('\n')
            for i in range(len(self.line)):
                screen.blit(font.render(self.line[i], 3, pygame.Color('black')), (x, y))
                y += 20
        else:
            screen.blit(font.render(text, 3, pygame.Color('black')), (x, y))
        
    def evolution(self):
        global name_of_the_files, step_in_evolution
        self.surface_for_plot(open(f'plot/{name_of_the_files[step_in_evolution]}').read())
        self.load_pictures()
        pygame.time.set_timer(pygame.USEREVENT, 18000)
    
    def load_pictures(self):
        global step_in_evolution, name_of_pictures
        if f'{step_in_evolution + 1}.jpg' in name_of_pictures:
            screen.blit(load_image(f'{step_in_evolution + 1}.jpg'), (205, 380))
            
            
class first_Planet():
    def __init__(self, name, auspiciousness, temperature, screen):
        screen.blit(load_image('space.png'), (0, 0))
        self.planet = load_image(name, True)
        screen.blit(self.planet, (420, 100))
        Function()
        pygame.draw.rect(screen, pygame.Color('green'), (1023, 53, auspiciousness * 3, 44))
        if temperature >= 150: 
            pygame.draw.rect(screen, pygame.Color('red'), (103, 53, temperature - 5, 44))
        elif 0 < temperature < 150:
            pygame.draw.rect(screen, pygame.Color('blue'), (103, 53, temperature - 5, 44))  
        
                
temperature = 250
auspiciousness = 10
life = 0
speed_of_wind = 0
water = 0
oxygen = 0
number_of_call = 0
magnetic_field = 'weak' 
font = pygame.font.Font(None, 30)
planet_name = 'планета1.png'
previous_planet_name = planet_name
flag_of_earthquake = False
flag_of_text = False
flag_of_meteorite = False
flag_of_UFO = False
text = ''
name_of_the_files = open('Сюжет.txt').read().split(',')
name_of_pictures = open('картинки.txt').read().split(',')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
planet = AnimatedSprite(load_image("planet.png"), 12, 4, 650, 250)
list_of_mountain = []
step_in_evolution = 0
id_of_sentence = len(DATA_BASE().cur.execute('''SELECT * FROM Achievements''').fetchall()) + 1
pos_xy = [[650, 250] for i in range(6)]
pos_xy.extend([[420, 100], [350, 95]])
rain = AnimatedSprite(load_image("rain.png", True), 5, 2, *pos_xy[0])
lightning = AnimatedSprite(load_image("молния.png", True), 10, 1, *pos_xy[1])
wind = AnimatedSprite(load_image("ветер_спрайт.png", True), 1, 8, *pos_xy[2])
tornado = AnimatedSprite(load_image("ураган.png", True), 4, 1, *pos_xy[4])
earthquake = AnimatedSprite(load_image("землетрясение.png", True), 6, 2, *pos_xy[6])
meteorite = AnimatedSprite(load_image("метеор.png", True), 4, 3, *pos_xy[7])
ufos = load_image("НЛО.png", True)
mountain = load_image("гора.png", True)
running = True
game_event = 'introduction'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            step_in_evolution += 1 
            if step_in_evolution < len(name_of_the_files):
                Plot().evolution()
            else:
                first_Planet(planet_name, auspiciousness, temperature, screen)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif game_event == 'animation':
                game_event = 'start_game'
            elif event.key == pygame.K_RETURN and 'choice' == game_event:
                game_event = 'planet'
                load_planet()
        elif event.type == pygame.MOUSEBUTTONUP and game_event == 'start_game':
            if Start_play(font, screen).start_game.collidepoint(event.pos):
                game_event = 'choice'
                Start_play(font, screen).choose(screen, game_event)
            elif Start_play(font, screen).achievement.collidepoint(event.pos):
                game_event = 'achievements' 
        elif game_event == 'achievements' and event.type == pygame.MOUSEBUTTONUP:
            if pygame.draw.rect(screen, (255, 255, 255), 
                                (50, 50, 50, 60), 3).collidepoint(event.pos):
                game_event = 'start_game'
        elif event.type == pygame.MOUSEBUTTONUP and 'planet' in game_event:
            for i in range(len(Function().widget)):
                for j in range(len(Function().widget[i])):
                    if Function().widget[i][j].collidepoint(event.pos):
                        Function().coordination(i, j)
            if flag_of_text:
                if Plot().rect_for_plot.collidepoint(event.pos):
                    flag_of_text = False
                    first_Planet(planet_name, auspiciousness, temperature, screen)
        elif event.type == pygame.MOUSEBUTTONDOWN and 'planet' in game_event:
            change_pos_of_sprite(game_event)
            rain, lightning, wind, tornado = update_coords(rain, lightning, wind, tornado, pos_xy)
    if game_event == 'introduction':
        animation(screen, font)
        game_event = 'animation'
    if game_event == 'animation':
        planet.update(screen)
        clock.tick(10) 
    if game_event == 'start_game':
        Start_play(font, screen)  
    if game_event == 'achievements':
        show_achievement(DATA_BASE().result, font, DATA_BASE().cur, DATA_BASE().con, screen)
    if 'planet' in game_event:
        events()
        Function().develop_life()
        Function().cheek_auspiciousness()
        if flag_of_earthquake:
            planet_name = change_on('temporary.png')
            earthquakes()
            number_of_call += 1
            if number_of_call == 11:
                flag_of_earthquake = False
                planet_name = change_on('после_землетрясения.png')
                first_Planet(planet_name, auspiciousness, temperature, screen)
                number_of_call = 0
        if flag_of_meteorite:
            planet_name = change_on('temporary.png')
            meteorites()
            number_of_call += 1
            if number_of_call == 11:
                flag_of_meteorite = False
                planet_name = change_on('после_метеорита.png')
                first_Planet(planet_name, auspiciousness, temperature, screen)
                number_of_call = 0
        if flag_of_UFO:
            cheek_UFO()
        if flag_of_text:
            Plot().surface_for_plot(text)
        water, planet_name = cheek_the_level_of_water(water, planet_name)
        temperature, planet_name, previous_planet_name = cheek_temperature(temperature, planet_name, previous_planet_name)
        add_sentence(temperature, oxygen, speed_of_wind, water, magnetic_field, 
                     id_of_sentence)
    pygame.display.update()    
    pygame.display.flip()
pygame.quit()