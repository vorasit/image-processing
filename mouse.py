import cv2
import time
import autopy
import numpy as np;
import Hand_Tracking_Module as htm
frame,wcam,hcam,smooth,px,py,cx,cy,pt=100,640,480,2,0,0,0,0,0
cap=cv2.VideoCapture(0);cap.set(3,wcam),(4,hcam);detector=htm.handDetector(maxHands=1);
wScr,hScr=autopy.screen.size()
while True:
	success,img=cap.read();img=detector.findHands(img);p,box=detector.findPosition(img)
	if len(p)!=0:
		x1,y1=p[8][1:];x2,y2=p[12][1:];fingers=detector.fingerUp();cv2.rectangle(img,(frame,frame),(wcam-frame,hcam-frame),(255,0,255),2)
		if fingers[0]==0 & fingers[1]==1 & fingers[2]==0 & fingers[3]==0 & fingers[4]==0:
			x3=np.interp(x1,(frame,wcam-frame),(0,wScr));y3=np.interp(y1,(frame,hcam-frame),(0,hScr))
			#มันจะตรวจจับตำแหน่งที่นิ้วชี้มาแสดง
			#cx = px + (x3-px)/smooth;cy = py + (y3-py)/smooth
			autopy.mouse.move(wScr-x3,y3);cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
		if fingers[1]==1 & fingers[0]==1:
			length=detector.Distance(img,8,12);autopy.mouse.click()
			# if length<40:
			# 	cv2.circle(img,(x1,y1),15(0,255,0),cv2.FILLED)
	cTime=time.time();fps=1/(cTime-pt);pt=cTime;cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3);cv2.imshow("Image",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

