import pygame
import random
import time


pygame.init()


CELL_SIZE = 40  
CELL_NUMBER = 20  
SCREEN_SIZE = CELL_SIZE * CELL_NUMBER  

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Улучшенная змейка")
clock = pygame.time.Clock()

class Food:
    """Класс для представления еды с разными типами"""
    def __init__(self):
        # Случайный выбор типа еды с разными вероятностями
        self.type = random.choices(
            ['normal', 'bonus', 'timed'], 
            weights=[70, 20, 10],  \
            k=1
        )[0]
        
        # Запоминаем время создания еды
        self.spawn_time = time.time()
        # Время жизни только для временной еды
        self.lifetime = random.randint(5, 10) if self.type == 'timed' else float('inf')
        
        # Генерируем позицию, не занятую змейкой
        self.x, self.y = self.generate_position()
        
        # Настройки в зависимости от типа еды
        if self.type == 'normal':
            self.color = RED  # Обычная еда - красная
            self.points = 1   # Дает 1 очко
        elif self.type == 'bonus':
            self.color = YELLOW  # Бонусная еда - желтая
            self.points = 3     # Дает 3 очка
        else:  # timed
            self.color = BLUE   # Временная еда - синяя
            self.points = 2     # Дает 2 очка

    def generate_position(self):
        """Генерирует случайную позицию на поле, не занятую змейкой"""
        while True:
            x = random.randint(0, CELL_NUMBER - 1) * CELL_SIZE
            y = random.randint(0, CELL_NUMBER - 1) * CELL_SIZE
            if [x, y] not in snake.snake_lst:
                return x, y

    def is_expired(self):
        """Проверяет, истекло ли время жизни еды (только для временной еды)"""
        return time.time() - self.spawn_time > self.lifetime

    def draw(self):
        """Отрисовывает еду на экране"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))
        
        # Для временной еды отображаем оставшееся время
        if self.type == 'timed':
            remaining = max(0, self.lifetime - (time.time() - self.spawn_time))
            font = pygame.font.SysFont(None, 20)
            text = font.render(f"{int(remaining)}", True, WHITE)
            screen.blit(text, (self.x + 10, self.y + 10))

class Snake:
    """Класс для представления змейки"""
    def __init__(self):
        self.reset()  # Инициализация змейки
        
    def reset(self):
        """Сбрасывает змейку в начальное состояние"""
        # Начальная позиция в центре поля
        self.x = (CELL_NUMBER // 2) * CELL_SIZE
        self.y = (CELL_NUMBER // 2) * CELL_SIZE
        self.snake_lst = [[self.x, self.y]]  # Список сегментов змейки
        self.direction = "RIGHT"  # Начальное направление
        self.length = 1  # Начальная длина
        self.score = 0   # Счет
        self.level = 1   # Уровень
        
    def move(self):
        """Двигает змейку в текущем направлении"""
        if self.direction == "UP":
            self.y -= CELL_SIZE
        elif self.direction == "DOWN":
            self.y += CELL_SIZE
        elif self.direction == "LEFT":
            self.x -= CELL_SIZE
        elif self.direction == "RIGHT":
            self.x += CELL_SIZE
            
        # Добавляем новую голову
        self.snake_lst.insert(0, [self.x, self.y])
        
        # Удаляем хвост, если змейка не выросла
        if len(self.snake_lst) > self.length:
            self.snake_lst.pop()
            
    def grow(self, points):
        """Увеличивает змейку и добавляет очки"""
        self.length += points
        self.score += points
        
        # Повышаем уровень каждые 5 очков
        if self.score // 5 > self.level - 1:
            self.level += 1
            
    def check_collision(self):
        """Проверяет столкновения с границами и самой собой"""
        # Столкновение с границами поля
        if (self.x < 0 or self.x >= SCREEN_SIZE or 
            self.y < 0 or self.y >= SCREEN_SIZE):
            return True
            
        # Столкновение с собственным телом (кроме головы)
        for segment in self.snake_lst[1:]:
            if segment == [self.x, self.y]:
                return True
                
        return False
        
    def draw(self):
        """Отрисовывает змейку на экране"""
        for segment in self.snake_lst:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Инициализация объектов
snake = Snake()
current_food = Food()  # Первая еда
game_active = True  # Состояние игры

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Управление змейкой и рестарт
        if event.type == pygame.KEYDOWN:
            if game_active:
                # Управление направлениями (проверка на противоположное направление)
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
            elif event.key == pygame.K_r:  # Рестарт при нажатии R
                snake.reset()
                current_food = Food()
                game_active = True
                fps = 10  # Сброс скорости
    
    if game_active:
        # Движение змейки
        snake.move()
        
        # Проверка столкновений
        if snake.check_collision():
            game_active = False
        
        # Проверка съедания еды
        if [snake.x, snake.y] == [current_food.x, current_food.y]:
            snake.grow(current_food.points)
            current_food = Food()  
        elif current_food.is_expired():  # Проверка истечения времени еды
            current_food = Food()
        
        # Отрисовка игры
        screen.fill(WHITE)  # Белый фон
        current_food.draw()  # Еда
        snake.draw()        # Змейка
        
        # Отображение информации (счет и уровень)
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Счет: {snake.score}", True, BLACK)
        level_text = font.render(f"Уровень: {snake.level}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        
        # Увеличение скорости с уровнем
        fps = 5 + snake.level * 2
    else:
        # Экран завершения игры
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 50)
        game_over_text = font.render("Игра окончена!", True, RED)
        score_text = font.render(f"Финальный счет: {snake.score}", True, BLACK)
        restart_text = font.render("Нажмите R для рестарта", True, BLACK)
        
        # Позиционирование текста
        screen.blit(game_over_text, (SCREEN_SIZE//2 - 150, SCREEN_SIZE//2 - 50))
        screen.blit(score_text, (SCREEN_SIZE//2 - 150, SCREEN_SIZE//2 + 10))
        screen.blit(restart_text, (SCREEN_SIZE//2 - 180, SCREEN_SIZE//2 + 70))
    
    # Обновление экрана
    pygame.display.flip()
    # Ограничение FPS (увеличивается с уровнем)
    clock.tick(fps)

# Завершение Pygame
pygame.quit()