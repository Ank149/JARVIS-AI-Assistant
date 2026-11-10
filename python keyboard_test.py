import pyautogui
import keyboard
import time

print("Testing keyboard in 5 seconds...")
time.sleep(5)

pyautogui.write("Hello Ankur", interval=0.1)
pyautogui.press("enter")

print("PyAutoGUI test completed")

keyboard.write("Jarvis Keyboard Working")