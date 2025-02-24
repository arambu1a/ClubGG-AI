import pyautogui
import time

x, y = 500, 500  # Set your desired coordinates

while True:
    pyautogui.click(x, y)  # Click at (x, y)
    time.sleep(0.1)  # Add a small delay to prevent excessive CPU usage
