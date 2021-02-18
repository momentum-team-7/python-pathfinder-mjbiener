coordinates = []

with open('elevation_small.txt', 'r') as file:
    for line in file.readlines():
        coordinates.append(line.split())
    print(coordinates)

# need to find the min value in the list (will be set to black 0, 0, 0)
# need to find the max value in the list (will be set to white 255, 255, 255)
# difference between max and min will be scaled to difference between 255-0

max_el = int(max(map(max, coordinates)))
print(max_el)

min_el = int(min(map(min, coordinates)))
print(min_el)

el_delta = int((max_el) - (min_el))
print (el_delta)



from PIL import Image
img = Image.new('RGB', (600, 600), color = (200, 200, 200))
img.save ('solid_color_image.png')

