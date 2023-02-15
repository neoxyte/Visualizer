import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Neo's fractal Generator")

# Fractal Constraints
X_MIN, X_MAX = -2, 2
Y_MIN, Y_MAX = -2, 2
MAX_ITERATIONS = 1000
COLOR_SCHEME = [(66, 30, 15), (25, 7, 26), (9, 1, 47), (4, 4, 73), (0, 7, 100), (12, 44, 138), (24, 82, 177), (57, 125, 209), (134, 181, 229), (211, 236, 248), (241, 233, 191), (248, 201, 95), (255, 170, 0), (204, 128, 0), (153, 87, 0), (106, 52, 3)]

# Define the function to calculate the Mandelbrot set
def calculate_mandelbrot(c):
    z = 0
    for i in range(MAX_ITERATIONS):
        if abs(z) > 2:
            return i
        z = z**2 + c
    return MAX_ITERATIONS

# Define the main function
def main():
    # Loop through all the pixels in the screen and calculate the corresponding color
    for x in range(800):
        for y in range(800):
            # Convert the pixel coordinates to the corresponding complex number
            c = complex(X_MIN + (x / 800) * (X_MAX - X_MIN), Y_MIN + (y / 800) * (Y_MAX - Y_MIN))

            # Calculate the color of the pixel based on the number of iterations required to escape
            iterations = calculate_mandelbrot(c)
            color = COLOR_SCHEME[iterations % len(COLOR_SCHEME)]

            # Set the pixel color on the screen
            screen.set_at((x, y), color)

    # Update the Pygame window
    pygame.display.update()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()