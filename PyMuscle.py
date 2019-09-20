from modules.GetElements import *
from tabulate import tabulate

storeby = ("Rubén Maiquez Cánovas", "rmaiquez.es", str(2017))

print()
print("-------------------------------------------- ")
print("Rutina de ejercicios para entrenamiento TRX: ")
print("-------------------------------------------- ")
print()
print(tabulate([['Pierna', GetElements(legs)], ['Pecho', GetElements(chest)], ['Biceps', GetElements(biceps)],
                ['Triceps', GetElements(triceps)],
                ['Espalda', GetElements(back)], ['Hombros', GetElements(shoulders)],
                ['Abdominales', GetElements(abdominal)]],
               headers=['Músculo', 'Ejercicio/s'], tablefmt='orgtbl'))

print("\nStore by: ")
print('. '.join(storeby))
