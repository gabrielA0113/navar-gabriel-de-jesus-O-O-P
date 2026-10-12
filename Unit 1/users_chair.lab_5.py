class chair:
    def __init__(self, color, type_chair, material):
        self.color = color
        self.type_chair = type_chair
        self.material = material
    def show_chair_info(self):
        return f"Chair Color: {self.color}, Chair Type: {self.type_chair}, Chair Material: {self.material}"
