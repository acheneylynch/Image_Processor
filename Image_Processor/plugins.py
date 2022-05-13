"""
Plugin utilites for the pictool.

This module contains all of the commands supported by the application script pictool.py.
To be a valid command, a function must (1) have a first parameter 'image' for the
image buffer, (2) assign default values to parameters after the first, and (3)
return True if it modifies the image and False if not.  You can use these rules to
make your own plugin utilities.

Only three four functions -- mono, flip, transpose, and rotate -- are required for this
project.  All others are optional, though the folder 'solutions' does contain examples
for each of them.

IMPORTANT: It is highly recommended that these functions enforce the preconditions for
any parameter after images.  Otherwise, command line typos may be hard to debug.

Author: Aidan Cheney-Lynch
Date: 05/11/22
"""


# Function useful for debugging
def display(image):
    """
    Returns False after pretty printing the image pixels, one pixel per line.

    All plug-in functions must return True or False.  This function returns False
    because it displays information about the image, but does not modify it.

    You can use this function to look at the pixels of a file and see whether the
    pixel values are what you expect them to be.  This is helpful to analyze a file
    after you have processed it.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects
    """
    height = len(image)
    width  = len(image[0])

    # Find the maximum string size for padding
    maxsize = 0
    for row in image:
        for pixel in row:
            text = repr(pixel)
            if len(text) > maxsize:
                maxsize = len(text)

    # Pretty print the pixels
    print()
    for pos1 in range(height):
        row = image[pos1]
        for pos2 in range(width):
            pixel = row[pos2]

            middle = repr(pixel)
            padding = maxsize-len(middle)

            prefix = '      '
            if pos1 == 0 and pos2 == 0:
                prefix = '[  [  '
            elif pos2 == 0:
                prefix = '   [  '

            suffix = ','
            if pos1 == height-1 and pos2 == width-1:
                suffix = (' '*padding)+' ]  ]'
            elif pos2 == width-1:
                suffix = (' '*padding)+' ],'

            print(prefix+middle+suffix)

    # This function does not modify the image
    return


# Example function illustrating image manipulation
def dered(image):
    """
    Returns True after removing all red values from the given image.

    All plug-in functions must return True or False.  This function returns True
    because it modifies the image. This function sets the red value to 0 for every
    pixel in the image.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects
    """
    # Get the image size
    height = len(image)
    width  = len(image[0])

    for row in range(height):
        for col in range(width):
            pixel = image[row][col]
            pixel.red = 0

    # This function DOES modify the image
    return True

def mono(image, sepia=False):
    """
    Returns True after converting the image to monochrome.

    All plug-in functions must return True or False.  This function returns True
    because it modifies the image. It converts the image to either greyscale or
    sepia tone, depending on the parameter sepia.

    If sepia is False, then this function uses greyscale.  For each pixel, it computes
    the overall brightness, defined as

        0.3 * red + 0.6 * green + 0.1 * blue.

    It then sets all three color components of the pixel to that value. The alpha value
    should remain untouched.

    If sepia is True, it makes the same computations as before but sets green to
    0.6 * brightness and blue to 0.4 * brightness.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects

    Parameter sepia: Whether to use sepia tone instead of greyscale
    Precondition: sepia is a bool
    """

    # Enforce the precondition for sepia
    assert type(sepia) == bool

    height = len(image)
    width = len(image[0])

    for row in range(height):

        for col in range(width):

            pixel = image[row][col]
            brightness = pixel.red * 0.3 + pixel.green * 0.6 + pixel.blue * 0.1

            if sepia==False:

                pixel.red = int(brightness)
                pixel.green = int(brightness)
                pixel.blue = int(brightness)

            if sepia==True:

                pixel.red = int(brightness)
                pixel.green = int(0.6*brightness)
                pixel.blue = int(0.4*brightness)

    # Change this to return True when the function is implemented
    #return False
    return True

def flip(image,vertical=False):
    """
    Returns True after reflecting the image horizontally or vertically.

    All plug-in functions must return True or False.  This function returns True
    because it modifies the image. By default it reflects the image horizonally,
    or vertically if vertical is True.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects

    Parameter vertical: Whether to reflect the image vertically
    Precondition: vertical is a bool
    """

    # Enforce the precondition for vertical
    assert type(vertical) == bool

    height = len(image)
    width = len(image[0])

    # Horizontal Flip
    if vertical == False:
        for col in range(height):
            image[col].reverse()

    # Vertical Flip
    if vertical == True:
        image.reverse()

    # Change this to return True when the function is implemented
    return True
    #return False

def transpose(image):
    """
    Returns True after transposing the image

    All plug-in functions must return True or False.  This function returns True
    because it modifies the image. It transposes the image, swaping colums and rows.

    Transposing is tricky because you cannot just change the pixel values; you have
    to change the size of the image table.  A 10x20 image becomes a 20x10 image.

    The easiest way to transpose is to make a transposed copy with the pixels from
    the original image.  Then remove all the rows in the image and replace it with
    the rows from the transposed copy.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects
    """

    # To loop through rows
    numrows = len(image)

    # To loop through columns
    numcols = len(image[0])

    # Accumulator variable for rotated copy of image
    result = []

    # For-loop to iterate through columns
    for co in range(numcols):

        row = []

        # For-loop to iterate through rows
        for ro in range(numrows):

            row.append(image[ro][co])

        result.append(row)

    # Clear image
    image.clear()

    # Loop through row of result
    for row in result:

        # Append row to image
        image.append(row)

    # Change this to return True when the function is implemented
    #return False
    return True

def rotate(image,right=False):
    """
    Returns True after rotating the image left of right by 90 degrees.

    All plug-in functions must return True or False.  This function returns True
    because it modifies the image. By default it rotates the image left, or right
    if parameter right is True.

    To rotate left, transpose and then flip vertically.  To rotate right, flip
    vertically first and then transpose.

    Parameter image: The image buffer
    Precondition: image is a 2d table of RGB objects

    Parameter right: Whether to rotate the image right
    Precondition: right is a bool
    """
    # Enforce the precondition for right
    assert type(right) == bool

    # Rotate image left
    if right == False:
        transpose(image)
        image.reverse()

    # Rotate image right
    if right == True:
        image.reverse()
        transpose(image)

    # Change this to return True when the function is implemented
    #return False
    return True
