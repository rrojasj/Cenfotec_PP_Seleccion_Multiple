import time
from MS_Functions import *

show_exercises()
excercise = int(input("\nSeleccione una opción: \n"))

while excercise != 0:
    
    if excercise == 1:
        execute_1()

    elif excercise == 2:
        execute_2()
    
    elif excercise == 3:
        execute_3
    
    elif excercise == 4:
        print()

    elif excercise == 5:
        print()
    
    time.sleep(3)
    show_exercises()
    excercise = int(input("\nSeleccione una opción: \n"))
    