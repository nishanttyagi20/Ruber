import cv2
import numpy as np

color = []
cubecolor = (0, 0, 0)
cubelineSize = 2

def drawCube(img, cubesize, cubeshape, start_point): 
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

cap = cv2.VideoCapture(1)
index = 1
while True:
    cubeImg = np.zeros((480, 640))
    res, cubeImg = cap.read()
    cv2.waitKey(10)
    drawCube(cubeImg, 180, 3, (100, 240))
    cv2.imshow("cube", cubeImg)
    if cv2.waitKey(1) == ord('c'):
        #index = index + 1
        print("start processing")
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
        cv2.imshow('1', img1)
        cv2.imshow('2', img2)
        cv2.imshow('3', img3)
        cv2.imshow('4', img4)
        cv2.imshow('5', img5)
        cv2.imshow('6', img6)
        cv2.imshow('7', img7)
        cv2.imshow('8', img8)
        cv2.imshow('9', img9)


        r, g, b = cv2.split(img1)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img2)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img3)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img4)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img5)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img6)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))


        r, g, b = cv2.split(img7)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))

        r, g, b = cv2.split(img8)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))

        r, g, b = cv2.split(img9)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        print(int(r_avg), int(g_avg), int(b_avg))

    if cv2.waitKey(10) == ord('q'):
        break