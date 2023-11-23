import cv2

#画像の読み込み
img = cv2.imread("ex2_1.jpg")

#高さと幅を測定し、変数に保存
height, width = img.shape[:2]

#出力
print(height)
print(width)
cv2.imshow('sample', img)
cv2.waitKey(0)