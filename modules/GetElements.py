from random import sample
import json

legs = ""
chest = ""
biceps = ""
triceps = ""
back = ""
shoulders = ""
abdominal = ""
muscle_list = [legs, chest, biceps, triceps, back, shoulders, abdominal]

with open('workouts/training.json') as fp:
    data = json.load(fp)

for muscle in data:
    if muscle["muscle"] == "legs":
        legs = muscle["exercises"]
        muscle_list.append(legs)
    elif muscle["muscle"] == "chest":
        chest = muscle["exercises"]
        muscle_list.append(chest)
    elif muscle["muscle"] == "biceps":
        biceps = muscle["exercises"]
        muscle_list.append(biceps)
    elif muscle["muscle"] == "triceps":
        triceps = muscle["exercises"]
        muscle_list.append(triceps)
    elif muscle["muscle"] == "back":
        back = muscle["exercises"]
        muscle_list.append(back)
    elif muscle["muscle"] == "shoulders":
        shoulders = muscle["exercises"]
        muscle_list.append(shoulders)
    elif muscle["muscle"] == "abdominal":
        abdominal = muscle["exercises"]
        muscle_list.append(abdominal)


def GetElements(muscles):
    rwork = sample(muscles, 2)
    return ' -- '.join(rwork)