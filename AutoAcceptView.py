import customtkinter as ctk
from typing import Any, Callable

class AutoAcceptView(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title = "CS2 AUTO ACCEPTOR"    
        self.geometry('300x150')
        
        self.header = ctk.CTkLabel(master=self, text="Auto Accept", font=("Helvetica", 24))
        self.header.pack(pady=12, padx=10)

        self.switch = ctk.CTkSwitch(master=self)
        self.switch.pack()


    def bind_toggle_event(self, callback: Callable):
        self.switch.configure(command=callback)

    def bind_toggle_text(self, text_var):
        self.switch.configure(text=text_var)

    def bind_text_color(self, text_color_var):
        self.switch.configure(text_color=text_color_var)
    
    