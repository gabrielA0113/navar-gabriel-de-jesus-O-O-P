
class User:
    def __init__(self, username, password, profile):
        self.username = username
        self.password = password
        self.profile = profile

    def update_profile(self, new_profile_text):
        self.profile = new_profile_text
        print(f"[{self.username}] Perfil actualizado a: '{self.profile}'")

    def create_post(self, text):
        print(f"[{self.username}] Publicación creada: '{text}'")

    def create_comment(self, text, post):
        print(f"[{self.username}] Comentario creado en la publicación de {post.author.username}: '{text}'")

    def send_message(self, text, receiver):
        print(f"[{self.username}] Mensaje enviado a {receiver.username}: '{text}'")


class Post:
    def __init__(self, post_id, author: User, content):
        self.post_id = post_id
        self.author = author
        self.content = content
        self.likes = 0

    def like(self, user: User):
        self.likes += 1
        print(f"A {user.username} le gustó la publicación de {self.author.username}. Total likes: {self.likes}")


class Comment:
    def __init__(self, comment_id, post: Post, author: User, text):
        self.comment_id = comment_id
        self.post = post
        self.author = author
        self.text = text

    def edit_text(self, new_text):
        self.text = new_text
        print(f"Comentario {self.comment_id} editado por {self.author.username}: '{self.text}'")


class Message:
    def __init__(self, message_id, sender: User, receiver: User, content):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print(f"Mensaje de {self.sender.username} para {self.receiver.username} marcado como LEÍDO.")


class Student:
    def __init__(self, name):
        self.name = name

    def enroll(self, course):
        self.course = course

    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")


class Course:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Course: {self.name}")


# Instances
student = Student("Carlos")
course = Course("Python Programming")

# Creating a relationship
student.enroll(course)

# Use the Relationship
student.show_course()
        