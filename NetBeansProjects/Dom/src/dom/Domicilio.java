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
public class Domicilio {

    private int idDomicilio;
    private String calle;
    private String numero;
    private String piso;
    private String departamento;
    private String barrio;
    private String manzana;
    private String casa;

    public Domicilio() {
    }

    public Domicilio(int idDomicilio, String calle, String numero, String piso, String departamento, String barrio, String manzana, String casa) {
        this.idDomicilio = idDomicilio;
        this.calle = calle;
        this.numero = numero;
        this.piso = piso;
        this.departamento = departamento;
        this.barrio = barrio;
        this.manzana = manzana;
        this.casa = casa;
    }

    public int getIdDomicilio() {
        return idDomicilio;
    }

    public void setIdDomicilio(int idDomicilio) {
        this.idDomicilio = idDomicilio;
    }

    public String getCalle() {
        return calle;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getPiso() {
        return piso;
    }

    public void setPiso(String piso) {
        this.piso = piso;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public String getBarrio() {
        return barrio;
    }

    public void setBarrio(String barrio) {
        this.barrio = barrio;
    }

    public String getManzana() {
        return manzana;
    }

    public void setManzana(String manzana) {
        this.manzana = manzana;
    }

    public String getCasa() {
        return casa;
    }

    public void setCasa(String casa) {
        this.casa = casa;
    }

    @Override
    public String toString() {
        return "idDomicilio: " + idDomicilio + ", calle: " + calle + ", numero: " + numero
                + ", piso: " + piso + ", departamento: " + departamento + ", barrio: " + barrio
                + ", manzana: " + manzana + ", casa: " + casa;
    }

}
