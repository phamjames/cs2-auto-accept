import asyncio
import customtkinter
from AutoAcceptController import AutoAcceptController

from AutoAcceptModel import AutoAcceptModel
from AutoAcceptView import AutoAcceptView

def main():
    # model
    model = AutoAcceptModel()
    # view 
    view = AutoAcceptView()
    # controller
    controller = AutoAcceptController(model, view)
    controller.run()
        
if __name__ == "__main__":
    main()
