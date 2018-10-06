#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracting yellow regions
Playing with channels
@author: jsaavedr
"""

import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import basic as  pai


filename = 'images/color/mm.jpg'
image=io .imread(filename)
    
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]
    
    
yellow = (1.2*red.astype(np.float32)*green.astype(np.float32)/255 - blue.astype(np.float32))
yellow = pai.toUINT8(yellow)
    

fig, xs = plt.subplots(1,2)
for i in range(2):
        xs[i].set_axis_off()
        
xs[0].imshow(image)
xs[0].set_title("Image")
xs[1].imshow(yellow, cmap="gray", vmin=0, vmax=255)
xs[1].set_title("Yellow")
    
