#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ejemplo_05
Thresholding with Otsu
@author: jsaavedr
"""


from skimage import  io
import Python.pai.basic  as pai
import matplotlib.pyplot as plt

if __name__ == '__main__' :
    filename ='./images/gray/car_2.png'
    image=io .imread(filename)
    #otsu_v = filters.threshold_otsu(image)
    otsu_th = pai.getOtsu(image)
    bin_image = pai.threshold(image, otsu_th)
    print ("otsu value: {}".format(otsu_th))
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].axis('off')
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[0].set_title("Original")
    xs[1].imshow(bin_image*255, cmap = 'gray', vmin = 0, vmax = 255)
    xs[1].set_title("Thresholded image")
    plt.show()