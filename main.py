import pygame
import sys
import random
import math
import time

pygame.init()

screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the Meteors")
bg = pygame.image.load("vutru.jpg")
bg2 = pygame.image.load("bg2.jpg")
bg3 = pygame.image.load("bg3.jpg")
bg4 = pygame.image.load("bg4.webp")
bg5 = pygame.image.load("bg5.jpg")
bg6 = pygame.image.load("bg6.jpg")
bg2 = pygame.transform.scale(bg2, (800, 600))
bg3 = pygame.transform.scale(bg3, (800, 600))
bg4 = pygame.transform.scale(bg4, (800, 600))
bg5 = pygame.transform.scale(bg5, (800, 600))
bg6 = pygame.transform.scale(bg6, (800, 600))
ship = pygame.image.load("rocketship.png")
pygame.display.set_icon(ship)
play = pygame.image.load('play.jpg')
play = pygame.transform.scale(play, (250, 60))
exit = pygame.image.load('exit.jpg')
exit = pygame.transform.scale(exit, (250, 60))
ship1 = pygame.transform.scale(ship, (100, 120))
l1 = pygame.image.load("l1.jpg")
l1 = pygame.transform.scale(l1, (150, 38))
l2 = pygame.image.load("l2.jpg")
l2 = pygame.transform.scale(l2, (150, 38))
l3 = pygame.image.load("l3.jpg")
l3 = pygame.transform.scale(l3, (150, 38))
l4 = pygame.image.load("l4.jpg")
l4 = pygame.transform.scale(l4, (150, 38))
l5 = pygame.image.load("l5.jpg")
l5 = pygame.transform.scale(l5, (150, 38))
l6 = pygame.image.load("l6.jpg")
l6 = pygame.transform.scale(l6, (150, 38))
m1 = pygame.image.load("m.png")
m2 = pygame.image.load("m.png")
m3 = pygame.image.load("m.png")
m4 = pygame.image.load("m.png")
m5 = pygame.image.load("m.png")
m6 = pygame.image.load("m.png")
m7 = pygame.image.load("m.png")
m8 = pygame.image.load("m.png")
m9 = pygame.image.load("m.png")
m10 = pygame.image.load("m.png")
m11 = pygame.image.load("m.png")
m12 = pygame.image.load("m.png")
m13 = pygame.image.load("m.png")
m14 = pygame.image.load("m.png")
m15 = pygame.image.load("m.png")
m16 = pygame.image.load("m.png")
m17 = pygame.image.load("m.png")
m18 = pygame.image.load("m.png")
back = pygame.image.load("back.png")
back = pygame.transform.scale(back, (50, 50))
score_text = pygame.font.SysFont("Arial", 24)
over = pygame.image.load("game.jpg")
over = pygame.transform.scale(over, (800, 600))
con = pygame.image.load("con.jpg")
con = pygame.transform.scale(con, (250, 100))
explosion = pygame.mixer.Sound("explosion.wav")
theme = pygame.mixer.Sound("sound.mp3")
game_over = pygame.mixer.Sound("mario.mp3")
game_theme = pygame.mixer.Sound("candyland.mp3")

x = 370
y = 520

m1_x = random.randint(0, 750)
m1_y = 0

m2_x = random.randint(0, 750)
m2_y = 0

m3_x = random.randint(0, 750)
m3_y = 0

m4_x = random.randint(0, 750)
m4_y = 0

m5_x = random.randint(0, 750)
m5_y = 0

m6_x = random.randint(0, 750)
m6_y = 0

m7_x = random.randint(0, 750)
m7_y = 0

m8_x = random.randint(0, 750)
m8_y = 0

m9_x = random.randint(0, 750)
m9_y = 0

m10_x = random.randint(0, 750)
m10_y = 0

m11_x = random.randint(0, 750)
m11_y = 0

m12_x = random.randint(0, 750)
m12_y = 0

m13_x = random.randint(0, 750)
m13_y = 0

m14_x = random.randint(0, 750)
m14_y = 0

m15_x = random.randint(0, 750)
m15_y = 0

m16_x = random.randint(0, 750)
m16_y = 0

