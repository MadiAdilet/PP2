import pygame
import sys
import random

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# Загрузка изображений
street = pygame.image.load("D:\\PP2\\lab8\\Racer\\AnimatedStreet.png")
car = pygame.image.load("D:\\PP2\\lab8\\Racer\\Player.png")
car = pygame.transform.scale(car, (50, 70))
traffic = pygame.image.load("D:\\PP2\\lab8\\Racer\\Enemy.png")
traffic = pygame.transform.scale(traffic, (50, 70))
coin_img = pygame.image.load("D:\\PP2\\lab8\\Racer\\coin.jpg")
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Позиции машин
player_x = WIDTH // 2 - 25
player_y = 500
enemy_x = random.randint(50, WIDTH - 110)
enemy_y = -100

# Настройки монет
coins = []
coin_speed = 3
coin_spawn_timer = 0
coin_spawn_interval = 60

# Настройки скорости
base_speed = 5.0
speed = base_speed
speed_increase_per_coin = 0.2  

# Счет
score = 0
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 50)

# Состояние игры
game_active = True

def reset_enemy():
    """Сбрасывает вражескую машину"""
    global enemy_x, enemy_y
    enemy_x = random.randint(50, WIDTH - 110)
    enemy_y = -100

def spawn_coin():
    """Создает новую монету"""
    coin_x = random.randint(30, WIDTH - 60)
    coin_y = -30
    coins.append(pygame.Rect(coin_x, coin_y, 30, 30))

def check_collision():
    """Проверяет столкновение машин"""
    player_rect = pygame.Rect(player_x, player_y, 50, 70)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 70)
    return player_rect.colliderect(enemy_rect)

def check_coin_collision():
    """Проверяет сбор монет и обновляет счет и скорость"""
    global score, speed
    player_rect = pygame.Rect(player_x, player_y, 50, 70)
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1
            speed += speed_increase_per_coin  

def show_game_over():
    """Показывает экран завершения игры"""
    text = big_font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 50))
    score_text = big_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - 80, HEIGHT//2 + 10))
    speed_text = big_font.render(f"Max Speed: {speed:.1f}", True, YELLOW)
    screen.blit(speed_text, (WIDTH//2 - 100, HEIGHT//2 + 70))

def show_hud():
    """Отображает HUD"""
    speed_text = font.render(f"Speed: {speed:.1f}", True, WHITE)
    score_text = font.render(f"Coins: {score}", True, YELLOW)
    screen.blit(speed_text, (10, 10))
    screen.blit(score_text, (WIDTH - 120, 10))

def reset_game():
    """Сбрасывает игру для рестарта"""
    global game_active, player_x, speed, score, coins
    game_active = True
    player_x = WIDTH // 2 - 25
    speed = base_speed
    score = 0
    coins = []
    reset_enemy()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not game_active:
            if event.key == pygame.K_r:  
                reset_game()
    
    screen.blit(street, (0, 0))
    
    if game_active:
        # Управление игроком
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_x <= WIDTH - 90:
            player_x += 5
        if keys[pygame.K_LEFT] and player_x >= 40:
            player_x -= 5
        
        # Движение вражеской машины
        enemy_y += speed
        if enemy_y > HEIGHT:
            reset_enemy()
        
        # Генерация монет
        coin_spawn_timer += 1
        if coin_spawn_timer >= coin_spawn_interval:
            spawn_coin()
            coin_spawn_timer = 0
        
        # Движение монет
        for coin in coins[:]:
            coin.y += coin_speed
            if coin.y > HEIGHT:
                coins.remove(coin)
        
        # Проверка столкновений
        if check_collision():
            game_active = False
        check_coin_collision()  
        
        # Отрисовка объектов
        screen.blit(car, (player_x, player_y))
        screen.blit(traffic, (enemy_x, enemy_y))
        for coin in coins:
            screen.blit(coin_img, coin)
        
        # Отображение HUD
        show_hud()
    else:
        show_game_over()
        restart_text = font.render("Press R to restart", True, WHITE)
        screen.blit(restart_text, (WIDTH//2 - 80, HEIGHT//2 + 50))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()