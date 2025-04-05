import pygame
import os

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Музыкальный проигрыватель")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 120, 255)

# Путь к папке с музыкой
MUSIC_FOLDER = "D:\PP2\lab7\music"  # Используем относительный путь

# Проверка существования папки
if not os.path.exists(MUSIC_FOLDER):
    print(f"Ошибка: Папка '{MUSIC_FOLDER}' не найдена!")
    pygame.quit()
    exit()

# Получение списка MP3-файлов
sounds = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) 
          if f.endswith(".mp3")]

if not sounds:
    print(f"Ошибка: В папке '{MUSIC_FOLDER}' нет MP3-файлов!")
    pygame.quit()
    exit()

# Текущий трек и состояние
current_track = 0
is_playing = False
is_paused = False

# Настройка шрифтов
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 24)

def draw_button(text, x, y, width, height, color=GRAY, text_color=BLACK):
    """Рисует кнопку с текстом и возвращает ее прямоугольник"""
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, border_radius=5)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    return rect

def play_music():
    """Загружает и воспроизводит текущий трек"""
    global is_playing, is_paused
    pygame.mixer.music.load(sounds[current_track])
    pygame.mixer.music.play()
    is_playing = True
    is_paused = False

def toggle_pause():
    """Переключает состояние паузы"""
    global is_paused
    if is_playing:
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
        else:
            pygame.mixer.music.pause()
            is_paused = True

def next_track():
    """Переключает на следующий трек"""
    global current_track
    current_track = (current_track + 1) % len(sounds)
    if is_playing or is_paused:
        play_music()

def prev_track():
    """Переключает на предыдущий трек"""
    global current_track
    current_track = (current_track - 1) % len(sounds)
    if is_playing or is_paused:
        play_music()

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # Отображение текущего трека
    track_name = os.path.basename(sounds[current_track])
    if len(track_name) > 20:
        track_name = track_name[:17] + "..."
    
    title_text = title_font.render("Сейчас играет:", True, WHITE)
    track_text = font.render(track_name, True, BLUE)
    
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))
    screen.blit(track_text, (WIDTH//2 - track_text.get_width()//2, 150))
    
    # Создание кнопок
    play_btn = draw_button("Play", 50, 400, 100, 50)
    pause_btn = draw_button("Pause", 200, 400, 100, 50)
    next_btn = draw_button("Next", 350, 400, 100, 50)
    prev_btn = draw_button("Previous", 50, 300, 150, 50)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(event.pos):
                play_music()
            elif pause_btn.collidepoint(event.pos):
                toggle_pause()
            elif next_btn.collidepoint(event.pos):
                next_track()
            elif prev_btn.collidepoint(event.pos):
                prev_track()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()