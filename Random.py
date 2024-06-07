# import turtle
# screen = turtle.Screen()
# turtle_circle = turtle.Turtle()

# turtle_circle.pensize(3)
# turtle_circle.color("blue")
# turtle_circle.penup()
# turtle_circle.goto(0,-100)
# turtle_circle.pendown()
# turtle_circle.fillcolor("blue")
# turtle_circle.begin_fill()
# turtle.circle(200)
# turtle_circle.end_fill()
# screen.exitonclick()


# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the display
# width, height = 400, 400
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Filled Circle")

# # Set the color
# circle_color = (0, 0, 255)  # Blue color

# # Draw a filled circle
# radius = 100
# center = (width // 2, height // 2)
# pygame.draw.circle(screen, circle_color, center, radius)

# # Update the display
# pygame.display.flip()

# # Run the event loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Quit Pygame
# pygame.quit()
# sys.exit()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create the Tic Tac Toe board
board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to draw the Tic Tac Toe grid
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

# Function to draw X or O in a cell
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 120)
    text = font.render(symbol, True, X_COLOR if symbol == 'X' else O_COLOR)
    text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text, text_rect)

# Function to check for a win
def check_win(symbol):
    # Check rows and columns
    for i in range(GRID_SIZE):
        if all(board[i][j] == symbol for j in range(GRID_SIZE)) or all(board[j][i] == symbol for j in range(GRID_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - i - 1] == symbol for i in range(GRID_SIZE)):
        return True

    return False

# Function to check for a draw
def check_draw():
    return all(board[i][j] != ' ' for i in range(GRID_SIZE) for j in range(GRID_SIZE))

# Main game loop
turn = 'X'
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if board[row][col] == ' ':
                board[row][col] = turn
                draw_symbol(row, col, turn)

                if check_win(turn):
                    print(f"{turn} wins!")
                    game_over = True
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    turn = 'O' if turn == 'X' else 'X'

    draw_grid()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
