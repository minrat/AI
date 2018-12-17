import pygame
import random

class Tools:
    def __init__(self):
        pass
    @staticmethod
    def random_color():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    @staticmethod
    def random_radius():
        return random.randint(5, 50)

    #随机位移
    @staticmethod
    def random_shift():
        sx = random.choice([-5, -9, 3, 7, 9, 5])
        sy = random.choice([-5, -9, 3, 7, 9, 5])
        return (sx, sy)

class Ball:
    def __init__(self, x, y, radius, sx, sy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    #行为:
    #移动: 在哪个窗口上移动
    def move(self, screen):
        self.x += self.sx
        self.y += self.sy

        #边界处理
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx

    #吃其他球
    def eat(self, other):
        if self.alive and other.alive and self != other:
            #self 的半径 > other的半径   两者之间的距离 < 两者的半径之和
            #两者之间的距离
            distance = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
            #半径的平方
            pow_radius = (self.radius + other.radius) ** 2
            if distance < pow_radius and self.radius > other.radius:
                #其他的就gameover
                other.alive = False
                #自身求变大
                self.radius += int(0.14 * other.radius)

    # 球一出现 绘制在屏幕上
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,(self.x, self.y), self.radius)


def main():
        #初始化
        pygame.init()
        #绘制窗口大小产生一个窗口对象
        screen = pygame.display.set_mode((800, 600))
        #设置窗口的标题
        pygame.display.set_caption("大球啃小球")
        #声明一个容器
        balls = []
        #设置启动状态
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #点击了叉号
                    running = False
                #处理鼠标的点击事件  左键是1  右键是3
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #以鼠标点击的地方为圆心点
                    #print(event.pos)
                    x , y = event.pos
                    #半径
                    radius = Tools.random_radius()
                    #颜色
                    color = Tools.random_color()
                    #位移
                    sx, sy = Tools.random_shift()
                    #根据这些特征创建一个圆
                    ball = Ball(x, y, radius, sx, sy, color)
                    balls.append(ball)
            #窗口背景
            screen.fill((255, 255, 255))
            # 获取球  将其绘制在屏幕上
            for ball in balls:
                #调用绘制的方法
                if ball.alive:
                    ball.draw(screen)
                else:
                    balls.remove(ball)

            #渲染
            pygame.display.flip()
            #渲染的时间间隔
            pygame.time.delay(50)

            #移动球
            for ball in balls:
                ball.move(screen)
                #检测球之间的碰撞
                for other in balls:
                    ball.eat(other)

if __name__ == "__main__":
    main()
