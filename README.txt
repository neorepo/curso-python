﻿/*PHP*/
$count = 11;
// ¿Qué tal esta legibilidad?
while ($count--> 1) {
    print $count . '<br>';
}

/*PHP*/
$count = 0;
// ¿Qué tal esta legibilidad?
while ($count++< 10) {
    print $count . '<br>';
}

INFORMÁTICA CONCEPTOS BÁSICOS
https://www.youtube.com/watch?v=fP_Wow2hn0Y
https://www.youtube.com/watch?v=FToDEHhpYHI

Puedes estar familiarizado con las leyes de De Morgan. Dicen que:

La negación de una conjunción es la separación de las negaciones.
var_dump( !($a && $b) );
var_dump( (!$a) || (!$b) );

La negación de una disyunción es la conjunción de las negaciones.
var_dump( !($a || $b) );
var_dump( (!$a) && (!$b) );

Escribamos lo mismo usando Python:

not (p and q) == (not p) or (not q) 
not (p or q) == (not p) and (not q)

def isYearLeap(year):
    isLeapYear = (year % 4 == 0)
    isLeapYear = isLeapYear and (year % 100 != 0)
    return isLeapYear or (year % 400 == 0)

def daysInMonth(year, month): #1900-2-28
    if not (month >= 1 and month <= 12):
        return None
    months = ['', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    if months[month] == 'Feb':
        if not isYearLeap(year):
            return 28
        else:
            return 29
    elif months[month] == 'Abr' or months[month] == 'Jun' or \
    months[month] == 'Sep' or months[month] == 'Nov':
        return 30
    else:
        return 31

def dayOfYear(year, month, day):
    dayOfYear = 0
    if not (month >= 1 and month <= 12):
        return None
    if not (day >= 1 and day <= 31):
        return None
    for i in range(1, month):
        dayOfYear += daysInMonth(year, i)
    return dayOfYear + day
    
# Año, mes, día
print( dayOfYear(2000, 12, 31) ) # 366

def isPrime(num):
    if num < 2:
        return False
    isPrime = True
    f = 2
    while f * f <= num:
        if num % f == 0:
            isPrime = False
            break
        f += 1
    return isPrime

for i in range(1, 200):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(352.5, 1.65))

SELECT nombre, count(nombre) AS total FROM localidad GROUP BY nombre ORDER BY total DESC LIMIT 1000

La raíz cuadrada de x es la misma que x^0.5
√x = x^.5