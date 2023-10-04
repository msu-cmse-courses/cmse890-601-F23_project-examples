#!/usr/bin/env python
# coding: utf-8

# This example is adapted from a lesson written by
# Dirk Colbry, Michigan State University

import os
import numpy as np
import scipy.ndimage as ndimage
from PIL import Image

input_folder = "coil-100"
output_folder = "segmented"

# make folder if doesn't exist
os.makedirs(output_folder, exist_ok=True)

for obj in range(1, 100): # 0, 100
    for angle in range(0,360,5):

        with Image.open(f"{input_folder}/obj{obj}__{angle}.png") as img:
            im = np.array(img.convert("RGBA")) # add transparency for testing

        # Use Logical operators for each RGB Color channel
        # Roughly selects pixels that are not part of black background
        r_threshold = im[:,:,0] > 40
        g_threshold = im[:,:,1] > 40
        b_threshold = im[:,:,2] > 40

        # Use logical_and to combine results of each channel
        binary_image = np.logical_and(r_threshold,g_threshold)
        binary_image = np.logical_and(binary_image,b_threshold)
        mask = ndimage.binary_closing(binary_image, iterations=4)

        im2 = im.copy()
        im2[~mask,3] = 0 # set alpha (transparency) channel to 0

        Image.fromarray(im2).save(f"{output_folder}/segmented_obj{obj}__{angle}.png")


