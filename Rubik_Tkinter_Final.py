import cv2      #opencv-python
import numpy as np  
import kociemba     #the rubix cube library
from tkinter import *


color = []      
cubecolor = (0, 0, 0)
cubelineSize = 2


def getcolor(r, g, b):      #function to specify the range of the r, g, b
    if (r >= 100 and r <= 160) and (g >= 25 and g <= 60) and (b >= 5 and b <= 45):
        return 'R'
    elif (r >= 140 and r <= 190) and (g >= 130 and g <= 180) and (b >= 120 and b <= 180):
        return 'B'
    elif (r >= 40 and r <= 80) and (g >= 140 and g <= 200) and (b >= 107 and b <= 200):
        return 'F'
    elif (r > 0 and r <= 40) and (g >= 80 and g <= 130) and (b > 140 and b < 200):
        return 'D'
    elif (r >= 0 and r <= 60) and (g >= 25 and g <= 55) and (b >= 135 and b < 200):
        return 'U'
    elif (r >= 63 and r <= 100) and (g >= 125 and g <= 170) and (b > 12 and b <= 90):
        return 'L'
    else:
        pass


def drawCube(img, cubesize, cubeshape, start_point):        #function to draw the On-Screen Cube
    cubecell = int(cubesize / cubeshape)
    
    for i in range(cubeshape + 1):
        start_line = (start_point[0], start_point[1] + i * cubecell)
        end_line = (start_point[0] + cubesize, start_point[1] + i * cubecell)
        cv2.line(img, start_line, end_line, cubecolor, 2)
    
    for i in range(cubeshape + 1):
        start_line = (start_point[0] + i * cubecell, start_point[1])
        end_line = (start_point[0] + i * cubecell, start_point[1] + cubesize)
        cv2.line(img, start_line, end_line, cubecolor, cubelineSize)

    return img


def showlabel(img, index):
    if index == 1:
        cv2.putText(cubeImg, "Show Upper Face", (int(17), 30),     #Show Upper Face     #red
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    elif index == 2:
        cv2.putText(cubeImg, "Show Right Face", (int(17), 30),    #Show Right Face    #blue
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    elif index == 3:
        cv2.putText(cubeImg, "Show Front Face", (int(17), 30),   #Show Front Face   #yellow
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    elif index == 4:
        cv2.putText(cubeImg, "Show Down Face", (int(17), 30),      #Show Down Face     #orange
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    elif index == 5:
        cv2.putText(cubeImg, "Show Left Face", (int(17), 30),       #Show Left Face     #green
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    elif index == 6:
        cv2.putText(cubeImg, "Show Back Face", (int(17), 30),       #Show Back Face     #white
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        cv2.imshow("cube", cubeImg)
    else:
        pass


cap = cv2.VideoCapture(0)           #open cv webcam
index = 1
while True:     #loop to get the camera running
    cubeImg = np.zeros((480, 640))
    res, cubeImg = cap.read()
    cv2.waitKey(10)
    drawCube(cubeImg, 180, 3, (100, 240))       #drawCube function
    cv2.imshow("cube", cubeImg)
    showlabel(cubeImg, index)       #showlabel function
    if cv2.waitKey(10) == ord('c'):  #key c to capture image in the cube on camera
        index = index + 1
        print("start processing")
        showlabel(cubeImg, index)
        img = cubeImg.copy()
        img1 = img[240:300, 100:160]
        img2 = img[240:300, 160:220]
        img3 = img[240:300, 220:280]
        img4 = img[300:360, 100:160]
        img5 = img[300:360, 160:220]
        img6 = img[300:360, 220:280]
        img7 = img[360:420, 100:160]
        img8 = img[360:420, 160:220]
        img9 = img[360:420, 220:280]
        pixel = [img1, img2, img3, img4, img5, img6, img7, img8, img9]

        for i in pixel:                            #Extracting RGB Values 
            r, g, b = cv2.split(i)
            r_avg = cv2.mean(r)[0]
            g_avg = cv2.mean(g)[0]
            b_avg = cv2.mean(b)[0]
            print(int(r_avg), int(g_avg), int(b_avg))
            res = getcolor(int(r_avg), int(g_avg), int(b_avg))
            color.append(res)

        print(color)
    if cv2.waitKey(9) == ord('s'):              #s key will start the solving of cube
        que = ''.join(color)
        print(que)
        print(kociemba.solve(que))

        root = Tk()
        root.title('RUBÉR')
        root.geometry("690x420")

        w = Label(root, text='Steps to solve the Cube', font=("Times New Roman", 45), bd=10)
        
        w.pack()
        soln = kociemba.solve(que)
        msg = Message(root, text=soln, pady=90, font=("Times New Roman", 15))
        
        msg.pack()
        
        ex = Button(root, text="Finish", command=root.destroy, activebackground='red',  height=2, width=20)
        ex.place(x=265, y=370)
        
        root.mainloop()
        break
        #break
    if cv2.waitKey(10) == ord('q'):             #q key will end the program
        break