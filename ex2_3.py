import cv2

#マウスがクリックされたときの処理を行う
def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


img = cv2.imread("ex2_1.jpg")
#画像の表示
cv2.imshow('sample', img)
#マウスがクリックされたときの処理の呼び出し
cv2.setMouseCallback('sample', onMouse)
cv2.waitKey(0)