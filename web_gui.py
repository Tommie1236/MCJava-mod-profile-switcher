import eel
import pyautogui 

width = pyautogui.size()[0]
height = pyautogui.size()[1]
SCREEN_SIZE = width, height

class Gui:

	def __init__(self):
		eel.init('web')
	
	def show(self, size):
		position = (SCREEN_SIZE[0] / 2 - size[0] / 2, SCREEN_SIZE[1] / 2 - size[1] / 2)
		eel.start('main.html', size=size, position=position)