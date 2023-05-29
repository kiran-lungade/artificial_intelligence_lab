'''
		NAME:: LUNGADE KIRAN SANJAY
		TITLE:: IMAGE PROCESSING
'''
#Import required library
from PIL import Image

#Open Image
im = Image.open("Taj1.jpeg")
im.show()

#grayscale the image
im1 = Image.open("Taj1.jpeg").convert('L')
im1.show()

#rotate the grayscale image
#Image rotate & show
im1.rotate(45).show()

#convert the original .jpeg image to .png image
im.save('Taj1.png')

#thumbnail the original image
im.thumbnail ((300, 300))
im.show()

'''
#Import required library
import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('Taj1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


'''  

***************      OUTPUT        ****************

#Import required library
from PIL import Image

#Open Image
im = Image.open("Taj.jpg")
im.show()
im = Image.open("Taj.jpg").convert('L')
im.show()
#Image rotate & show
im.rotate(45).show()


'''
