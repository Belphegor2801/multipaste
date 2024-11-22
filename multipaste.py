import sys
import customtkinter

from pynput.keyboard import Key, Listener

import pyautogui
import pyperclip



class MultiPaste(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multipaste")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.init_constants()
        self.init_ctk_vars()

        self.build_widgets()
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # region init
    def init_constants(self):
        self.num_of_buttons = 9
        
        self.button_dictionary = {}
        for i in range(self.num_of_buttons):
            self.button_dictionary[i] = {
                "display": f"Ctrl + {i + 1}",
                "key": f"<{49 + i}>"
            }
            
        self.keys = [x["key"] for x in self.button_dictionary.values()] 
    
    def init_ctk_vars(self):
        self.text_vars = []
        for i in range(self.num_of_buttons):
            self.text_vars.append(customtkinter.StringVar())
            
    def _pass(self):
        pass
            
    # endregion
    
    # region build ui
    def build_widgets(self):
        for i in range(self.num_of_buttons):
            text_label = customtkinter.CTkButton(self, text=self.button_dictionary[i]["display"], width=50, command=self._pass)
            text_entry = customtkinter.CTkEntry(self, width=350, textvariable=self.text_vars[i])
            text_label.grid(row=i, column=0, padx=(10, 0), pady=5, sticky="e")
            text_entry.grid(row=i, column=1, padx=(10, 10), pady=5)

    # endregion
   
    # region utils
    def get_key_index(self, key):
        return self.keys.index(key)
    
    def on_release(self, key):
        key = str(key)
        if key in self.keys:
            text = self.text_vars[self.get_key_index(key)].get()
            pyperclip.copy(text)
            pyautogui.press("v")
    
    def on_closing(self):
        sys.exit()
    # endregion


main = MultiPaste()
listener = Listener(on_release=lambda event: main.on_release(event))
listener.start()
main.mainloop()
listener.join()