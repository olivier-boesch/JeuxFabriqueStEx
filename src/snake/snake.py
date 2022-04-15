# importation biblio
import pygame
import time
import random
 
 
 
 
 
# init image de font
background = pygame.image.load("bg.png")
background2 = pygame.image.load("bg2.jpg")
gameover_image = pygame.image.load("gameover.png")
gameover_image = pygame.transform.scale(gameover_image, (170,170))
bg_easteregg = pygame.image.load("easter_egg.png")
 
# init pour pouvoir utiliser des objet avec des son
pygame.init() 
# tout les prérequis pour les sons qu'on utilisera plus tard
pygame.mixer.set_num_channels(2)
canal_1 = pygame.mixer.Channel(0)
canal_2 = pygame.mixer.Channel(1)
bonbon_sound = pygame.mixer.Sound("bonbon_son.mp3")
gameover_sound = pygame.mixer.Sound("gameover_son.mp3")
theme_sound = pygame.mixer.Sound("theme.mp3")
easteregg_sound = pygame.mixer.Sound("easteregg_son.mp3")
 
 
# point départ
point = 0
 

# vitesse du serpent 
speed_serpent = 10
 
# taille fenetre
fenetre_x = 600
fenetre_y = 600
 
# definiton couleurs
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
cyan = pygame.Color(127,255,212)
 
# Initialisation Pygame
pygame.init()
 
# musique de theme du jeu 
if point == 666:
    theme_sound = easteregg_sound
    canal_2.play(theme_sound)
else:
    canal_2.play(theme_sound)
