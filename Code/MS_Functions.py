





def show_exercises():
    """
    Description: 
    - Muestra el menú de los ejercicios
    """
    print("\n************** MENÚ DE EJERCICIOS **************")
    print("[1] Ejercicio No.1 - Fecha del día de mañana")
    print("[2] Ejercicio No.2 - Lados para un triángulo")
    print("[3] Ejercicio No.3 - Candidato a beca")
    print("[4] Ejercicio No.4 - Promoción teléfonica")
    print("[5] Ejercicio No.5 - Edad de una piedra")
    print("[0] Salir del programa")

def execute_1():
    """
    Description: 
    - Muestra el enunciado e inicia la ejecución específica del ejercicio
    """

    import datetime
    import calendar

    enunciado = "A usted le piden realizar un programa que, recibiendo el día, el mes y el año de la fecha de hoy, calcule e imprima la fecha del día de mañana.\n"
    print("\n"+enunciado)

    date_today = input("Ingrese la fecha del día de hoy. Formato: mm/dd/aaaa\n")
    leap_year = int(input("Este es un año bisiesto? 1. Si / 2. No\n"))
    format_date_formula = '%m/%d/%Y'
    try:
        date_formatted = datetime.datetime.strptime(date_today, format_date_formula)
    except:
        print("\nError: Este no es un año bisiesto. Favor ingresar una fecha correcta, muchas gracias!")
        

    else:
        day = date_formatted.date().day
        month = date_formatted.date().month
        year = date_formatted.date().year
        list_31 = [1,3,5,7,8,10,12]

        def validate_date(p_day, p_month, p_year, p_cant_days_month):
            """
            Descripción: Función que valida y calcula el nuevo día, mes y año y al finalizar imprime un mensaje de la nueva fecha.
            """
            
            if p_day > 0 and p_day <= p_cant_days_month:
                if p_day == p_cant_days_month:
                    p_day = 1
                    p_month = p_month + 1
                else:
                    p_day = p_day + 1

                import locale
                locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
                month_string = calendar.month_name[p_month]
                msg = f"\nInformación:\nMañana es {str(p_day)} de {month_string} del {str(p_year)}\nMuchas por utilizar nuestro sistema.\n"

            else:
                msg = "Fecha incorrecta, favor trate intente nuevamente."

            print(msg)
            
        if month != 2:
            in_list = list_31.count(month)

            if in_list > 0:
                cant_days_month = 31

                if month == 12:
                    year = year + 1
                    month = 0
                    validate_date(day, month, year, cant_days_month)
                else:
                    validate_date(day, month, year, cant_days_month)
            
            else:
                cant_days_month = 30
                validate_date(day, month, year, cant_days_month)
        
        else:
            if leap_year == 1:
                cant_days_month = 29
                validate_date(day, month, year, cant_days_month)
            else:
                cant_days_month = 28
                validate_date(day, month, year, cant_days_month)
    finally:
        print("\nGracias por utilizar nuestro sistema de fechas y calendario.\n")
        



