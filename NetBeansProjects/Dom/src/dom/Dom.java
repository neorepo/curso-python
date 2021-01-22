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
public class Dom {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        String apellido = "Silva";
        String nombre = "Julio";
        String edad = "39";
        String calle = null;
        String numero = null;
        String piso = null;
        String departamento = null;
        String barrio = "El Progreso";
        String manzana = "B";
        String casa = "7";

        // Persona p1 = new Persona(1, apellido, nombre, edad, new Domicilio(1, calle, numero, piso, departamento, barrio, manzana, casa));
        Persona p2 = new Persona();
        p2.setIdPersona(1);
        p2.setApellido(apellido);
        p2.setNombre(nombre);
        p2.setEdad(edad);

        Domicilio d1 = new Domicilio();
        d1.setIdDomicilio(p2.getIdPersona());
        d1.setCalle(calle);
        d1.setNumero(numero);
        d1.setPiso(piso);
        d1.setDepartamento(departamento);
        d1.setBarrio(barrio);
        d1.setManzana(manzana);
        d1.setCasa(casa);

        p2.setDomicilio(d1);

        int age;

        do {
            age = Number.getInt("Ingrese su edad:");
            if (age == -1) {
                age = 0;
                break;
            }
        } while (18 > age);

        System.out.println("La edad ingresada es: " + age);
    }

}
