from chairs import chair
from users import user
from library import library


chair1 = chair("001", "Ergonomica", "Negro")
chair2 = chair("002", "Ejecutiva", "Azul")

r
user1 = user("001", "Gabriel Navar")

library1 = library()


library1.add_chair(chair1)
library1.add_chair(chair2)

library1.add_users(user1)


library1.show_chairs()
library1.show_users()