theme_sound.set_volume(0.1)

 
# Initialisation fenetre jeu
pygame.display.set_caption('TG12 - Le Snake')
fenetre = pygame.display.set_mode((fenetre_x, fenetre_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# pos par defaut du serpent
pos_serpent = [100, 50]
 
# definition 4 premiers blocs du corps du serpent
body_serpent = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# position du fruit
pos_fruit = [random.randrange(1, (fenetre_x//10)) * 10,
                  random.randrange(1, (fenetre_y//10)) * 10]
 
fruit_spawn = True
 
# création direction par défaut du serpent 
# qui est la droite
direction = 'RIGHT'
change_direction = direction
 

 
# afficher fonction point 
def points(choice, color, font, size):
   
    # créer point_font
    point_font = pygame.font.SysFont(font, size)
     
    # créer affichage
    # point_surface
    point_surface = point_font.render('Point(s) : ' + str(point), True, color)
     
    # créer un object rectangulaire pour le texte
    # Surface objet
    point_rect = point_surface.get_rect()
    point_rect.midtop = (48.5,10)
     
    # displaying text
    fenetre.blit(point_surface, point_rect)
def highscore(choice, color, font, size):
   
    # créer point_font
    highscore_font = pygame.font.SysFont(font, size)
     
    # créer affichage
    # point_surface
    highscore_surface = highscore_font.render('Meilleur score : ' + str(meilleur_score), True, color)
     
    # créer un object rectangulaire pour le texte
    # Surface objet
    highscore_rect = highscore_surface.get_rect()
    highscore_rect.midtop = (89.8,30)
     
    # displaying text
    fenetre.blit(highscore_surface, highscore_rect)
 
# fonction game over
def game_over():
   
    # son de gameover
    # musique play sur le canal 2, même canal que le son du game over
    # quand gameover se lance, musique du jeu s'arrete car sur le meme canal
    canal_2.play(gameover_sound)
   
   
   
    font_template = pygame.font.SysFont("Impact",30)
     
    # créer une surface de texte
    game_over_surface = font_template.render('Points : ' , True, red)
    game_over_pts_surface = font_template.render(str(point), True, white)
    best_score_surface = font_template.render('Meilleur score : ', True, red)
    best_score_pts_surface = font_template.render(str(meilleur_score), True, white)
     
    # créer un objet rectangulaire pour le texte
    # surface objet
    game_over_rect = game_over_surface.get_rect()
    best_score_rect = best_score_surface.get_rect()
    game_over_pts_rect = game_over_pts_surface.get_rect()
    best_score_pts_rect = best_score_pts_surface.get_rect()
    
    pygame.draw.rect(fenetre, (107,142,35), pygame.Rect(48, 200, 500, 200), 0)
    pygame.display.flip()
    pygame.draw.rect(fenetre, black, pygame.Rect(48, 200, 500, 200), 4)
    pygame.display.flip()
    
     
     
     
    # parametre pos text
    game_over_rect.midtop = (277,320)
    best_score_rect.midtop = (267,350)
    game_over_pts_rect.midtop = (353,320)
    best_score_pts_rect.midtop = (393,350)
     
    # blit dessinera le texte à l'écran
    fenetre.blit(gameover_image, (215,175))
    fenetre.blit(game_over_surface, game_over_rect)
    fenetre.blit(best_score_surface, best_score_rect)
    fenetre.blit(game_over_pts_surface, game_over_pts_rect)
    fenetre.blit(best_score_pts_surface, best_score_pts_rect)
    pygame.display.flip()
     
    
    # quitter le prog. apres 5sec
    time.sleep(5)
     
    # desactiver la librarie pygame
    pygame.quit()
     
    # quitter le prog
    quit()
 
 
# Fonction principale
while True:
     
    # gestion des événements clés
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'
 
    # Si deux touches sont enfoncées simultanément
    # il ne faut pas que le serpent aille dans 2 direction en meme temps
    # conditions/regles pour dir. simultannées
    if change_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # bouger le serpent
    if direction == 'UP':
        pos_serpent[1] -= 10
    if direction == 'DOWN':
        pos_serpent[1] += 10
    if direction == 'LEFT':
        pos_serpent[0] -= 10
    if direction == 'RIGHT':
        pos_serpent[0] += 10
 
    # Mécanisme de croissance du corps du serpent a chaque fruit mangé
    # si les fruits et les serpents entrent en collision, alors les points
    # seront augmentés de 10
    body_serpent.insert(0, list(pos_serpent))
    if point < 666 or point > 666:
        if pos_serpent[0] == pos_fruit[0] and pos_serpent[1] == pos_fruit[1]:
            point += 10
            canal_1.play(bonbon_sound) #sur canal 1 car sinon coupe la musique de fond
            bonbon_sound.set_volume(0.2) # volume a 0.2 (1 par défaut)
            speed_serpent += 1
            
            fruit_spawn = False
        else:
            body_serpent.pop()
             
        if not fruit_spawn:
            pos_fruit = [random.randrange(1, (fenetre_x//10)) * 10,
                              random.randrange(1, (fenetre_y//10)) * 10]
             
        fruit_spawn = True
    else:
        if pos_serpent[0] == pos_fruit[0] and pos_serpent[1] == pos_fruit[1]:
            canal_1.play(bonbon_sound) #sur canal 1 car sinon coupe la musique de fond
            bonbon_sound.set_volume(0.2) # volume a 0.2 (1 par défaut)
            speed_serpent += 1
            
            fruit_spawn = False
        else:
            body_serpent.pop()
             
        if not fruit_spawn:
            pos_fruit = [random.randrange(1, (fenetre_x//10)) * 10,
                              random.randrange(1, (fenetre_y//10)) * 10]
             
        fruit_spawn = True
        
     
    
 
    # Conditions de game over
    if pos_serpent[0] < 0 or pos_serpent[0] > fenetre_x-10:
        game_over()
    if pos_serpent[1] < 0 or pos_serpent[1] > fenetre_y-10:
        game_over()
 
    # Se toucher soit même
    for block in body_serpent[1:]:
        if pos_serpent[0] == block[0] and pos_serpent[1] == block[1]:
            game_over()
            
    # meilleurs_scores
    
    best_score = open("meilleur_score.txt", "r")
    
    meilleur_score = int(best_score.readline())
    
    if meilleur_score < point:
        meilleur_score = point
        best_score = open("meilleur_score.txt", "w")
        best_score.write(str(point))
    
    
    
 
    # affichage des points et meilleur score
    points(1, white, 'impact', 20)
    highscore(1, white, 'impact', 20)
    
 
    # Refresh fenetre jeu
    pygame.display.update()
    
        
           
    
    
    
    # level 2
    if point >= 200 and point < 666 or point > 666:
        fenetre.blit(background2, (0,0))
        for pos in body_serpent:
            pygame.draw.rect(fenetre, blue, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(fenetre, cyan, pygame.Rect(pos_fruit[0], pos_fruit[1], 10, 10))
        
    elif point < 200:
        fenetre.blit(background, (0, 0)) #level 1
        for pos in body_serpent:
            pygame.draw.rect(fenetre, yellow, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(fenetre, red, pygame.Rect(pos_fruit[0], pos_fruit[1], 10, 10))
    elif point == 666:
        fenetre.blit(bg_easteregg, (0,0))
        speed_serpent = 30
        theme_sound = easteregg_sound
        for pos in body_serpent:
            pygame.draw.rect(fenetre, white, pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(fenetre, red, pygame.Rect(pos_fruit[0], pos_fruit[1], 10, 10))
        
        
 
    # Frame Per Second /Refresh Rate
    fps.tick(speed_serpent)