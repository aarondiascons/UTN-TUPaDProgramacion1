#Ejercicio 1 — “Caja del Kiosco”

nombre = input("¿Cómo es tu nombre?")

while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("¿Cómo es tu nombre?")

cantidad = input("¿Cuántos productos vas a comprar?")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: debe ser un número mayor a 0")
    cantidad = input("Cantidad de productos:")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio:")

    while not precio.isdigit():
        print("Error: precio inválido")
        precio = input(f"Producto {i} - Precio:")

    precio = int(precio)
    total_sin_descuento += precio

    descuento = input("¿Tiene descuento? (S/N):").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N")
        descuento = input("¿Tiene descuento? (S/N):").lower()

    if descuento == "s":
        precio_descuento = precio * 0.9
    else:
        precio_descuento = precio

    total_con_descuento += precio_descuento


ahorro = total_sin_descuento - total_con_descuento

promedio = total_con_descuento / cantidad

print("\n --- RESULTADOS ---")

print(f"Total sin descuentos: $ {total_sin_descuento}")

print(f"Total con descuentos: $ {total_con_descuento:.2f}")

print(f"Ahorro: ${ahorro:.2f}")

print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:

    usuario = input(f"Intento {intentos +1}/3 - Usuario:")
    clave = input("Clave:")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada")

while acceso:

    print("\n1) Estado de inscripción 2) Cambiar clave  3) Mensaje  4) Salir")
    opcion = input("Opción:")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción:")

    opcion = int(opcion)

    while opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango")
        opcion = input("Opción:")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción:")

        opcion = int(opcion)

    if opcion == 1:
        print("Inscripto")

    elif opcion == 2:
        nueva = input("Nueva clave:")

        if len(nueva) < 6:
            print("Error: mínimo 6 caracteres.")
        else:
            confirmar = input("Confirmar clave:")

            if nueva == confirmar:
                clave_correcta = nueva
                print("Clave cambiada correctamente.")
            else:
                print("Error: las claves no coinciden.")

    elif opcion == 3:
        print("¡Seguí así, vas muy bien en programación!")

    elif opcion == 4:
        print("Saliendo del sistema...")
        acceso = False

#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre = input("¿Cómo es su nombre? ")

while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("¿Cómo es su nombre? ")

sistema = True

while sistema:

    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda del día  4) Ver resumen general  5) Cerrar sistema")

    opcion = input("Opción:")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción:")

    opcion = int(opcion)

    while opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango")
        opcion = input("Opción:")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción:")

        opcion = int(opcion)


    if opcion == 1:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: ingrese 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: solo letras")
            paciente = input("Nombre del paciente: ")

        if dia == 1:
            
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: paciente ya tiene turno ese día")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                elif lunes2 == "":
                    lunes2 = paciente
                elif lunes3 == "":
                    lunes3 = paciente
                elif lunes4 == "":
                    lunes4 = paciente
                else:
                    print("No hay turnos disponibles en Lunes")

        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: paciente ya tiene turno ese día")
            else:
                if martes1 == "":
                    martes1 = paciente
                elif martes2 == "":
                    martes2 = paciente
                elif martes3 == "":
                    martes3 = paciente
                else:
                    print("No hay turnos disponibles en Martes")

   
    elif opcion == 2:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: ingrese 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: solo letras")
            paciente = input("Nombre del paciente: ")

        encontrado = False

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado")
        else:
            print("Paciente no encontrado")

   
    elif opcion == 3:

        dia = input("Día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: ingrese 1 o 2")
            dia = input("Día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        if dia == 1:
            print("\n--- Lunes ---")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\n--- Martes ---")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    
    elif opcion == 4:

        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("\n--- RESUMEN ---")
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Ambos días tienen la misma cantidad de turnos")

    elif opcion == 5:
        print("Sistema cerrado")
        sistema = False

#Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

nombre = input("¿Cómo es su nombre agente? ")

while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("¿Cómo es su nombre agente? ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("¡La alarma bloqueó la bóveda! DERROTA")
        break

    print("\n--- ESTADO ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas} | Alarma: {alarma}")

    print("\n1) Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) Hackear panel (-10 energía, -3 tiempo)")
    print("3) Descansar (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido")
            opcion = input("Opción: ")

        opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("¡Forzaste demasiadas veces! La cerradura se trabó")
            alarma = True
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma! Elegí número (1-3): ")

                while not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
                    print("Error: ingrese 1, 2 o 3")
                    riesgo = input("Riesgo de alarma! Elegí número (1-3): ")

                if int(riesgo) == 3:
                    alarma = True
                    print("¡Se activó la alarma!")

            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura!")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura")

    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10
            print("Descansaste pero la alarma te drenó energía")

if cerraduras_abiertas == 3:
    print("\n¡VICTORIA! Abriste la bóveda")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA: te quedaste sin recursos")

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("1) Ataque Pesado")
    print("2) Ráfaga Veloz")
    print("3) Curar")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_base * 1.5
        else:
            danio = danio_base

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")