m17_x = random.randint(0, 750)
m17_y = 0

m18_x = random.randint(0, 750)
m18_y = 0

x_change = 0

tt = 0
gameover = False
score = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 0.7
            elif event.key == pygame.K_RIGHT:
                x_change += 0.7
        if event.type == pygame.KEYUP:
            x_change = 0
    x += x_change
    if x < 0 or x > 750:
        x = 370
    if tt == 0:
        theme.play()
        screen.blit(bg, (0, 0))
        screen.blit(play, (100, 200))
        screen.blit(exit, (100, 400))
        screen.blit(ship1, (500, 270))
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        play_rect = pygame.Rect(100, 200, 250, 75)
        exit_rect = pygame.Rect(100, 400, 250, 75)
        if play_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 1
        if exit_rect.collidepoint(mouse_pos):
            if mouse[0]:
                pygame.quit()
                sys.exit()
    elif tt == 1:
        screen.blit(bg, (0, 0))
        screen.blit(ship1, (170, 270))
        screen.blit(l4, (600, 150))
        screen.blit(l5, (600, 270))
        screen.blit(l6, (600, 390))
        screen.blit(l1, (410, 150))
        screen.blit(l2, (410, 270))
        screen.blit(l3, (410, 390))
        mouse_pos = pygame.mouse.get_pos()
        l4_rect = pygame.Rect(600, 150, 150, 38)
        l5_rect = pygame.Rect(600, 270, 150, 38)
        l6_rect = pygame.Rect(600, 390, 150, 38)
        l1_rect = pygame.Rect(410, 150, 150, 38)
        l2_rect = pygame.Rect(410, 270, 150, 38)
        l3_rect = pygame.Rect(410, 390, 150, 38)
        mouse = pygame.mouse.get_pressed()
        if l1_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 2
                gameover = False
        elif l2_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 3
        elif l3_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 4
        elif l4_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 5
        elif l5_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 6
        elif l6_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 7
    elif tt == 2:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m1, (m1_x, m1_y))
            screen.blit(m2, (m2_x, m2_y))
            screen.blit(back, (750,0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m1_y += 0.5
            m2_y += 0.7
            if m1_y > 600:
                m1_y = 0
                m1_x = random.randint(0, 750)
                score += 1
            if m2_y > 600:
                m2_y = 0
                m2_x = random.randint(0, 750)
                score += 1
            score_render = score_text.render("Score: " + str(score), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis1 = math.sqrt((x - m1_x) ** 2 + (y - m1_y) ** 2)
            dis2 = math.sqrt((x - m2_x) ** 2 + (y - m2_y) ** 2)
            if dis1 < 30 or dis2 < 30:
                game_theme.stop()
                gameover = True
                explosion.play()
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m1_x = random.randint(0, 750)
                m2_x = random.randint(0, 750)
                m1_y = 0
                m2_y = 0
                score = 0
    elif tt == 3:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg2, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m3, (m3_x, m3_y))
            screen.blit(m4, (m4_x, m4_y))
            screen.blit(back, (750, 0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m3_y += 0.9
            m4_y += 1.1
            if m3_y > 600:
                m3_y = 0
                m3_x = random.randint(0, 750)
                score2 += 1
            if m4_y > 600:
                m4_y = 0
                m4_x = random.randint(0, 750)
                score2 += 1
            score_render = score_text.render("Score: " + str(score2), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis3 = math.sqrt((x - m3_x) ** 2 + (y - m3_y) ** 2)
            dis4 = math.sqrt((x - m4_x) ** 2 + (y - m4_y) ** 2)
            if dis3 < 30 or dis4 < 30:
                game_theme.stop()
                explosion.play()
                gameover = True
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m3_x = random.randint(0, 750)
                m4_x = random.randint(0, 750)
                m3_y = 0
                m4_y = 0
                score2 = 0
    elif tt == 4:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg3, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m5, (m5_x, m5_y))
            screen.blit(m6, (m6_x, m6_y))
            screen.blit(m7, (m7_x, m7_y))
            screen.blit(m8, (m8_x, m8_y))
            screen.blit(back, (750, 0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m5_y += 1
            m6_y += 1.1
            m7_y += 1.2
            m8_y += 0.9
            if m5_y > 600:
                m5_y = 0
                m5_x = random.randint(0, 750)
                score3 += 1
            if m6_y > 600:
                m6_y = 0
                m6_x = random.randint(0, 750)
                score3 += 1
            if m7_y > 600:
                m7_y = 0
                m7_x = random.randint(0, 750)
                score3 += 1
            if m8_y > 600:
                m8_y = 0
                m8_x = random.randint(0, 750)
                score3 += 1
            score_render = score_text.render("Score: " + str(score3), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis5 = math.sqrt((x - m5_x) ** 2 + (y - m5_y) ** 2)
            dis6 = math.sqrt((x - m6_x) ** 2 + (y - m6_y) ** 2)
            dis7 = math.sqrt((x - m7_x) ** 2 + (y - m7_y) ** 2)
            dis8 = math.sqrt((x - m8_x) ** 2 + (y - m8_y) ** 2)
            if dis5 < 30 or dis6 < 30 or dis7 < 30 or dis8 < 30:
                game_theme.stop()
                explosion.play()
                gameover = True
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m5_x = random.randint(0, 750)
                m6_x = random.randint(0, 750)
                m5_y = 0
                m6_y = 0
                m7_x = random.randint(0, 750)
                m8_x = random.randint(0, 750)
                m7_y = 0
                m8_y = 0
                score3 = 0
    elif tt == 5:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg4, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m5, (m5_x, m5_y))
            screen.blit(m6, (m6_x, m6_y))
            screen.blit(m7, (m7_x, m7_y))
            screen.blit(m8, (m8_x, m8_y))
            screen.blit(back, (750, 0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m5_y += 1
            m6_y += 0.8
            m7_y += 1.2
            m8_y += 1.1
            if m5_y > 600:
                m5_y = 0
                m5_x = random.randint(0, 750)
                score3 += 1
            if m6_y > 600:
                m6_y = 0
                m6_x = random.randint(0, 750)
                score3 += 1
            if m7_y > 600:
                m7_y = 0
                m7_x = random.randint(0, 750)
                score3 += 1
            if m8_y > 600:
                m8_y = 0
                m8_x = random.randint(0, 750)
                score3 += 1
            score_render = score_text.render("Score: " + str(score3), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis5 = math.sqrt((x - m5_x) ** 2 + (y - m5_y) ** 2)
            dis6 = math.sqrt((x - m6_x) ** 2 + (y - m6_y) ** 2)
            dis7 = math.sqrt((x - m7_x) ** 2 + (y - m7_y) ** 2)
            dis8 = math.sqrt((x - m8_x) ** 2 + (y - m8_y) ** 2)
            if dis5 < 30 or dis6 < 30 or dis7 < 30 or dis8 < 30:
                game_theme.stop()
                explosion.play()
                gameover = True
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m5_x = random.randint(0, 750)
                m6_x = random.randint(0, 750)
                m5_y = 0
                m6_y = 0
                m7_x = random.randint(0, 750)
                m8_x = random.randint(0, 750)
                m7_y = 0
                m8_y = 0
                score3 = 0
    elif tt == 6:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg5, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m9, (m9_x, m9_y))
            screen.blit(m10, (m10_x, m10_y))
            screen.blit(m11, (m11_x, m11_y))
            screen.blit(m12, (m12_x, m12_y))
            screen.blit(m13, (m13_x, m13_y))
            screen.blit(back, (750, 0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m9_y += 1.3
            m10_y += 1.35
            m11_y += 1.25
            m12_y += 1.4
            m13_y += 1.2
            if m9_y > 600:
                m9_y = 0
                m9_x = random.randint(0, 750)
                score4 += 1
            if m10_y > 600:
                m10_y = 0
                m10_x = random.randint(0, 750)
                score4 += 1
            if m11_y > 600:
                m11_y = 0
                m11_x = random.randint(0, 750)
                score4 += 1
            if m12_y > 600:
                m12_y = 0
                m12_x = random.randint(0, 750)
                score4 += 1
            if m13_y > 600:
                m13_y = 0
                m13_x = random.randint(0, 750)
                score4 += 1
            score_render = score_text.render("Score: " + str(score4), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis9 = math.sqrt((x - m9_x) ** 2 + (y - m9_y) ** 2)
            dis10 = math.sqrt((x - m10_x) ** 2 + (y - m10_y) ** 2)
            dis11 = math.sqrt((x - m11_x) ** 2 + (y - m11_y) ** 2)
            dis12 = math.sqrt((x - m12_x) ** 2 + (y - m12_y) ** 2)
            dis13 = math.sqrt((x - m13_x) ** 2 + (y - m13_y) ** 2)
            if dis9 < 30 or dis10 < 30 or dis11 < 30 or dis12 < 30 or dis13 < 30:
                game_theme.stop()
                explosion.play()
                gameover = True
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m9_x = random.randint(0, 750)
                m10_x = random.randint(0, 750)
                m9_y = 0
                m10_y = 0
                m11_x = random.randint(0, 750)
                m12_x = random.randint(0, 750)
                m11_y = 0
                m12_y = 0
                m13_x = random.randint(0, 750)
                m13_y = 0
                score4 = 0
    elif tt == 7:
        theme.stop()
        if gameover == False:
            game_theme.play()
            screen.blit(bg6, (0, 0))
            screen.blit(ship, (x, y))
            screen.blit(m14, (m14_x, m14_y))
            screen.blit(m15, (m15_x, m15_y))
            screen.blit(m16, (m16_x, m16_y))
            screen.blit(m17, (m17_x, m17_y))
            screen.blit(m18, (m18_x, m18_y))
            screen.blit(back, (750, 0))
            back_rect = pygame.Rect(750, 0, 50, 50)
            mouse_pos = pygame.mouse.get_pos()
            mouse = pygame.mouse.get_pressed()
            if back_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    tt = 1
            m14_y += 1.4
            m15_y += 1.43
            m16_y += 1.34
            m17_y += 1.41
            m18_y += 1.625
            if m14_y > 600:
                m14_y = 0
                m14_x = random.randint(0, 750)
                score5 += 1
            if m15_y > 600:
                m15_y = 0
                m15_x = random.randint(0, 750)
                score5 += 1
            if m16_y > 600:
                m16_y = 0
                m16_x = random.randint(0, 750)
                score5 += 1
            if m17_y > 600:
                m17_y = 0
                m17_x = random.randint(0, 750)
                score5 += 1
            if m18_y > 600:
                m18_y = 0
                m18_x = random.randint(0, 750)
                score5 += 1
            score_render = score_text.render("Score: " + str(score5), True, (255, 255, 255))
            screen.blit(score_render, (0, 0))
            dis14 = math.sqrt((x - m14_x) ** 2 + (y - m14_y) ** 2)
            dis15 = math.sqrt((x - m15_x) ** 2 + (y - m15_y) ** 2)
            dis16 = math.sqrt((x - m16_x) ** 2 + (y - m16_y) ** 2)
            dis17 = math.sqrt((x - m17_x) ** 2 + (y - m17_y) ** 2)
            dis18 = math.sqrt((x - m18_x) ** 2 + (y - m18_y) ** 2)
            if dis14 < 30 or dis15 < 30 or dis16 < 30 or dis17 < 30 or dis18 < 30:
                game_theme.stop()
                explosion.play()
                gameover = True
                time.sleep(3)
                tt = 8
                x = 370
                y = 520
                m14_x = random.randint(0, 750)
                m15_x = random.randint(0, 750)
                m14_y = 0
                m15_y = 0
                m16_x = random.randint(0, 750)
                m17_x = random.randint(0, 750)
                m16_y = 0
                m17_y = 0
                m18_x = random.randint(0, 750)
                m18_y = 0
                score5 = 0
    elif tt == 8:
        game_over.play()
        gameover = False
        screen.blit(over, (0, 0))
        screen.blit(con, (275, 400))
        con_rect = pygame.Rect(275, 400, 250, 100)
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if con_rect.collidepoint(mouse_pos):
            if mouse[0]:
                tt = 0
    pygame.display.update()