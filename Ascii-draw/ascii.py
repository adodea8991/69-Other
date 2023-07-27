import random
import math

def draw_circle(radius):
    circle = []
    for y in range(-radius, radius + 1):
        row = ""
        for x in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                row += "@"
            else:
                row += " "
        circle.append(row)
    return circle

def print_ascii_circle(circle):
    for row in circle:
        print(row)

def random_size():
    return random.randint(5, 15)

def main():
    radius = random_size()
    circle = draw_circle(radius)
    print_ascii_circle(circle)

if __name__ == "__main__":
    main()
