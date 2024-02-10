import cv2

img = cv2.imread("ImageSave/Photo Passport Size.jpg")

greyScaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image",img)

cv2.imshow("GreyScaled",greyScaled)

cv2.imwrite("./ImageSave/GreyScaledImage.jpg",greyScaled)

# cv2.waitKey(10000)
# cv2.destroyAllWindows()
