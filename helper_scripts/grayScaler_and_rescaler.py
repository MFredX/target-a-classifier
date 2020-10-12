import cv2
import numpy as np 
import os
import sys

### This script grey scales and rescales the images mentioned in the arguments
### argv[1] source file with images to be processed
### argv[2] destination file with processed images

def grey_scaler(inputImage):
    #original = cv2.imread(inputImage)
    gray = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
    return gray

def rescaler(inputImage):
    #Images resized to (720,480) (w,h) due to these being the size of Pi camera images
    #Also to preserve image data
    resized = cv2.resize(inputImage, (150,100)) #Resize dimensions here
    return resized

def main():
    source_path=sys.argv[1]
    dest_path=sys.argv[2]
    for img in os.listdir(sys.argv[1]):
        print("Processing "+img)
        image_read = cv2.imread(source_path+img)
        rescaled_image=rescaler(image_read)
        greyscaled_image=grey_scaler(rescaled_image)
        name =img + 'grey_&_resized'
        cv2.imwrite(os.path.join(dest_path,name +'.jpg'), greyscaled_image)
        
main()