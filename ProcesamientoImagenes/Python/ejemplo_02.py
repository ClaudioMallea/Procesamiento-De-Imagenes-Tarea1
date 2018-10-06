#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Loading 3-channel color images
@author: jsaavedr
"""
import matplotlib.pyplot as plt
from skimage import io
#import numpy as np
#import pai.basic as  pai

if __name__ == '__main__': 
    filename = 'images/color/mm.jpg'
    image=io .imread(filename)
    
    red = image[:,:,0]    
    green = image[:,:,1]
    blue = image[:,:,2]
    
    
#    yellow = (1.2*red.astype(np.float32)*green.astype(np.float32)/255 - blue.astype(np.float32))
#    print(yellow)
#    yellow = pai.toUINT8(yellow)
    

    fig, xs = plt.subplots(1,4)
    for i in range(4):
        xs[i].set_axis_off()
        
    xs[0].imshow(image)
    xs[0].set_title("Image")
    xs[1].imshow(red, cmap="gray", vmin=0, vmax=255)
    xs[1].set_title("Red")
    xs[2].imshow(green, cmap="gray", vmin=0, vmax=255)
    xs[2].set_title("Green")
    xs[3].imshow(blue, cmap="gray", vmin=0, vmax=255)
    xs[3].set_title("Blue")
    plt.show()
    
