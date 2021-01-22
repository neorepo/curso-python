/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import static java.util.stream.Collectors.toList;

/**
 *
 * @author Julio Cesar
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        /*List<String> list = new ArrayList<>(Arrays.asList("Julio", "Ximena", "Romina"));

        int len = list.size();

        while (len-- > 0) {
            list.remove(0);
        }

        for (String name : list) {
            System.out.println(name);
        }*/
        // Ejercicio 2
        // Objeto de tipo Scanner para lectura de datos por consola o terminal
        Scanner leerEntrada = new Scanner(System.in);

        // Array de tipo String con nombres de clientes
        String[] nombresDeCliente = {"Alberto", "Juan", "Pablo", "Victoria", "Gabriela"};

        // Lista de tipo cliente, para almacenar los cinco clientes
        List<Cliente> clientes = new ArrayList<>();
        // Clientes totales
        int clientesTotales = nombresDeCliente.length;

        // Llenado de la lista de tipo cliente
        for (int i = 0; i < clientesTotales; i++) {
            // Agregar nuevo cliente a la lista
            clientes.add(new Cliente(nombresDeCliente[i]));
        }

        // Lectura datos de entrada
        System.out.println("Ingrese el nombre del cliente a buscar:");
        String nombreBuscado = leerEntrada.next();

        int idx = -1;

        // Iteramos la lista en busca del nombre
        for (int i = 0; i < clientesTotales; i++) {
            if (clientes.get(i).getNombre().equalsIgnoreCase(nombreBuscado)) {
                idx = i;
                break;
            }
        }

        if (idx != -1) {
            System.out.println("El objeto con nombre " + nombreBuscado
                    + " se encuentra en el índice " + idx);
        } else {
            System.out.println("El nombre que busca no se encuentra en la lista.");
        }

        // Ejemplo 2
        List<Cliente> lst = new ArrayList<>(Arrays.asList(
                new Cliente("Amadeo", "Masculino", 9),
                new Cliente("Julio", "Masculino", 39),
                new Cliente("Cecilia", "Femenino", 14),
                new Cliente("Celia", "Femenino", 45),
                new Cliente("Vanesa", "Femenino", 30),
                new Cliente("Aldana", "Femenino", 16)
        ));

        System.out.println(
                lst.stream()
                        .filter(cliente -> cliente.getEdad() < 18)
                        .map(Cliente::getNombre)
                        .map(String::toUpperCase)
                        .collect(toList()));

        //System.out.println(p2);
        //lst.forEach(System.out::println);
        lst.forEach(cliente -> {
            System.out.println(cliente);
        });

        //new Thread(() -> lst.forEach(System.out::println)).start();
        /*list.replaceAll(String::toUpperCase);
        new Thread(() -> list.forEach(System.out::println)).start();*/
        for (int i = 0; i++ < 5;) {
            System.out.println(
                    "Por favor, ingrese " + i + " elemento" + (i == 1 ? "" : "s")
            );
        }

        char lower = 'a';

        char upper = (char) (223 & lower);
        System.out.println("a => " + upper);

        for (int i = 0;
                i < 10;
                i = i + 1) {
            System.out.println("i: " + i);
        }

        int i = 0;

        while (i < 10) {
            System.out.println("i: " + i);
            i = i + 1;
        }

        System.out.println("Fuera del while: " + i);
    }

}
