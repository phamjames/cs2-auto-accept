import customtkinter as ctk
from typing import Any, Callable

class AutoAcceptView(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry('300x100')

        self.title("CS2 AUTO ACCEPTOR")
        
        self.header = ctk.CTkLabel(master=self, text="Auto Accept", font=("Helvetica", 24))
        self.header.pack(pady=12, padx=10)

        self.switch = ctk.CTkSwitch(master=self)
        self.switch.pack()


    def bind_toggle_event(self, callback: Callable):
        self.switch.configure(command=callback)

    def configure_header_text(self, text, text_color=None):
        self.header.configure(text=text, text_color=text_color)

    def configure_toggle_text(self, text, text_color=None):
        self.switch.configure(text=text, text_color=text_color)

    
    