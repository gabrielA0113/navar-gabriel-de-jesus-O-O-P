class Chair:
    def __init__(self, chair_id, material, color):
        self.chair_id = chair_id
        self.material = material
        self.color = color

    def show_chair_info(self):
        return f"Silla ID: {self.chair_id} | Material: {self.material} | Color: {self.color}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.chairs = []  

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def add_chair(self, chair):
        self.chairs.append(chair)  

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())

    def show_chairs(self):
        for chair in self.chairs:  
            print(chair.show_chair_info())