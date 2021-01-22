/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pruebas;

import java.util.Calendar;

/**
 *
 * @author neo
 */
public class Main {
//https://docs.oracle.com/javase/tutorial/collections/interfaces/list.html

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        Calendar objCalendar = Calendar.getInstance();

        String[] meses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
        String[] dias = {"Domingo", "Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado"};

        System.out.println(meses[objCalendar.get(Calendar.MONTH)]);
        System.out.println(dias[objCalendar.get(Calendar.DAY_OF_WEEK)]);
        System.out.println(objCalendar.get(Calendar.DAY_OF_MONTH));
        System.out.println(objCalendar.getTime());

        String s = "Hay un lugar más allá del tiempo, donde existe un mundo mejor.";

        // Lampara L1 = (new Lampara()).setStatus("On");
        // System.out.println("La lampara L1 esta en: " + L1.getStatus());
        Libro L1 = new Libro("9780672337840", "Introduction to Programming in Java", "Robert Sedgewick", 784);
        Libro L2 = new Libro("0134076435", "Introduction to Programming in Python", " Kevin Wayne", 792);

        if (L1.getNumPaginas() > L2.getNumPaginas()) {
            System.out.println("El libro: " + L1.getTitulo() + " contiene un mayor número de páginas.");
        } else {
            System.out.println("El libro: " + L2.getTitulo() + " contiene un mayor número de páginas.");
        }

        Raices r1 = new Raices(-1, -7, -6);
        Raices r2 = new Raices(1, 4, 4);

        r1.calculo();
        r2.calculo();

        DateTime dt = new DateTime();
        System.out.println(dt.getComponentDateTime());
    }
}
