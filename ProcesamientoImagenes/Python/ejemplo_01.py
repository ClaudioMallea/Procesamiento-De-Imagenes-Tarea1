#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ejemplo_01
An image plotted as a surface
@author: jsaavedr
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from skimage import  io


if __name__ == '__main__' :
    filename ='./images/gray/lion_gray.jpg'
    
    image=io.imread(filename)    
    start_p = (125,125)
    end_p = (150,150) 
    #a sub-image (region of interest) is extracted
    simage=image[start_p[0]:end_p[0], start_p[1]:end_p[1]]    

    #ready to display 
    fig, xs = plt.subplots(1,2)
    
    xs[0].imshow(simage, cmap='gray', vmax=255, vmin = 0)
    xs[0].axis('off')
    
    #mgrid yiends all the points defined in a region
    xx, yy = np.mgrid[0:simage.shape[0], 0:simage.shape[1]]
    xs[1]=fig.add_subplot(1,2,2,projection='3d')
    xs[1].plot_surface(xx, yy, simage, cmap='gray')
    xs[1].axis('on')
    plt.show()