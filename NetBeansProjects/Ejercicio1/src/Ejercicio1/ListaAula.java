/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

import java.util.ArrayList;

/**
 *
 * @author Julio Cesar
 */
public class ListaAula {

    private static ArrayList<Aula> listadoAulas = new ArrayList<>();

    public static void agregarAula(Aula aula) {
        listadoAulas.add(aula);
    }

    public static ArrayList getAulas() {
        return listadoAulas;
    }
}
