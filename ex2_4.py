import cv2
import numpy as np

#マウスがクリックされたときの処理
def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[x, y])

#画像読み込みと表示
img = cv2.imread("ex2_1.jpg")
cv2.imshow('sample', img)

#マウスがクリックされた時の処理の呼び出し
cv2.setMouseCallback('sample', onMouse)
cv2.waitKey(0)
