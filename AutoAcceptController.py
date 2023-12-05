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
        self.view.configure_toggle_text(self.get_toggle_text_var(), self.get_text_color_var())
    
    def toggle_off(self):
        self.model.stop_scan()
        self.view.configure_toggle_text(self.get_toggle_text_var(), self.get_text_color_var())
        
    def toggle_on(self):
        self.model.run_scan()
        self.view.configure_toggle_text(self.get_toggle_text_var(), self.get_text_color_var())
        
    def toggle_event(self):
        scan_running = self.model.get_scanning_state()
        self.toggle_off() if scan_running else self.toggle_on()
    
    def get_text_color_var(self):
        scanning = self.model.get_scanning_state()
        return "green" if scanning else "red"

    def get_toggle_text_var(self):
        scanning = self.model.get_scanning_state()
        return "ON" if scanning else "OFF"
    
    def on_view_closing(self):
        self.view.configure_header_text("closing app...", "yellow")
        self.view.update()

        scan_running = self.model.get_scanning_state()
        if scan_running:
            self.model.stop_scan()
        
        self.view.quit()

    def run(self):
        self.view.protocol("WM_DELETE_WINDOW", self.on_view_closing)
        self.view.mainloop()

