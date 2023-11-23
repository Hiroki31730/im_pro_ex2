import cv2
import numpy as np

# グローバル変数
drawing = False  # マウスがクリックされているかどうか
start_x, start_y = 0, 0  # マウスがクリックされた座標

#短形波を描画する処理
def draw(event, x, y, flags, param):
    global start_x, start_y, drawing

    #ボタンが押された時の処理
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    #ボタンを離したときの処理
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (start_x, start_y), (x, y), (0, 255, 255))
        cv2.imshow('image', img)

# 画像の読み込み
img = cv2.imread('ex2_1.jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)


cv2.imshow('image', img)
cv2.waitKey(0)
    