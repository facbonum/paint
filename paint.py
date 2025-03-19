import pygame
import math

pygame.init()

fps = 144
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 20
active_color = 'white'
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)  # Make the window resizable
pygame.display.set_caption("Paint!")
painting = []
last_pos = None  # Store the last mouse position to draw lines

def draw_menu(size, color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Define brush variables here
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50], 3)
    pygame.draw.circle(screen, 'white', (35, 35), 20)

    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50], 3)
    pygame.draw.circle(screen, 'white', (90, 35), 15)

    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50], 3)
    pygame.draw.circle(screen, 'white', (166, 35), 10)

    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50], 3)
    pygame.draw.circle(screen, 'white', (215, 35), 5)

    xs_brush = pygame.draw.rect(screen, 'black', [250, 10, 50, 50], 3)
    pygame.draw.circle(screen, 'white', (35, 35), 5)  # Slightly bigger brush for visibility

    # Add brush size to the list
    brush_list = [xl_brush, l_brush, m_brush, s_brush, xs_brush]

    # Active color circle
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Define color rectangles horizontally aligned
    color_rects = [
        pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 295, 10, 25, 25]),  # Blue
        pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 260, 10, 25, 25]),  # Red
        pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 225, 10, 25, 25]),  # Green
        pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 190, 10, 25, 25]),  # Yellow
        pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 155, 10, 25, 25]),  # Teal
        pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 120, 10, 25, 25]),  # Purple
        pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 85, 10, 25, 25]),  # White
        pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 50, 10, 25, 25]),  # Black
        pygame.draw.rect(screen, (139, 69, 19), [WIDTH - 35, 10, 25, 25]),  # Brown
        pygame.draw.rect(screen, (255, 165, 0), [WIDTH - 35, 35, 25, 25]),  # Orange
        pygame.draw.rect(screen, (255, 20, 147), [WIDTH - 35, 60, 25, 25]),  # Deep Pink
        pygame.draw.rect(screen, (0, 128, 128), [WIDTH - 35, 85, 25, 25]),  # Teal (Darker)
        pygame.draw.rect(screen, (255, 99, 71), [WIDTH - 35, 110, 25, 25]),  # Tomato Red
    ]

    # Add color rects to the list
    color_rect = color_rects

    # Define RGB values for colors
    rgb_list = [
        (0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), 
        (255, 0, 255), (0, 0, 0), (255, 255, 255), (139, 69, 19), (255, 165, 0), 
        (255, 20, 147), (0, 128, 128), (255, 99, 71)
    ]

    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

def draw_line_between_points(start, end, color, radius):
    """Draw a line between two points to make the stroke more continuous."""
    pygame.draw.line(screen, color, start, end, radius)

run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    if left_click and mouse[1] > 70:
        # If the left click is pressed, draw between the previous and current position
        if last_pos:
            # Draw line between last position and current position
            draw_line_between_points(last_pos, mouse, active_color, active_size)
        last_pos = mouse  # Update the last position for the next frame
        painting.append((active_color, mouse, active_size))  # Append as a tuple

    draw_painting(painting)

    if mouse[1] > 70:  # Brush size tracking cursor
        pygame.draw.circle(screen, active_color, mouse, active_size)  # Draw active size cursor

    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Stop the game loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)  # Brush size selection logic

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]  # Color selection

    # Call draw_menu with correct arguments
    draw_menu(active_size, active_color)

    pygame.display.flip()

pygame.quit()
