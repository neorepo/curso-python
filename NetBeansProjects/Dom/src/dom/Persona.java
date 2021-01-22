/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dom;

/**
 *
 * @author neo
 */
public class Persona {

    private int idPersona;
    private String apellido;
    private String nombre;
    private String edad;

    private Domicilio domicilio;

    public Persona() {
    }

    public Persona(int idPersona, String apellido, String nombre, String edad) {
        this.idPersona = idPersona;
        this.apellido = apellido;
        this.nombre = nombre;
        this.edad = edad;
    }

    public Persona(int idPersona, String apellido, String nombre, String edad, Domicilio domicilio) {
        this.idPersona = idPersona;
        this.apellido = apellido;
        this.nombre = nombre;
        this.edad = edad;
        this.domicilio = domicilio;
    }

    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }

    public Domicilio getDomicilio() {
        return domicilio;
    }

    public void setDomicilio(Domicilio domicilio) {
        this.domicilio = domicilio;
    }

    @Override
    public String toString() {
        return "idPersona: " + idPersona + ", apellido: " + apellido + ", nombre: " + nombre
                + ", edad: " + edad + ", domicilio: calle: " + domicilio.getCalle()
                + ", número: " + domicilio.getNumero() + ", piso: " + domicilio.getPiso()
                + ", departamento: " + domicilio.getDepartamento() + ", barrio: " + domicilio.getBarrio()
                + ", manzana: " + domicilio.getManzana() + ", casa: " + domicilio.getCasa();
    }

}
