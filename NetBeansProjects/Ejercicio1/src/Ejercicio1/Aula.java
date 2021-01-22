/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

/**
 *
 * @author Julio Cesar
 */
public class Aula {

    private String nombreAula;
    private int cantidadBancos;
    private int cantidadAlumnos;

    public Aula() {
    }

    public Aula(String nombreAula, int cantidadBancos) {
        this.nombreAula = nombreAula;
        this.cantidadBancos = cantidadBancos;
    }

    public String getNombreAula() {
        return nombreAula;
    }

    public void setNombreAula(String nombreAula) {
        this.nombreAula = nombreAula;
    }

    public int getCantidadBancos() {
        return cantidadBancos;
    }

    public void setCantidadBancos(int cantidadBancos) {
        this.cantidadBancos = cantidadBancos;
    }

    public int getCantidadAlumnos() {
        return cantidadAlumnos;
    }

    public void setCantidadAlumnos(int cantidadAlumnos) {
        this.cantidadAlumnos = cantidadAlumnos;
    }

    @Override
    public String toString() {
        return "Identificador Aula: " + nombreAula + ", Cantidad de Bancos: " + cantidadBancos;
    }

}
