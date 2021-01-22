/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Julio Cesar
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        // MODELO 1
        //
        // Objeto de tipo Scanner para lectura de datos por consola o terminal
        Scanner leerEntrada = new Scanner(System.in);

        // Lista de nombres de aulas
        ArrayList<String> nombreAula = new ArrayList<>();
        nombreAula.add("Azul");
        nombreAula.add("Verde");
        nombreAula.add("Amarillo");

        // Lista cantidad de bancos aula
        ArrayList<Integer> cantBancosAula = new ArrayList<>();
        cantBancosAula.add(40);
        cantBancosAula.add(35);
        cantBancosAula.add(30);

        // Lista de tipo Aula
        ArrayList<Aula> listaAulas = new ArrayList<>();

        // Iniciamos el llenado del ArrayList de tipo Aula
        listaAulas.add(new Aula(nombreAula.get(0), cantBancosAula.get(0)));
        listaAulas.add(new Aula(nombreAula.get(1), cantBancosAula.get(1)));
        listaAulas.add(new Aula(nombreAula.get(2), cantBancosAula.get(2)));

        // Índice inicial
        int idx = 0;

        int maximaCapacidadBancos = listaAulas.get(idx).getCantidadBancos();
        // Cantidad de elementos en la lista
        int M = listaAulas.size();

        // Busqueda del aula con mayor capacidad
        for (int i = 1; i < M; i++) {
            if (listaAulas.get(i).getCantidadBancos() > maximaCapacidadBancos) {
                maximaCapacidadBancos = listaAulas.get(i).getCantidadBancos();
                idx = i;
            }
        }

        // Lectura de datos
        System.out.println("ingrese la cantidad de alumnos inscriptos para cursar tercer grado:");
        int cantidadAlumnos = leerEntrada.nextInt();

        if (cantidadAlumnos <= maximaCapacidadBancos) {

            /**
             * Iniciamos la lectura de la lista de atrás para adelante, ya que
             * el último elemento es el que tiene menor cantidad de bancos.
             */
            for (int i = M; i > 0; i--) {
                if (cantidadAlumnos <= listaAulas.get(i - 1).getCantidadBancos()) {
                    System.out.println(
                            "EL aula " + listaAulas.get(i - 1).getNombreAula() + " es la indicada para la cantidad de alumnos.");
                    break;
                }
            }

        } else {
            System.out.println("La cantidad de alumnos debe ser menor o igual a " + maximaCapacidadBancos);
        }
    }
}
