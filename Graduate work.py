# Thesis of the student group 214 Bandik Vyacheslav
# Topic of work:  The Engraver game
#
# 2. Графическая программа, рисующая непрерывную линию на экране с помощью
# 3. клавиш WASD. Создана под влиянием игры "Волшебный экран"


import pygame

# инициализация Pygame
pygame.init()

WIDTH, HEIGHT = 1000, 800 # 640, 480  Размер экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гравировщик")

# цвета для рисования
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# начальные координаты и скорость
x, y = WIDTH // 2, HEIGHT // 2
speed = 0.1

# основной цикл программы
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение гравировщика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    elif keys[pygame.K_s]:
        y += speed
    elif keys[pygame.K_a]:
        x -= speed
    elif keys[pygame.K_d]:
        x += speed

    # рисование линии
    pygame.draw.line(screen, RED, (x, y), (x + speed, y + speed), 5)

    # обновление экрана
    pygame.display.flip()

# завершение Pygame
pygame.quit()




# После запуска программы можно использовать клавиши WASD
# для перемещения гравировщика и рисования непрерывной красной линии.