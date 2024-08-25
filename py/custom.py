import numpy as np
import cv2

def create_custom_image():
   
    # Define the size of the image (height, width, channels) and  Create an empty image with three channels (RGB), initialized to zero (black)
    image = np.zeros((512, 512,3) , dtype=np.uint8)

    #Draw a red rectangle
    cv2.rectangle(image, (100,100), (400,400),(0,0,255),-1)

    #Draw a blue Circle
    cv2.circle(image, (256,256), 50, (2555,0,0),-1)

    #Draw a Green Line
    cv2.line(image, (0,0), (512,512),(0,255,0),5)


    # Display the image
    cv2.imshow('Custom Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the image to a file
    cv2.imwrite('custom_image.png', image)

# Run the function
create_custom_image()
