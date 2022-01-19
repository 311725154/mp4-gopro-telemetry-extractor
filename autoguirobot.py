import pyautogui as gui
import webbrowser

class Autoguirobot:
    """
    Imports: pyautogui
    automation upload module for website upload files if selenium fail
    """
    def __init__(self,app):

        self.browser = app
        gui.PAUSE = 3.0
        gui.FAILSAFE = True

    def start_chrome(self):


        # open the site
        webbrowser.open('https://goprotelemetryextractor.com/free')
        print(gui.size())
        print(gui.position())
        free_list = []
        try:
            while not free_list:
                confidance_val = 0.9
                x,y = gui.locateOnScreen('free1.png', grayscale=False, confidance=confidance_val)
                if gui.onScreen(x, y):
                    gui.click(x, y)
                confidance_val += 0.2


        except TypeError:
            print("exception type")
            for _ in range(8): gui.press('tab')


        gui.press('enter')


        try:
            x, y = gui.locateOnScreen('choose_file.png')
            print("x="+str(x)+" y="+str(y))
            gui.click(x, y)
        except TypeError:
            print('exception type 2')
            gui.moveTo(2902, 500)
            gui.click()
        #gui.press('enter')
        #gui.press('tab')
        # gui.press('enter')
        # gui.typewrite('https://goprotelemetryextractor.com/free')
        # gui.press('enter')
