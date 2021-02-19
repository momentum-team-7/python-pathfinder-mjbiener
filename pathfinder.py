from PIL import Image
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

# def get_max_el ():
    max_el = int(max(map(max, coordinates)))
    print(max_el)
    # return max_el
    

min_el = int(min(map(min, coordinates)))
print(min_el)

el_delta = int((max_el) - (min_el))
print (el_delta)

# difference between max and min needs to be scaled to difference between 255-0

def calc_color_value (elevation, min_el, max_el) :
    color_value = (((int(elevation) - min_el)/(el_delta)) * 255)
    # print (int(color_value), int(color_value), int(color_value))
    return (int(color_value), int(color_value), int(color_value))

# determines the pixel dimensions of the required picture 

dimensions = len(coordinates[0]), len(coordinates)
print (dimensions)

# img = Image.new('RGB', dimensions, color = (200, 200, 200))
# img.save ('solid_color_image.png')

img = Image.new('RGB', dimensions,)
for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            img.putpixel((y, x), calc_color_value(
                coordinates[x][y], min_el, max_el)) #changing putpixel to y,x rotated image 90 degrees and mirrored#
img.save(large[0:len(large)-3] + 'png')