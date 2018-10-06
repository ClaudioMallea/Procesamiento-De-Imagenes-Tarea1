#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAI ejemplo_00
Loading and manipulating images using scikit-image (https://scikit-image.org/)
It is also possible to use OpenCv (cv2 module)
@author: jsaavedr
"""
import numpy as np
from skimage import io
from skimage import draw
import matplotlib.pyplot as plt


# %%
def drawRectangle(image, start_p, end_p, color):
    """
    Draw the perimenter of a rectangle on an image, from start_p(r,c) to end_p(r,c)
    """
    rr_1, cc_1 = draw.line(start_p[0], start_p[1], start_p[0], end_p[1])
    image[rr_1, cc_1] = color
    rr_1, cc_1 = draw.line(start_p[0], end_p[1], end_p[0], end_p[1])
    image[rr_1, cc_1] = color
    rr_1, cc_1 = draw.line(end_p[0], end_p[1], end_p[0], start_p[1])
    image[rr_1, cc_1] = color
    rr_1, cc_1 = draw.line(end_p[0], start_p[1], start_p[0], start_p[1])
    image[rr_1, cc_1] = color


# %%
if __name__ == '__main__':
    filename = './images/gray/lion_gray.jpg'
    # reading an image into a numpy array
    image = io.imread(filename)
    print(image.shape)
    start_p = (125, 125)
    end_p = (150, 150)
    simage = image[start_p[0]:end_p[0], start_p[1]:end_p[1]]
    # the region of interest (roi) is drawn on the image
    drawRectangle(image, start_p, end_p, 255)
    # ------------------------------------------------------------------
    fig, xs = plt.subplots(1, 2)
    xs[0].imshow(image, cmap='gray', vmax=255, vmin=0)
    xs[0].axis('off')

    xs[1].imshow(simage, cmap='gray', vmax=255, vmin=0)
    xs[1].axis('off')
    print(simage)
    plt.show()
