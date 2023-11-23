import cv2

#任意の画像の読み込み
img =cv2.imread("ex2_1.jpg")

#画像の表示
cv2.imshow("Image", img)

#画像がキー入力されるまで表示する
cv2.waitKey(0)