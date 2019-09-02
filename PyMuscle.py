from random import sample
from tabulate import tabulate

legs = ['Zancadas en suspensión', 'Sentadilla en suspensión', 'Carrera resistida', 'Curl femoral', 'Sentadilla búlgara',
        'Mountain climber']
chest = ['Press de pecho en suspensión', 'Flexiones con TRX', 'Flexiones con las piernas apoyadas en las asas']
biceps = ['Curl de Bíceps en TRX']
triceps = ['Fondos en TRX', 'Extensiones de tríceps', 'Tríceps kickbacks']
back = ['Remo en suspensión', 'Superman']
shoulders = ['Face Pull en TRX']
abdominal = ['Encogimiento abdominal en suspensión', 'Plancha', 'Plancha lateral']


def getlegs():
    chosenLegs = sample(legs, 2)
    return ', '.join(chosenLegs)


def getchest():
    chosenChest = sample(chest, 1)
    return ', '.join(chosenChest)


def getbiceps():
    chosenBiceps = sample(biceps, 1)
    return ', '.join(chosenBiceps)


def gettriceps():
    chosenTriceps = sample(triceps, 1)
    return ', '.join(chosenTriceps)


def getback():
    chosenBack = sample(back, 1)
    return ', '.join(chosenBack)


def getshoulders():
    chosenShoulders = sample(shoulders, 1)
    return ', '.join(chosenShoulders)


def getabdominal():
    chosenAbdominal = sample(abdominal, 1)
    return ', '.join(chosenAbdominal)


print("-------------------------------------------- ")
print("Rutina de ejercicios para entrenamiento TRX: ")
print("-------------------------------------------- ")
print()
print(tabulate([['Pierna', getlegs()], ['Pecho', getchest()], ['Biceps', getbiceps()], ['Triceps', gettriceps()],
                ['Espalda', getback()], ['Hombros', getshoulders()], ['Abdominales', getabdominal()]],
               headers=['Músculo', 'Ejercicio/s'], tablefmt='orgtbl'))
