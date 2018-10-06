#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ejemplo_04
Image Histogram
@author: jsaavedr
"""


import numpy as np
from skimage import data, io, filters, color
import pai.basic  as pai
import matplotlib.pyplot as plt

if __name__ == '__main__' :
    filename ='./images/gray/ten_coins.png'
    image=io .imread(filename)
    
    h = pai.getHistogram(image)
    
    fig, xs = plt.subplots(1,2)
    for i in range(2):
        xs[i].axis('off')
        
    xs[0].imshow(image, cmap = 'gray', vmin =0 , vmax=255)
    xs[1].bar(x=np.arange(256), height=h)
    xs[1].axis('on')
    plt.show()








