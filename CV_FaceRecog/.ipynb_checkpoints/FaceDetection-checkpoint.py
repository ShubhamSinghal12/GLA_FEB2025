import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


while True:
    
    ret,frame = cap.read()
    
    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame,1.3,5) #Frame, Scaling Factors, Neighbours

    # cv2.imshow("Gray Video",gray_frame)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #image, start co-ordinates, end co-ordinates, color, thickness
    
    cv2.imshow("Video Capture",frame)

    key_pressed = cv2.waitKey(1)
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()