"""Windows Automation Module"""
import os, time

WINDOWS = os.name == "nt"

class WindowsAutomation:
    def __init__(self):
        self.available = False
        if WINDOWS:
            try:
                import pyautogui
                import keyboard
                self.pyautogui = pyautogui
                self.keyboard = keyboard
                self.available = True
            except:
                pass
    
    def move_mouse(self, x, y):
        if not self.available:
            return "Install: pip install pyautogui"
        self.pyautogui.moveTo(x, y)
        return f"Moved to ({x}, {y})"
    
    def click(self, x=None, y=None):
        if not self.available:
            return "Install: pip install pyautogui"
        if x and y:
            self.pyautogui.click(x, y)
        else:
            self.pyautogui.click()
        return "Clicked"
    
    def screenshot(self, filename="screenshot.png"):
        if not self.available:
            return "Install: pip install pyautogui pillow"
        self.pyautogui.screenshot(filename)
        return f"Saved: {filename}"
    
    def wait(self, seconds):
        time.sleep(seconds)
        return f"Waited {seconds}s"
