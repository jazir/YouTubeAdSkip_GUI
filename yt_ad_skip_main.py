import cv2 as cv
import pyautogui
import numpy as np
import time
import threading
import PySimpleGUI as sg


def skip_ad():
    while True:
        time.sleep(3)
        print("Skip mode active")
        screen = pyautogui.screenshot()
        screen = cv.cvtColor(np.array(screen), cv.COLOR_BGR2GRAY)
        template = cv.imread('point.jpg', 0)
        w, h = template.shape[::-1]

        method = eval('cv.TM_CCOEFF_NORMED')
        res = cv.matchTemplate(screen, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        Threshold_val = 0.9
        if max_val > Threshold_val:
            clickX, clickY = max_loc[0] + 40, max_loc[1] + 10  # Correct for both screen
            pyautogui.moveTo(clickX, clickY, duration=0.1)
            pyautogui.click()


def main():
    layout1 = [[sg.Text("Click Skip Ad to automate ad skipping")],
               [sg.Button("Skip Ad")]]
    layout2 = [[sg.Text("Ad skip is active. Click Stop to stop execution and exit")],
               [sg.Button("Stop")]]
    # margins = (100, 500)
    # Create the window
    window1 = sg.Window("Auto Youtube Ad Skip", layout1)
    window2 = sg.Window("Auto Youtube Ad Skip", layout2)

    while True:
        event, values = window1.read()
        # End program if user closes window or presses the Stop button
        if event in (sg.WIN_CLOSED, "Exit", None):
            break

        elif event == "Skip Ad":
            threading.Thread(target=skip_ad, daemon=True).start()
            window1.close()
            window2.read()

    window2.close()


if __name__ == '__main__':
    main()
