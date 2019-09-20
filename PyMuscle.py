from random import sample
from tabulate import tabulate

#  TODO: get exercises from an external file.

legs = ['Zancadas en suspensión', 'Sentadilla en suspensión', 'Carrera resistida', 'Curl femoral', 'Sentadilla búlgara',
        'Mountain climber']
chest = ['Press de pecho en suspensión', 'Flexiones con TRX', 'Flexiones con las piernas apoyadas en las anillas']
biceps = ['Curl de Bíceps en TRX', 'Biceps a dos manos']
triceps = ['Fondos en TRX', 'Extensiones de tríceps', 'Tríceps kickbacks']
back = ['Remo en suspensión', 'Superman']
shoulders = ['Face Pull en TRX', 'Aperturas en Y']
abdominal = ['Encogimiento abdominal en suspensión', 'Plancha', 'Plancha lateral']


def GetElement(muscles):
    rwork = sample(muscles, 2)
    return ' -- '.join(rwork)


print("-------------------------------------------- ")
print("Rutina de ejercicios para entrenamiento TRX: ")
print("-------------------------------------------- ")
print()
print(tabulate([['Pierna', GetElement(legs)], ['Pecho', GetElement(chest)], ['Biceps', GetElement(biceps)],
                ['Triceps', GetElement(triceps)],
                ['Espalda', GetElement(back)], ['Hombros', GetElement(shoulders)],
                ['Abdominales', GetElement(abdominal)]],
               headers=['Músculo', 'Ejercicio/s'], tablefmt='orgtbl'))
