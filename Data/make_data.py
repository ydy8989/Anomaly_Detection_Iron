import numpy as np
import cv2


cap = cv2.VideoCapture(0)
count = 1

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # s1 = 'ano/o{}.jpg'.format(count)
    # count = count + 1
    # cv2.imwrite(s1, gray)
    # print(count)

    cv2.imshow('img', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()