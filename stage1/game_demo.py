#!/bin/bash/env python
# -*- coding: utf-8
import pygame,random, time
from pygame.locals import *

def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))

def playGame(scr, lives, score):
    font1 = pygame.font.Font(None, 24)
    # 小挡板的坐标和宽高
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40
    # 让小球从一个上面随机的位置出现
    ball_x, ball_y = random.randint(0, 500), -50
    vel_y = 1  # 小球的初始下落速度
    white = 255, 255, 255
    while lives > 0:  # 循环条件改为当有命时才游戏 否则就结束游戏
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEMOTION:  # 监听鼠标动作
                rect_x, _ = event.pos  # 让小挡板始终都和鼠标一起动
        # print("Ball Position:", ball_x, ball_y)
        if ball_y > 500:
            # print("life:", lives)
            ball_x = random.randint(0, 500)
            ball_y = -50
            # 生命值减少1
            lives -= 1
            # print("life:", lives)
        pygame.draw.circle(scr, (250, 25, 255), (ball_x, ball_y), 30, 0)
        # 小球下落位置（速度）
        ball_y += vel_y
        pygame.display.update()
        scr.fill(white)
        # 设置挡板的移动范围
        if rect_x < 0:
            rect_x = 0
        elif rect_x > 600-rect_w:
            rect_x = 600-rect_w
        pygame.draw.rect(scr, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        # 添加 生命 文件显示
        print_text(scr, font1, 0, 0, "Life:" + str(lives))
        # 添加 得分 文字显示
        print_text(scr, font1, 500, 0, "Score:" + str(score))
        # 更新
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("VipJr BALL Game")
    lives = 3
    score = 0
    playGame(screen, lives, score)
    
main()
