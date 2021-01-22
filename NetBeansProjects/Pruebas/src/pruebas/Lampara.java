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
public class Lampara {

    /**
     * off or on
     */
    private String status;

    public Lampara() {
        status = "Off";
    }

    public String getStatus() {
        return status;
    }

    public Lampara setStatus(String status) {
        this.status = status;
        return this;
    }
}
