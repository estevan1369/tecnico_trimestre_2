class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Pedido:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.total = cantidad * producto.precio

# Datos por teclado
nombre = input("Nombre del cliente: ")
email = input("Email: ")
c1 = Cliente(nombre, email)

prod = input("Nombre del producto: ")
precio = float(input("Precio: "))
p1 = Producto(prod, precio)

cant = int(input("Cantidad: "))
pedido1 = Pedido(c1, p1, cant)

# Mostrar resultado con f-strings
print(f"\nCliente: {c1.nombre} - {c1.email}")
print(f"Producto: {p1.nombre} - Precio: {p1.precio}")
print(f"Pedido total: {pedido1.total}")