from ast import Break
from time import sleep
import pyautogui
import keyboard
import mouse



hotKeyForPrint = 's' #=> Use essa Key pra marcar coordenadas na tela.
hotKeyForMidButton = 'k' #=> Use essa Key pra clicar com o 'Mouse Middle Button' nas coordenadas marcadas com a tecla 'S'
hotKeyForLefButton = 'l' #=> Use essa Key pra clicar com o 'Mouse Left Button' nas coordenadas marcadas com a tecla 'L'
hotKeyForRigButton = 'r' #=> Use essa Key pra clicar com o 'Mouse Right Button' nas coordenadas marcadas com a tecla 'R'
# =================================================================================================================
# ========================================DIVIRTA-SE===============================================================
# =================================================================================================================
mapiation = []

while True:
    if keyboard.is_pressed(hotKeyForPrint):
        currentMX, currentMY = pyautogui.position()
        mapiation.append(currentMX)
        mapiation.append(currentMY)
        mapLenght = len(mapiation)
        print(mapiation)
        print(mapLenght)
        sleep(0.2)
    elif keyboard.is_pressed(hotKeyForMidButton):
        for point in range(0, mapLenght, 2):
            pyautogui.moveTo(mapiation[point], mapiation[point + 1])
            pyautogui.middleClick()
            sleep(0.4)
            break
    elif keyboard.is_pressed(hotKeyForLefButton):
        for point in range(0, mapLenght, 2):
            pyautogui.moveTo(mapiation[point], mapiation[point + 1])
            pyautogui.leftClick()
            sleep(0.4)
            break
    elif keyboard.is_pressed(hotKeyForRigButton):
        for point in range(0, mapLenght, 2):
            pyautogui.moveTo(mapiation[point], mapiation[point + 1])
            pyautogui.rightClick()
            sleep(0.4)
            break
    
        