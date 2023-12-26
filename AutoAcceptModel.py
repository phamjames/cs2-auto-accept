import time
import cv2
import numpy as np
import pyautogui
import math
import pytesseract
import pygetwindow
from StoppableThread import StoppableThread

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class AutoAcceptModel():
    def __init__(self):
        self._scanning = False
        self._scan_task = None
        self._cs2_window = None
        self._cs2_res = None
        self._cs2_w = None
        self._cs2_h = None
        self._keywords = ["your","match","is","ready","accept"]

    def _set_cs2_resolution(self):  
        self._cs2_window = pygetwindow.getWindowsWithTitle('Counter-Strike 2')[0]
        self._cs2_window.restore()
        self._cs2_res = (self._cs2_window.width, self._cs2_window.height)
        self._cs2_w = self._cs2_res[0]
        self._cs2_h = self._cs2_res[1]

    def _set_scanning_state(self, is_scanning: bool):
        self._scanning = is_scanning

    def get_scanning_state(self):
        return self._scanning

    def _set_scan_task(self, task):
        self._scan_task = task

    def _get_scan_task(self) -> StoppableThread:
        return self._scan_task
    
    def _get_match_ready_region(self) -> tuple[int, int, int, int]:
        return (self._cs2_w//4, self._cs2_h//4, self._cs2_w//2, self._cs2_h//4)
    
    def _get_accept_button_pos(self) -> tuple[int, int]:
        return (self._cs2_w // 2, math.ceil(self._cs2_h // 2.5))

    def _click_accept(self) -> bool:
        pyautogui.moveTo(self._get_accept_button_pos(), duration=.5)
        pyautogui.doubleClick()
        scanned_text = self._scan_for_text(self._get_match_ready_region())
        return 'players' in scanned_text

    def _scan_for_text(self, region) -> str:
        img = np.array(pyautogui.screenshot(region=region))
        cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
        img = cv2.normalize(img, cv2norm_img, 0, 255, cv2.NORM_MINMAX)
        img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
        img = cv2.GaussianBlur(img, (1, 1), 0)
        text = pytesseract.image_to_string(img).lower()
        return text
    
    def _is_match_ready(self, text) -> bool:
        for keyword in self._keywords:
                if keyword in text:
                    return True
        return False

    def _scan_for_match_ready(self):
        
        while self.get_scanning_state():
            scanned_text = self._scan_for_text(self._get_match_ready_region())
            print("-----------scanned text start-------------")
            print(scanned_text)
            print("------------scanned text end--------------\n")

        
            if self._is_match_ready(scanned_text):
                print("clicking accept")
                self._click_accept()

            time.sleep(6) # arbitrary number

    def run_scan(self):
        self._set_cs2_resolution()
        print("Your CS2 Resolution is ---> ",self._cs2_res)
        print('')
        self._set_scan_task(StoppableThread(target= self._scan_for_match_ready))
        self._set_scanning_state(is_scanning = True)
        self._get_scan_task().start()
        
    def stop_scan(self):
        self._get_scan_task().stop()
        self._set_scanning_state(is_scanning = False)







    
        

              
            


                



    
        
    



   