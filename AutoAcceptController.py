import asyncio
from AutoAcceptView import AutoAcceptView
from AutoAcceptModel import AutoAcceptModel

class AutoAcceptController:
    def __init__(self, model: AutoAcceptModel, view: AutoAcceptView):
        self.model = model
        self.view = view
        self._toggle_text_var = "OFF"
        self._text_color_var = "red"
        self.view.bind_toggle_event(self.toggle_event)
        self.view.bind_text_color(self.get_text_color_var())
        self.view.bind_toggle_text(self.get_toggle_text_var())


    def toggle_event(self):
        print("toggled")
        scanning = self.model.get_scanning_state()
        if not scanning:
            print("starting scan")
            self.model.run_scan()
            self._text_color_var = "green"
            self._toggle_text_var = "ON"
        else:
            print("stopping scan")
            self.model.stop_scan()
            self._text_color_var = "red"
            self._toggle_text_var = "OFF"
    
    def get_text_color_var(self):
        return self._text_color_var

    def get_toggle_text_var(self):
        return self._toggle_text_var
    
    def run(self):
        self.view.mainloop()

