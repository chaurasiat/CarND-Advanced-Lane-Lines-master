import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import glob
import pickle

import os


img = mpimg.imread('test_images/test4.jpg')
image_shape = img.shape
print("image Shape",image_shape)
plt.imshow(img)
plt.show()
