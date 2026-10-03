class Chair:
    def __init__(self, id_chair, type_chair, color, available=True):
        self.id = id_chair
        self.type = type_chair
        self.color = color
        self.available = available

    def show_chair_info(self):
        status = "Disponible" if self.available else "Ocupada"
        return f"ID: {self.id}, Tipo: {self.type}, Color: {self.color}, Estado: {status}"
