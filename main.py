import cv2
import numpy as np
from PIL import Image
# from matplotlib import pyplot as plt


# reading image
img = cv2.imread(r'C:\Users\RobotComp.ru\PycharmProjects\olympTask\image.png')

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:

    # here we are ignoring first counter because
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue

    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    # using drawContours() function
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

if __name__ == '__main__':
    # displaying the image after drawing contours

    # create a model of shapes
    # gets color bounds of red circle
    lower =(0, 0, 255) # lower bound for each channel
    upper = (0, 0, 255) # upper bound for each channel

    # create the mask
    mask = cv2.inRange(img, lower, upper)

    coords = np.argwhere(mask == 255)
    print(coords)

    # Loop through the contours and calculate the area of each object
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Draw a bounding box around each object and display the area on the image
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, str(area), (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # create new image
    # # open the original image
    # original_img = Image.open(r"C:\Users\RobotComp.ru\PycharmProjects\olympTask\image.png")
    #
    # # Flip the original image vertically
    # vertical_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
    # vertical_img.save("new_image.png")
    #
    # # close all our files object
    # original_img.close()
    # vertical_img.close()
