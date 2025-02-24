import pyautogui
import time

time.sleep(2)

while True: # Take an empty seat
    takeSeat = pyautogui.locateOnScreen('seat1.png', confidence = 0.75)
    if takeSeat:
        button_center = pyautogui.center(takeSeat)
        print(f"Clicking at: {button_center}")  # Print the click location just in case not working 

        pyautogui.doubleClick(button_center)
        break

time.sleep(2)
while True: # Confirm VPIP/GPS
    confirming = pyautogui.locateOnScreen('confirmseat.png', confidence = 0.75)
    if confirming:
        button_confirm = pyautogui.center(confirming)
        pyautogui.doubleClick(button_confirm)
        break

time.sleep(2)
while True: #Confirm buy in (minimum)
    buyin = pyautogui.locateOnScreen('buyin.png', confidence = 0.75)
    if buyin:
        button_buyin = pyautogui.center(buyin)
        pyautogui.doubleClick(button_buyin)
        break

time.sleep(2)


