# The floodfill algorithm will fill any enclosed shape(s) with
# a color

image = [
    """
    "....########........"
    "....#......#........"
    "....#......#........"
    "....#..#######......"
    "....#..#.....#......"
    "....####.....######."
    "....#.............#."
    "....###############."
    "...................."
    "...................."
    """
]

def print_image():
    for line in image:
        print("".join(line))

def floodfill(row, col, c):
    floodfill(...)

print_image()
floodfill(2,5, "*")