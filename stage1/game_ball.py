#!/bin/bash/env python
# -*- coding:utf-8 -*-
import sys, pygame, random
from pygame.locals import *

def show_content(screen, font, x, y, text, color=(255, 255, 255)):
    # 创建字体，<文本,抗锯齿,颜色>
    content_text = font.render(text, True, color)
    # 加载文本内容
    screen.blit(content_text, (x, y))

def play_game(screen, lives, score, font):
    # 颜色设置(R,B,G)
    red = 220, 50, 50
    blue = 0, 0, 100
    # 游戏状态标志位
    game_over = True
    # 挡板位置初始化
    pos_x = 300
    pos_y = 460
    # 小球位置随机初始化
    ball_x = random.randint(0, 600)
    # 小球下落高度初始化
    ball_y = -50
    # 小球下落速度
    vel_y = 0.3 + score/4
    while True:
        for event in pygame.event.get():  # 获取事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:  # 绑定光标与挡板
                pos_x, _ = event.pos
            elif event.type == MOUSEBUTTONUP:  # 鼠标抬起
                if game_over:
                    game_over = False
                    lives = 3
                    score = 0
        # 获取键盘,绑定左&右方向以及退出按键
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:  # 左上角Esc键
            pygame.quit()
            sys.exit()
        elif keys[K_RIGHT]:  # 右方向键
            pos_x += 1
        elif keys[K_LEFT]:  # 左方向键
            pos_x -= 1
        # 背景颜色
        screen.fill(blue)
        if game_over:
            show_content(screen, font, 150, 200, 'Score: '+str(score))
            show_content(screen, font, 150, 250, 'Click To Re-Play')
        else:  # 判断小球运行轨迹
            ball_y += vel_y
            if ball_y > 500:  # fallen
                ball_x = random.randint(0, 500)  # 小球随机出现
                ball_y = -50
                lives -= 1
                if lives == 0:
                    game_over = True
            elif ball_y > pos_y:
                # 判断球与板接触的区间
                if (ball_y - pos_y) < 40 and (ball_x > pos_x) and ball_x < (pos_x + 120):
                    score += 1
                    ball_x = random.randint(0, 500)
                    ball_y = -50
        # 小球动态变化颜色(动态改变球的颜色)
        pygame.draw.circle(screen, ((score * 3 + 125) % 255, (score * 3 + 100) % 255, (score + 210) % 255),
                           (ball_x, int(ball_y)), 30, 0)
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 600-120:
            pos_x = 480
        # 绘制矩形挡板
        pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)
        # 屏幕文字显示
        show_content(screen, font, 0, 0, 'Lives:' + str(lives))
        show_content(screen, font, 500, 0, 'Score:' + str(score))
        # 更新屏幕内容
        pygame.display.update()

def start_game():
    # 初始化
    pygame.init()
    # 窗口设置
    screen = pygame.display.set_mode((600, 500))
    # 窗口标题
    pygame.display.set_caption('Ball Game')
    # 设置光标可见
    pygame.mouse.set_visible(True)
    # 设置字体
    font1 = pygame.font.Font(None, 24)
    # 初始生命&分数
    lives = 3
    score = 0
    # 加载游戏
    play_game(screen, lives, score, font1)


if __name__ == '__main__':
    start_game()
