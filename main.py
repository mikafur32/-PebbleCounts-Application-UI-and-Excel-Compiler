import subprocess
import os
import cv2

def yn(f, prompt, y_other, y_other_f):
    inp = f(prompt)
    while inp != 'y' and inp != 'n':
        inp = f(prompt)

    if inp == 'y':
        y_other_f(y_other)

    return inp == 'y'


def count(file, i):
    subprocess.call(
        'python PebbleCounts.py -im %s\\%d\\%d.tif -ortho y'
        % (file, i, i)
    )

    image = cv2.imread('%s\\%d\\%d_PebbleCounts_FIGURE.png'
                       % (file, i, i))
    #cv2.imshow('Figure', image)


#####################################################################################################################
'''
    PEBBLECOUNTING
'''
#####################################################################################################################
file = input('Enter the folder location of the tiles: ')
start = int(input('Which tile would you like to start on? '))


# Naming convention for the tiles:
# 1. Name each tile 1 through x
# 1.tif, 2.tif, 3.tif... x.tif
# 2. Place each numbered tile into a folder with the same number name
# 1.tif goes into the folder 1
# C:\  ...  \1\1.tif

for i in range(start, len(next(os.walk(file))[1])):
    print('Counting Pebbles on tile %d' % i)
    count(file, i)

    while yn(input, 'Redo %d? y/n ' % i,
             'python PebbleCounts.py -im %s\\%d\\%d.tif -ortho y'
             % (file, i, i),
             subprocess.call
             ) == True:
        count(file, i)
