import pyautogui
import random
import string

x, y= pyautogui.position()
print(x)
print(y)

letters = string.ascii_lowercase
first_name = ''.join(random.choice(letters) for i in range(10))
print(type(first_name))

x, y = pyautogui.size()
print(x)
print(y)
