


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

def show_scholarships():
    """
    Description: 
    - Muestra el menú para la selección de tipos de beca
    """
    print("\n************** Tipos de beca **************")
    print("[1] Requisitos Tipo A - Bloque completo & Todas las materias ganadas y notas superiores a 70")
    print("[2] Requisitos Tipo B - Promedio igual o mayor a 90 & Notas igual o mayor a 80")
    print("[3] Requisitos Tipo C - Promedio igual o mayor a 85 y ha sido asistente nivel A o B")
    print("[0] Salir del programa\n")

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
        

def execute_2():
    """
    Description: 
    - Muestra el enunciado e inicia la ejecución específica del ejercicio
    """
    import json

    statement = '''{
    "msg":"Enunciado:
A usted se le pide que realice un programa que, recibiendo la medida de tres lados, se imprima si estos tres lados pueden formar un triángulo.
Tres lados forman un triángulo si la suma de dos lados de un triángulo siempre es mayor al tercer lado.
Por ejemplo, si tenemos un lado a que mide 7, un lado b que mide 10 y un lado c que mide 5, se compara si la suma de los lados b y c es mayor que la medida del lado a.
Luego si la suma de los lados a y b es mayor que la medida del lado c y, finalmente, si la suma del lado a y c es mayor que la medida del lado b.
Si las tres condiciones se cumplen, entonces los tres lados conforman un triángulo."
}'''
    print("\n")
    print(json.loads(statement, strict=False)["msg"])

    print("\nIngrese los valores de cada lado que formarán el triángulo:\n")
    lado_1 = float(input("Lado 1:\n"))
    lado_2 = float(input("Lado 2:\n"))
    lado_3 = float(input("Lado 3:\n"))

    triangle_yes = "Los lados SI forman un triángulo" 
    triangle_no = "Los lados NO forman un triángulo" 

    if sum([lado_1, lado_2]) > lado_3:
        if sum([lado_2, lado_3]) > lado_1:
            if sum([lado_1, lado_3]) > lado_2:
                msg = triangle_yes
            else:
                msg = triangle_no
        else:
                msg = triangle_no
    else:
        msg = triangle_no

    print("\n"+msg+"\nMuchas gracias.")

def create_score_list(p_scores_qty) -> list:
    """
    Description:
    - Obtiene las notas de los cursos, las agrega a una lista y retorna la lista "score_list"
    """
    counter = 1
    score_list = []

    for _ in range(p_scores_qty):
        score = input("Ingrese el valor de la nota No."+counter)
        score_list.append(score)
    
    return score_list

def calc_avg(p_score_list, p_scores_qty) -> float:
    """
    Description:
    - Calcula el promedio de los elementos en la lista
    """
    avg = (sum(p_score_list)/p_scores_qty)
    return avg

def validate_sch(p_continue, p_min_score, p_score_list) -> str:
    """
    Description:
    - Determina si el estudiante es candidato para la aprobación de la beca Tipo A o B.
    """

    if p_continue == 1:

        for i in p_score_list:
            if i > p_min_score:
                i += 1
                for i in p_min_score:
                    if i > p_min_score:
                        i += 1
                        for i in p_min_score:
                            if i > p_min_score:
                                i += 1
                                for i in p_min_score:
                                    if i > p_min_score:
                                       msg = "El estudiante SI aplica para la beca."
                                    else:
                                       msg = "El estudiante NO aplica para la beca."
                            else:
                                msg = "El estudiante NO aplica para la beca."
                    else:
                        msg = "El estudiante NO aplica para la beca."
            else:
                msg = "El estudiante NO aplica para la beca."
    return msg

def execute_3():
    """
    Description: 
    - Muestra el enunciado e inicia la ejecución específica del ejercicio
    """
    import json
    import time

    statement = '''{
    "msg":"Enunciado:
A usted se le pide realizar un programa que determine si un estudiante de una institución universitaria es candidato a que le den una beca. 
Un estudiante puede optar por una beca solamente si:
A. Si lleva el bloque de cuatro materias completo, y no perdió ninguna materia, por lo que el sistema siempre va a recibir las notas de las cuatro materias y todas las notas van a ser superiores a 70. 
B. Si el promedio de las notas de las materias del cuatrimestre es igual o superior a noventa, y si ninguna nota está por debajo de 8. 
C. Si el promedio de las materias del cuatrimestre es igual a superior a 85, fue asistente durante el cuatrimestre y la calificación que se le otorgó como asistente fue de una A o una B. 
Si su calificación como asistente fue de una C no tiene derecho a beca, sin importar el promedio."
}'''
    print("\n")
    print(json.loads(statement, strict=False)["msg"])

    scores_qty = int(input("\nIngrese la cantidad de notas para verificar:\n"))

    score_list = create_score_list(scores_qty)

    avg = calc_avg(score_list, scores_qty)

    show_scholarships()
    sch_option = int(input("Seleccione el tipo de aplicación para la beca:"))
    
    while sch_option != 0:

        if sch_option == 1:
            
            min_score = 70

            full_block = int(input("El estudiante lleva bloque de cuatro materias completo? \n1. Si\n2. No"))

            if full_block == 1:
                next_step = full_block
                msg = validate_sch(next_step, min_score, score_list)
        
        elif sch_option == 2:
            min_score = 80

            if avg >= 90:
                next_step = 1
                msg = validate_sch(next_step, min_score, score_list)

        elif sch_option == 3:
            min_avg = 85

            if avg >= min_avg:
                assist = int(input("El estudiante fue asistente durante el cuatrimestre anterior? \n1. Si\n2. No"))

                if assist == 1:
                    assist_level = input("Ingrese la calificación que obtuvo el estudiante como asistente: \n1. A\n2. B\n3. C")

                    if assist_level == 1 and assist_level == 2:
                        msg = "El estudiante SI aplica para la beca."
                    else:
                        msg = "El estudiante NO aplica para la beca."
                else:
                    msg = "El estudiante SI aplica para la beca."
            else:
                msg = "El estudiante SI aplica para la beca."

        else:
            print("Ha ingresado un valor incorrecto, favor intente nuevamente.\nMuchas gracias!")
            time.sleep(3)
            show_exercises()
        
        time.sleep(3)
        show_exercises()


