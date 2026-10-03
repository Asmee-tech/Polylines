import cv2
import numpy as np

butterfly=cv2.imread("opencv-assets-main/butterflies.jpg")

hut=np.array([(30,100),(30,50),(55,20),(90,50),(90,100)],dtype=np.int32)
points=hut.reshape(-1,1,2)
poly=cv2.polylines(butterfly,[points],True,(255,0,0),1)
poly=cv2.fillPoly(poly,[points],(255,0,0))
cv2.imshow("window1",poly)
cv2.waitKey(0)