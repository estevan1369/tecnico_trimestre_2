import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Datos cliente
        System.out.print("Nombre del cliente: ");
        String nombreCliente = sc.nextLine();
        System.out.print("Email: ");
        String email = sc.nextLine();

        // Datos producto
        System.out.print("Nombre del producto: ");
        String nombreProducto = sc.nextLine();
        System.out.print("Precio: ");
        double precio = sc.nextDouble();

        // Pedido
        System.out.print("Cantidad: ");
        int cantidad = sc.nextInt();
        double total = cantidad * precio;

        // Resultado
        System.out.println("\nCliente: " + nombreCliente + " - " + email);
        System.out.println("Producto: " + nombreProducto + " - " + precio);
        System.out.println("Pedido total: " + total);

        sc.close();
    }
}