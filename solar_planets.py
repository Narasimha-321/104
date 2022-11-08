import cv2
img=cv2.imread("solar-system.jpg")
txt="sun"
cv2.putText(img,
"Sun",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255))
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("imshow",gray_img)
cv2.waitKey(0)



