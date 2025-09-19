import random
import os
iterations = 20
terminal_width = int(input("What's the width of the terminal?: "))
terminal_height = int(input("What's the height of the terminal?: "))
square_size = int(input("What's the size of the character?: "))
signe = input("What's the sing?: ")
def clear_terminal():
    os.system('clear')

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def place_square(grid, x, y):

    for i in range(square_size):
        for j in range(square_size):
            if 0 <= x + i < terminal_height and 0 <= y + j < terminal_width:
                grid[x + i][y + j] = signe

def generate_random_point_from_square(x, y):

    rand_x = random.randint(x, x + square_size - 1)
    rand_y = random.randint(y, y + square_size - 1)
    return rand_x, rand_y

def is_square_within_bounds(x, y):

    return (0 <= x <= terminal_height - square_size) and (0 <= y <= terminal_width - square_size)

def main():
 
    grid = [[' ' for _ in range(terminal_width)] for _ in range(terminal_height)]
    
    current_x, current_y = random.randint(0, terminal_height - square_size), random.randint(0, terminal_width - square_size)

    iterations = int(input("Enter the number of squares to generate: "))

    for _ in range(iterations):

        while not is_square_within_bounds(current_x, current_y):
            current_x, current_y = random.randint(0, terminal_height - square_size), random.randint(0, terminal_width - square_size)

        place_square(grid, current_x, current_y)

        current_x, current_y = generate_random_point_from_square(current_x, current_y)

    clear_terminal()
    print_grid(grid)

if __name__ == "__main__":
    main()