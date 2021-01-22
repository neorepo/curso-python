/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dom;

import javax.swing.JOptionPane;

/**
 *
 * @author neo
 */
public class Number {

    private static final String CONSTANTE;

    static {
        CONSTANTE = "Soy una constante";
    }

    public static int getInt(String message) {
        int n = 0;
        String str = JOptionPane.showInputDialog(message);
        if (str == null) {
            return -1;
        }
        if (str.matches("^[+-]?\\d+$")) {
            try {
                n = Integer.parseInt(str);
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null,
                        "No ingrese valores mayores a 2147483647 o menores a -2147483648.");
            }
        }
        return n;
    }
}
