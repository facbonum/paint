import pygame

pygame.init()

# Screen properties
WIDTH = 860
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint!")

# Brush state variables
active_size = 20
active_color = (0, 0, 0)  # Default to black
painting = []  # List of painting data (color, position, size)

# Initialize clock and FPS
fps = 144
timer = pygame.time.Clock()

# Default canvas color
canvas_color = (255, 255, 255)  # White canvas

# Create canvas surface
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(canvas_color)

def draw_menu(size, color):
    """Draw the brush sizes and color palette at the top."""
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])  # Original height for menu bar
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Brush sizes
    brush_sizes = [20, 15, 10, 5, 2]
    for i, brush_size in enumerate(brush_sizes):
        pygame.draw.rect(screen, 'black', [10 + (i * 60), 10, 50, 50], 3)
        pygame.draw.circle(screen, 'white', (35 + (i * 60), 35), brush_size)

    # Active color circle
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Primary color selection (arranged horizontally)
    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), 
              (255, 0, 255), (0, 0, 0), (255, 255, 255), (150, 0, 255), (170, 170, 100), (200, 140, 200)]
    for i, color_rect in enumerate(colors):
        pygame.draw.rect(screen, color_rect, [WIDTH - 380 + (i * 35), 10, 25, 25])

    # Custom color selection (beneath the primary colors)
    custom_colors = [(165, 42, 42), (255, 69, 0), (70, 170, 255), (255, 105, 180), 
                     (255, 215, 0), (0, 128, 128), (128, 0, 128), (255, 20, 147), 
                     (0, 100, 255), (90, 255, 200), (20, 0, 180)]
    for i, color_rect in enumerate(custom_colors):
        pygame.draw.rect(screen, color_rect, [WIDTH - 380 + (i * 35), 40, 25, 25])  # Placing below the primary colors

    return brush_sizes, colors, custom_colors

def draw_painting(paints):
    """Draw all the painted strokes on the canvas."""
    for color, position, size in paints:
        pygame.draw.circle(canvas, color, position, size)

run = True
while run:
    timer.tick(fps)

    # Handle window events
    screen.fill('white')  # Fill the screen with the background color
    screen.blit(canvas, (0, 0))  # Draw the canvas (painted strokes)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    # Handle painting if the user clicks the mouse
    if left_click and mouse[1] > 70:  # Only paint below the menu (70px is menu height)
        painting.append((active_color, mouse, active_size))  # Append brush info to painting list
        draw_painting(painting)  # Redraw painting strokes

    # Brush size tracking cursor
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)

    brush_sizes, colors, custom_colors = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Quit the game loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle brush size selection
            for i, brush_size in enumerate(brush_sizes):
                if pygame.Rect(10 + (i * 60), 10, 50, 50).collidepoint(event.pos):
                    active_size = brush_size  # Set active brush size

            # Handle primary color selection
            for i, color_rect in enumerate(colors):
                if pygame.Rect(WIDTH - 380 + (i * 35), 10, 25, 25).collidepoint(event.pos):
                    active_color = color_rect  # Set active color

            # Handle custom color selection (beneath primary colors)
            for i, color_rect in enumerate(custom_colors):
                if pygame.Rect(WIDTH - 380 + (i * 35), 40, 25, 25).collidepoint(event.pos):
                    active_color = color_rect  # Set active custom color

    pygame.display.flip()

pygame.quit()
