/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pruebas;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Month;
import java.time.ZoneId;
import java.time.ZonedDateTime;

/**
 *
 * @author neo
 */
public class DateTime {
    // https://www.youtube.com/watch?v=OIg9lNpMJew&list=PLX8CzqL3ArzVzEnBoxNsq4uwyPT5o1TKZ&index=8

    public LocalDate getJuliosBirthday() {
        return LocalDate.of(1981, Month.MARCH, 3);
    }

    public LocalTime getSampleLocalTime() {
        return LocalTime.of(22, 36);
    }

    public LocalDateTime getSampleLocalDateTime() {
        return LocalDateTime.of(1981, Month.MARCH, 3, 22, 36);
    }

    public LocalDateTime getComponentDateTime() {
        return LocalDateTime.of(getJuliosBirthday(), getSampleLocalTime());
    }

    public LocalDate getTodayFromLocalDateTime() {
        return LocalDateTime.now().toLocalDate();
    }

    public int getDifferenceBetweenLimaAndBsAs() {
        ZonedDateTime lima = ZonedDateTime.now(ZoneId.of("America/Lima"));
        ZonedDateTime buenosAires = ZonedDateTime.now(ZoneId.of("America/Buenos_Aires"));
        return lima.getHour() - buenosAires.getHour();
    }
}
