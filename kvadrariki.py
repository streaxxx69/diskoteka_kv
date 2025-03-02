import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

# Определение начальных цветов
width = 100
height = 75

# Создание списка для хранения квадратов и их цветов
rects = []
colors = []

# Функция для генерации случайного цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Добавление квадратов и их начальных цветов
for _ in range(5):
    rect = pygame.Rect(0, 0, width, height)
    rects.append(rect)
    colors.append(random_color())  # Начальный цвет для каждого квадрата

# Установка позиций квадратов
rects[0].topleft = (0, 0)  # Верхний левый
rects[1].topright = (screen_width, 0)  # Верхний правый
rects[2].bottomright = (screen_width, screen_height)  # Нижний правый
rects[3].bottomleft = (0, screen_height)  # Нижний левый
rects[4].center = (screen_width // 2, screen_height // 2)  # Центр

# Основной цикл
running = True
while running:
    screen.fill((255, 255, 255))  # Очистка экрана

    # Обновление цвета квадратов
    for i in range(len(colors)):
        colors[i] = random_color()  # Меняем цвет на случайный

    # Отрисовка квадратов
    for rect, color in zip(rects, colors):
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()  # Обновление дисплея

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение работы Pygame
pygame.quit()
