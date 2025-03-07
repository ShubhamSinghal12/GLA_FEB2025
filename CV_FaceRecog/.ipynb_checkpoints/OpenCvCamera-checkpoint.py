import cv2


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret == False:
        continue
        
    cv2.imshow('Pic',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()










# img = cv2.imread("./dog.png")
# new_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)

# # new_img = img[:,:,::-1]
# new_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# # gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)


# cv2.imshow('Dog Image',new_img)
# cv2.imshow('Gray Dog Image',gray)

# cv2.waitKey(0) # Program will stop when any key is pressed
# cv2.destroyAllWindows()




