import pyautogui as pg

#X,Yの位置の取得
positionX, positionY = pg.position()

#現在のカーソルの位置を出力する
print('マウスの位置X:',positionX)
print('マウスの位置Y:',positionY)

