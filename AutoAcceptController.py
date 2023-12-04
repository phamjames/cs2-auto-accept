import asyncio
from customtkinter import StringVar
from AutoAcceptView import AutoAcceptView
from AutoAcceptModel import AutoAcceptModel

class AutoAcceptController:
    def __init__(self, model: AutoAcceptModel, view: AutoAcceptView):
        self.model = model
        self.view = view
        self._toggle_text_var = StringVar(self.view, "OFF")
        self._text_color_var = "red"
        self.view.bind_toggle_event(self.toggle_event)
        self.view.configure_text_color(self.get_text_color_var())
        self.view.configure_toggle_text(self.get_toggle_text_var())


    def toggle_event(self):
        print("toggled")
        scanning = self.model.get_scanning_state()
        if not scanning:
            print("starting scan")
            self.model.run_scan()
            self.view.configure_text_color(self.get_text_color_var())
            self.view.configure_toggle_text(self.get_toggle_text_var())
        else:
            print("stopping scan")
            self.model.stop_scan()
            self.view.configure_text_color(self.get_text_color_var())
            self.view.configure_toggle_text(self.get_toggle_text_var())

    def get_text_color_var(self):
        scanning = self.model.get_scanning_state()
        return "green" if scanning else "red"

    def get_toggle_text_var(self):
        scanning = self.model.get_scanning_state()
        return "ON" if scanning else "OFF"
    
    def run(self):
        self.view.mainloop()

