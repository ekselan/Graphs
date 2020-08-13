import sys
import time

# The floodfill algorithm will fill any enclosed shape(s) with
# a color

image = [
    list("....########........"),
    list("....#......#........"),
    list("....#......#........"),
    list("....#..#######......"),
    list("....#..#.....#......"),
    list("....####.....######."),
    list("....#.............#."),
    list("....###############."),
    list("...................."),
    list("....................")
]

def print_image():
    for line in image:
        print("".join(line))

def floodfill(row, col, c):
    if row < 0 or row > len(image) -1 or col < 0 or col > len(image[0]) - 1:
        return

    if image[row][col] != ".":
        return

    image[row][col] = c

    sys("clear")
    print_image()
    time.sleep(0.25)

    # north neighbor
    floodfill(row-1, col, c)
    # south
    floodfill(row+1, col, c)
    # east
    floodfill(row, col+1, c)
    # west
    floodfill(row, col-1, c)

if __name__ == "__main__":
    
    floodfill(2, 5, "*")
    # print_image()
    # print("---" * 10)
    # floodfill(1, 1, "$")
    # print_image()