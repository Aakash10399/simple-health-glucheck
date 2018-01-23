#!/usr/bin/python
import numpy as np
import cv2
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.widget import Widget
b_cfactor = 0.0722
g_cfactor = 0.7152
r_cfactor = 0.2126
b_0 = 0
g_0 = 0
r_0 = 0
img_0 = cv2.imread("0.jpg")
height,width,channels = img_0.shape
for i in range(0,height):
	for j in range(0,width):
		(b,g,r) = img_0[i,j]
		b_0 = b_0 + b
		g_0 = g_0 + g
		r_0 = r_0 + r
b_0 = b_0/(height*width)
g_0 = g_0/(height*width)
r_0 = r_0/(height*width)
#print b_0
#print g_0
#print r_0
#print "*************************"
b_100 = 0
g_100 = 0
r_100 = 0
img_100 = cv2.imread("100.jpg")
height,width,channels = img_100.shape
for i in range(0,height):
	for j in range(0,width):
		(b,g,r) = img_100[i,j]
		b_100 = b_100 + b
		g_100 = g_100 + g
		r_100 = r_100 + r
b_100 = b_100/(height*width)
g_100 = g_100/(height*width)
r_100 = r_100/(height*width)
#print b_100
#print g_100
#print r_100
#print "*************************"
b_300 = 0
g_300 = 0
r_300 = 0
img_300 = cv2.imread("300.jpg")
height,width,channels = img_300.shape
for i in range(0,height):
	for j in range(0,width):
		(b,g,r) = img_300[i,j]
		b_300 = b_300 + b
		g_300 = g_300 + g
		r_300 = r_300 + r
b_300 = b_300/(height*width)
g_300 = g_300/(height*width)
r_300 = r_300/(height*width)
#print b_300
#print g_300
#print r_300
#print "*************************"
b_1000 = 0
g_1000 = 0
r_1000 = 0
img_1000 = cv2.imread("1000.jpg")
height,width,channels = img_1000.shape
for i in range(0,height):
	for j in range(0,width):
		(b,g,r) = img_1000[i,j]
		b_1000 = b_1000 + b
		g_1000 = g_1000 + g
		r_1000 = r_1000 + r
b_1000 = b_1000/(height*width)
g_1000 = g_1000/(height*width)
r_1000 = r_1000/(height*width)
#print b_1000
#print g_1000
#print r_1000
#print "*************************"
b_3000 = 0
g_3000 = 0
r_3000 = 0
img_3000 = cv2.imread("3000.jpg")
height,width,channels = img_3000.shape
for i in range(0,height):
	for j in range(0,width):
		(b,g,r) = img_3000[i,j]
		b_3000 = b_3000 + b
		g_3000 = g_3000 + g
		r_3000 = r_3000 + r
b_3000 = b_3000/(height*width)
g_3000 = g_3000/(height*width)
r_3000 = r_3000/(height*width)
#print b_3000
#print g_3000
#print r_3000
#print "*************************"
cam = cv2.VideoCapture(0)
while True:
    if cam.grab():
        flag, frame = cam.retrieve()
        if not flag:
            continue
        else:
            cv2.imshow('INITIAL', frame)
            gray_counter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_counter2 = cv2.bitwise_not(cv2.Canny(gray_counter,100,200))
            ret,thresh = cv2.threshold(gray_counter2,127,255,1)
            _,contours,_ = cv2.findContours(thresh,1,2)
            if len(contours)==1:
            	captured_frame = frame
            	cv2.destroyAllWindows()
            	break
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
    	captured_frame = frame
    	cv2.destroyAllWindows()
    	break
#captured_frame = cv2.imread("test.jpg") #testing
canny = cv2.bitwise_not(cv2.Canny(captured_frame,100,200))
height,width = canny.shape
count = 0
centroid_x = 0
centroid_y = 0
for i in range(0,height):
	for j in range(0,width):
		if canny[i,j] == 0:
			count = count + 1
			centroid_x = centroid_x + i
			centroid_y = centroid_y + j
centroid_x = centroid_x / count
centroid_y = centroid_y / count
#print str(centroid_x) + " , " + str(centroid_y)
#print str(height) + " , " + str(width)
#cv2.imshow("Captured Frame",captured_frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
b_var,g_var,r_var = captured_frame[centroid_x,centroid_y]
#print str(r_var) + " , " + str(g_var) + " , " + str(b_var)
x0 = (b_cfactor*b_0)+(g_cfactor*g_0)+(r_cfactor*r_0)
y0 = 0
x1 = (b_cfactor*b_100)+(g_cfactor*g_100)+(r_cfactor*r_100)
y1 = 100
x2 = (b_cfactor*b_300)+(g_cfactor*g_300)+(r_cfactor*r_300)
y2 = 300
x3 = (b_cfactor*b_1000)+(g_cfactor*g_1000)+(r_cfactor*r_1000)
y3 = 1000
x4 = (b_cfactor*b_3000)+(g_cfactor*g_3000)+(r_cfactor*r_3000)
y4 = 3000
x_tofind = (b_cfactor*b_var)+(g_cfactor*g_var)+(r_cfactor*r_var)
term1 = (((x_tofind-x1)*(x_tofind-x2)*(x_tofind-x3)*(x_tofind-x4)*y0)/((x0-x1)*(x0-x2)*(x0-x3)*(x0-x4)))
term2 = (((x_tofind-x0)*(x_tofind-x2)*(x_tofind-x3)*(x_tofind-x4)*y1)/((x1-x0)*(x1-x2)*(x1-x3)*(x1-x4)))
term3 = (((x_tofind-x0)*(x_tofind-x1)*(x_tofind-x3)*(x_tofind-x4)*y2)/((x2-x0)*(x2-x1)*(x2-x3)*(x2-x4)))
term4 = (((x_tofind-x0)*(x_tofind-x1)*(x_tofind-x2)*(x_tofind-x4)*y3)/((x3-x0)*(x3-x1)*(x3-x2)*(x3-x4)))
term5 = (((x_tofind-x0)*(x_tofind-x1)*(x_tofind-x2)*(x_tofind-x3)*y4)/((x4-x0)*(x4-x1)*(x4-x2)*(x4-x3)))
y_tofind = term1 + term2 + term3 + term4 + term5
#print y_tofind
#app = tk.Tk()
#text1 = tk.Label(app,text="Glucose Test Level",font=("Helvetica", 16))
#text1.pack()
#text2 = tk.Label(app,text=str(y_tofind)+" mg/dL",font=("Helvetica", 16))
#text2.pack()
#app.minsize(500,80)
#app.geometry("500x80")
#app.mainloop()
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '80')
Config.write()
class Layout(Widget):
    def draw(self):
        with self.canvas:
        	Label(text="Glucose Test Level",font=("Helvetica", 16),pos=(200,0))
        	Label(text=str(y_tofind)+" mg/dL",font=("Helvetica", 16),pos=(200,-20))
class GlucoseLevel(App):
    def build(self):
    	app = Layout()
    	app.draw()
        return app
GlucoseLevel().run()
