#  LABORATORIO

# Tiempo Estimado

# 5-10 minutos
# Nivel de dificultad

# Facil
# Objetivos

#     Experimentar con el código Python existente.
#     Descubrir y solucionar errores básicos de sintaxis.
#     Familiarizarse con la función print() y sus capacidades de formato.

# Escenario

# Recomendamos que juegues con el código que hemos escrito para ti y que realices algunas correcciones (quizás incluso destructivas). Siéntete libre de modificar cualquier parte del código, pero hay una condición: aprende de tus errores y saca tus propias conclusiones.

# Intenta:

#     Minimizar el número de invocaciones de la función print() insertando la secuencia \n en las cadenas.
#     Hacer la flecha dos veces más grande (pero mantener las proporciones).
#     Duplicar la flecha, colocando ambas flechas lado a lado; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (te contaremos más sobre ello pronto).
#     Elimina cualquiera de las comillas y observa detenidamente la respuesta de Python; presta atención a donde Python ve un error: ¿es el lugar en donde realmente existe el error?
#     Haz lo mismo con algunos de los paréntesis.
#     Cambia cualquiera de las palabras print en otra cosa (por ejemplo de minuscula a mayuscula, Print) - ¿Qué sucede ahora?
#     Reemplaza algunas de las comillas por apóstrofes; observa lo que pasa detenidamente.

# Solución Muestra

###################
print("version original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("con menos invocaciones de 'print()': ")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("mas alto:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doble:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)