import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Smartphone(SmartDevice):
    def __init__(self, name="Phone Smart Device"):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} is turned on"

    def turn_off(self):
        return f"{self.name} is turned off"

    class SmartTV(SmartDevice):
        def __init__(self, name="Samsung Smart TV"):
            super().__init__(name)

    def turn_on(self):
        return f"{self.name} is turned on"

    def turn_off(self):
        return f"{self.name} is turned off"

class SmartLight(SmartDevice):
    def __init__(self, name="Living Room Smart Light"):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} set the brightness to 100%"

    def turn_off(self):
        return f"{self.name} turned off"


class SmartSpeaker(SmartDevice):
    def __init__(self, name="Alexa Smart Speaker"):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} is playing music"

    def turn_off(self):
        return f"{self.name} is turned off"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Home App")
        self.geometry("650x700")
        self.resizable(False, False)

        self.devices = {
            "Light": SmartLight(),
            "Speaker": SmartSpeaker(),
        }

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self,
            text="Smart Home Center",
            font=("Arial", 16, "bold"),
            fg="#039be5"
        )
        title.pack(pady=20)

        self.device_var = tk.StringVar(value="Light")

        group_box = tk.LabelFrame(
            self,
            text="Select device",
            padx=12,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        for device_name in self.devices:
            ttk.Radiobutton(
                group_box,
                text=device_name,
                value=device_name,
                variable=self.device_var
            ).pack(anchor="w", pady=3)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Turn On", command=lambda: self.show_result("on"), width=12).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Turn Off", command=lambda: self.show_result("off"), width=12).grid(row=0, column=1, padx=10)

        self.output = tk.Label(
            self,
            text="Choose a device and click a button.",
            bg="#ecf0f1",
            fg="#a31a3f",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.output.pack(fill="x", padx=20, pady=5)

    def show_result(self, action):
        selected_name = self.device_var.get()
        device = self.devices[selected_name]

        if action == "on":
            result = device.turn_on()
        else:
            result = device.turn_off()

        self.output.config(text=result)


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
      