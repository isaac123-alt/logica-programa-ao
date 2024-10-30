import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Fútbol Mejorado")

# Colores
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Clases para el jugador, la pelota, el oponente y la portería
class Player:
    def __init__(self):
        self.rect = pygame.Rect(width // 2, height // 2, 50, 50)
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.x = max(0, min(self.rect.x, width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, height - self.rect.height))

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, width - 20), random.randint(0, height - 20), 20, 20)
        self.speed_x = 0
        self.speed_y = 0

    def kick(self, dx, dy):
        self.speed_x = dx * 10  # Cambia la velocidad horizontal
        self.speed_y = dy * -10  # Cambia la velocidad vertical

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Fricción
        self.speed_x *= 0.95
        self.speed_y *= 0.95

        # Limitar velocidad
        if abs(self.speed_x) < 1:
            self.speed_x = 0
        if abs(self.speed_y) < 1:
            self.speed_y = 0

        # Mantener la pelota dentro de los límites de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed_x = 0
        elif self.rect.x > width - 20:
            self.rect.x = width - 20
            self.speed_x = 0
        
        if self.rect.y < 0:
            self.rect.y = 0
            self.speed_y = 0
        elif self.rect.y > height - 20:
            self.rect.y = height - 20
            self.speed_y = 0

class Goal:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 10)

class Opponent:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, width - 50), random.randint(0, height // 2), 50, 50)
        self.speed = 2

    def move(self, ball_rect):
        if self.rect.x < ball_rect.x:
            self.rect.x += self.speed
        elif self.rect.x > ball_rect.x:
            self.rect.x -= self.speed
        if self.rect.y < ball_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > ball_rect.y:
            self.rect.y -= self.speed

# Inicializar jugador, pelota, portería y oponente
player = Player()
ball = Ball()
goal = Goal(width // 2 - 50, height - 50)
opponent = Opponent()

# Marcador y temporizador
score = 0
timer = 60  # 60 segundos
font = pygame.font.Font(None, 36)

# Ciclo del juego
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()  # Temporizador de inicio

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manejo de teclas
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1
    player.move(dx, dy)

    if keys[pygame.K_SPACE]:  # Patear la pelota
        if player.rect.colliderect(ball.rect):
            ball.kick(dx, dy)  # Patear en la dirección del movimiento

    # Actualizar la pelota
    ball.update()

    # Mover oponente
    opponent.move(ball.rect)

    # Colisión con la portería
    if ball.rect.colliderect(goal.rect):
        score += 1
        ball.rect.x = random.randint(0, width - 20)
        ball.rect.y = random.randint(0, height - 20)
        opponent = Opponent()  # Reiniciar oponente en nueva posición

    # Actualizar temporizador
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Segundos
    if seconds > timer:
        running = False

    # Dibujar todo
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, player.rect)  # Jugador
    pygame.draw.ellipse(screen, RED, ball.rect)    # Pelota
    pygame.draw.rect(screen, BLACK, goal.rect)     # Portería
    pygame.draw.rect(screen, BLUE, opponent.rect)  # Oponente

    # Mostrar marcador y temporizador
    score_text = font.render(f"Puntos: {score}", True, BLACK)
    timer_text = font.render(f"Tiempo: {timer - int(seconds)}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (width - 150, 10))

    pygame.display.flip()
    clock.tick(60)

# Fin del juego
screen.fill(GREEN)
end_text = font.render(f"Fin del juego! Puntos: {score}", True, BLACK)
screen.blit(end_text, (width // 2 - 150, height // 2 - 20))
pygame.display.flip()
pygame.time.delay(3000)

pygame.quit()
