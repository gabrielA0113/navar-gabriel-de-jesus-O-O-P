class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


#Clases hijas

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, "electronico")


class ProductoRopa(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, "ropa")


class ProductoAlimento(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, "alimento")


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0

        for producto in self.productos:

            if producto.tipo == "electronico":
                total += producto.precio * 1.16

            elif producto.tipo == "ropa":
                total += producto.precio * 1.08

            elif producto.tipo == "alimento":
                total += producto.precio * 1.00

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")

        print("\nProductos:")

        for producto in self.productos:
            print(
                f"- {producto.nombre}: "
                f"${producto.precio:.2f}"
            )

        print(f"\nTotal: ${self.calcular_total():.2f}")


# main program

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    ProductoElectronico("Laptop", 15000)
)

pedido.agregar_producto(
    ProductoRopa("Playera", 500)
)

pedido.agregar_producto(
    ProductoAlimento("Cereal", 100)
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)