import pygame
import random
import time


CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
BALL_RADIUS = 10
BALL_VEL_X = 5
BALL_VEL_Y = 5
BRICK_WIDTH = 80
BRICK_HEIGHT = 10
PEDAL_WIDTH = 130
PEDAL_HEIGHT = 15
GAP_BETWEEN_BRICKS = 10
GAP_BETWEEN_TOP_WALL_AND_BRICKS = 50
GAP_BETWEEN_SIDE_WALL_AND_BRICKS = 10
GAP_BETWEEN_ROW = 20
BRICK_NUM = 11


pygame.init()

screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption('Breakout')

#Renkler
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (169, 169, 169)

font = pygame.font.SysFont("Arial", 20)


ball_x = CANVAS_WIDTH // 2
ball_y = CANVAS_HEIGHT // 2
ball_vel_x = random.randint(2, 5)
ball_vel_y = random.randint(4, 7)


paddle_x = (CANVAS_WIDTH - PEDAL_WIDTH) // 2
paddle_y = CANVAS_HEIGHT - PEDAL_HEIGHT - 20

bricks = []
for i in range(6):
    for j in range(BRICK_NUM):
        brick = pygame.Rect(GAP_BETWEEN_SIDE_WALL_AND_BRICKS + j * (BRICK_WIDTH + GAP_BETWEEN_BRICKS),
                            GAP_BETWEEN_TOP_WALL_AND_BRICKS + i * (BRICK_HEIGHT + GAP_BETWEEN_ROW),
                            BRICK_WIDTH, BRICK_HEIGHT)
        color = [GREEN, BLUE, MAGENTA, PINK, ORANGE, YELLOW][i]
        bricks.append((brick, color))


life = 3
BRICK_NUM_DEL = len(bricks)


running = True
while running:
    screen.fill(GRAY)

    #Pedal
    pygame.draw.rect(screen, BROWN, (paddle_x, paddle_y, PEDAL_WIDTH, PEDAL_HEIGHT))

    # Draw ball
    pygame.draw.ellipse(screen, BLACK, (ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2))

    #Tuglalar
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    #Sayac
    life_text = font.render(f"Lives: {life}", True, BLACK)
    screen.blit(life_text, (550, 570))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mouse_x, _ = pygame.mouse.get_pos()
    paddle_x = min(max(0, mouse_x - PEDAL_WIDTH // 2), CANVAS_WIDTH - PEDAL_WIDTH)


    ball_x += ball_vel_x
    ball_y += ball_vel_y


    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= CANVAS_WIDTH:
        ball_vel_x = -ball_vel_x
    if ball_y - BALL_RADIUS <= 0:
        ball_vel_y = -ball_vel_y
    if ball_y + BALL_RADIUS >= CANVAS_HEIGHT:
        life -= 1
        if life <= 0:
            game_over_text = font.render("You Lose!", True, BLACK)
            screen.blit(game_over_text, (CANVAS_WIDTH // 2 - 70, CANVAS_HEIGHT // 2))
            pygame.display.update()
            time.sleep(2)
            running = False
        else:
            ball_x = CANVAS_WIDTH // 2
            ball_y = CANVAS_HEIGHT // 2
            ball_vel_x = random.randint(2, 5)
            ball_vel_y = random.randint(4, 7)


    if pygame.Rect(paddle_x, paddle_y, PEDAL_WIDTH, PEDAL_HEIGHT).colliderect(
            pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
        ball_vel_y = -ball_vel_y

    ball_rect = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
    for brick, color in bricks[:]:
        if brick.colliderect(ball_rect):
            ball_vel_y = -ball_vel_y
            bricks.remove((brick, color))
            BRICK_NUM_DEL -= 1
            if BRICK_NUM_DEL == 0:
                win_text = font.render("You Win!", True, BLACK)
                screen.blit(win_text, (CANVAS_WIDTH // 2 - 60, CANVAS_HEIGHT // 2))
                pygame.display.update()
                time.sleep(2)
                running = False
            break


    pygame.display.update()


    pygame.time.delay(20)


pygame.quit()
