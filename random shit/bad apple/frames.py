import tkinter as tk
import pyautogui

class Manager:
        
    def BitMaker(sizex, sizey, posx, posy):
        window = tk.Tk()
        window.geometry(f"{sizex}x{sizey}+{posx}+{posy}")
        
        return window
    
    def FrameIt():
        return tk.mainloop()
        
    def DestroyBit(*bits):
        for bit in bits:
            bit.height