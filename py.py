# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; padding-left: 0px; color: rgb(152, 143, 129);" class="token comment"># Обновление</span>

<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; padding-left: 0px; color: rgb(152, 143, 129);" class="token comment"># Рендеринг</span>
screen<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">.</span>fill<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">(</span>BLACK<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">)</span>
<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; padding-left: 0px; color: rgb(152, 143, 129);" class="token comment"># После отрисовки всего, переворачиваем экран</span>
pygame<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">.</span>display<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">.</span>flip<span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">(</span><span style="box-sizing: border-box; font-weight: inherit !important; font-size: inherit; color: rgb(168, 160, 149);" class="token punctuation">)</span>

pygame.quit()