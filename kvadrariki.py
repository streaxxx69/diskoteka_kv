import pygame
import pygame
pygame.init()
import random
import sys
from all_colors import colors

# Инициализация Pygame


# Параметры окна
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Changing Rectangles")
screen.fill((255, 255, 255))  # Заполнение фона белым цветом

# Параметры прямоугольников
rect_size = 200
x, y = (WIDTH - rect_size) // 2, (HEIGHT - rect_size) // 2  # Начальные координаты
fps = 60
clock = pygame.time.Clock()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Завершение работы игры

    screen.fill((255, 255, 255))  # Сброс фона

    # Рисование вложенных прямоугольников
    size = rect_size
    for i in range(10):  # Рисуем 10 вложенных прямоугольников
        color = random.choice(colors)  # Случайный цвет
        pygame.draw.rect(screen, color, (x + i * 10, y + i * 10, size, size), 0)  # Вложенные прямоугольники
        size -= 10  # Уменьшение размера

    pygame.display.flip()  # Обновление экрана
    clock.tick(fps)  # Установка кадров в секунду


