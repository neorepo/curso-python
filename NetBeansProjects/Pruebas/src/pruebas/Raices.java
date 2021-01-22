/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pruebas;

/**
 *
 * @author neo
 */
public class Raices {

    // x = (-b +- √ b^2 - 4.a.c) / 2.a
    private double a;
    private double b;
    private double c;

    public Raices(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    // resultadoRaiz(): se imprimirá la única raíz, cuando tenga sólo una solución posible.
    private void resultadoRaiz() {
        // x = (-b +- √ b^2 - 4.a.c) / 2.a
        double x = -(b) / (2 * a);
        System.out.println("X: " + x);
    }

    //getDiscriminante(): retorna el valor del discriminante (double), la fórmula del discriminate es: b^2 - 4*a*c
    private double getDiscriminante() {
        // b^2 - 4.a.c
        return Math.pow(b, 2) - (4 * a * c);
    }

    private void resultadoRaices() {
        // x = (-b +- √ b^2 - 4.a.c) / 2.a
        double x1 = (-(b) + Math.pow(getDiscriminante(), .5)) / (2 * a); // La raíz cuadrada de x es lo mismo que x^0.5
        double x2 = (-(b) - Math.sqrt(getDiscriminante())) / (2 * a);
        System.out.println("X1: " + x1);
        System.out.println("X2: " + x2);
    }

    // hayRaices(): retorna si tiene dos soluciones con un booleano (si el discriminante es > 0)
    private boolean hayRaices() {
        return getDiscriminante() > 0; // hay dos raíces con números reales.
    }

    // hayRaiz(): retorna si tiene una única solución con un booleano (si el discriminante es = 0)
    private boolean hayRaiz() {
        return getDiscriminante() == 0; // solo hay una raíz para la ecuación.
    }

    // calculo(): imprimir las soluciones posibles de nuestra ecuación. También si no existe solución.
    public void calculo() {
        if (hayRaices()) {
            resultadoRaices();
        } else if (hayRaiz()) {
            resultadoRaiz();
        } else {
            // getDiscriminante() < 0 => No existe solución
            System.out.println("No hay una solución real.");
        }
    }

}
