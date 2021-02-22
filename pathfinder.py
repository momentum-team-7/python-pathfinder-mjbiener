from PIL import Image
import random
small = 'elevation_small.txt'
large = 'elevation_large.txt'
test = 'test_grid.txt'

coordinates = []

with open(large, 'r') as file:
    for line in file.readlines():
        coordinates.append(line.split())
    print(coordinates)

# need to find the min value in the list (will be set to black 0, 0, 0)
# need to find the max value in the list (will be set to white 255, 255, 255)


max_el = int(max(map(max, coordinates)))
print(max_el)

min_el = int(min(map(min, coordinates)))
print(min_el)

el_delta = int((max_el) - (min_el))
print (el_delta)

# difference between max and min scaled to difference between 255-0

def calc_color_value (elevation, min_el, max_el) :
    color_value = (((int(elevation) - min_el)/(el_delta)) * 255)
    # print (int(color_value), int(color_value), int(color_value))
    return (int(color_value), int(color_value), int(color_value))

# determines the pixel dimensions of the required picture 

dimensions = len(coordinates[0]), len(coordinates)
print (dimensions)

img = Image.new('RGB', dimensions,)
for y in range(dimensions[1]):
        for x in range(dimensions[0]):
            img.putpixel((x, y), calc_color_value(
                coordinates[y][x], min_el, max_el)) 
img.save(large[0:len(large)-3] + 'png')



# Code below adapted from Tatiana and Ben #

greedy_path = []


def draw_path(draw_line):
    img.putpixel(draw_line, (15, 230, 172))


def find_lowest_delta(current, top, straight, bottom):
    top_delta = current - top
    straight_delta = current - straight
    bottom_delta = current - bottom
    lowest_delta = min([top_delta, straight_delta, bottom_delta])
    if lowest_delta == top_delta:
        return top
    elif lowest_delta == straight_delta:
        return straight
    elif lowest_delta == bottom_delta:
        return bottom


def find_greedy_path():
    length_of_file = len(coordinates[0]) - 1
    height_of_file = len(coordinates) - 1
    x = 0
    y = int(input(f"Pick a starting point between 0 and {length_of_file}: "))
    for coordinate in range(len(coordinates)):
        draw_path((x, y))
        current_position = int(coordinates[y][x])

        x = x + 1
        top = y - 1
        bottom = y + 1
        straight = y

        top_el = int(coordinates[top][x])
        straight_el = int(coordinates[straight][x])
        bottom_el = int(coordinates[bottom][x])
        low_el = find_lowest_delta(
            current_position, top_el, straight_el, bottom_el)
        
        # if low_el ==  (top_el and bottom_el):
        #     top_or_bottom = [top, bottom]
        #     y = coinflip(top_or_bottom)
        if low_el == top_el:
            y = top
        elif low_el == bottom_el:
            y = bottom
        elif low_el == straight_el:
            y = straight
        if x == length_of_file:
            img.save('greedy_path' + large[0:len(large)-3] + 'png')
            return

def coinflip(top_or_bottom):
    return top_or_bottom[random.randint(0,1)]

find_greedy_path()