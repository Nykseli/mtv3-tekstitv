from PIL import Image
from charmap import ABC, ABC_MAP
import sys
import io
from urllib import request

CELL_WIDTH = 10
CELL_HEIGHT = 12


#print( width, height)
#print (px[0, 15])
#px[4,4] = (0,0,0)
#print (px[4,4])

def what_letter(cell):

    # empty space
    if cell == [0,0,0,0]:
        sys.stdout.write(' ')
        return


    for i in range(len(ABC)):
        if ABC[i] == cell:
            sys.stdout.write(ABC_MAP[i])
            return

    # sys.stdout.write(str(cell))

def print_image(image_data):
    img = Image.open(io.BytesIO(image_data))
    #img = Image.open('896-01.gif')
    width, height = img.size
    px = img.load()

    startx = 0
    starty = 0
    while starty < height:
        while startx < width:
            tmpy = starty
            bg = px[startx, starty]
            cell = []
            for _ in range(4):
                power = 0
                tmp_sum = 0
                for y in range(tmpy, tmpy + 3):
                    for x in range(startx, startx + CELL_WIDTH):
                        if px[x, y] != bg:
                            tmp_sum += 2 ** power
                        power += 1
                cell.append(tmp_sum)
                tmpy += 3

            what_letter(cell)
            startx += CELL_WIDTH

        startx = 0
        sys.stdout.write('\n')
        starty += CELL_HEIGHT


    img.close()



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Page pls")
        exit(1)
    data = request.urlopen(f"http://www.mtvtekstikanava.fi/new2008/images/{sys.argv[1]}-01.gif").read()
    print(str(type(data)))
    print_image(data)
