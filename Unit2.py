#A
basis = [
    [1 if i == j else 0 for i in range(10)]
    for j in range(10)
]

#B
import random
def random_character():
    params = [0]*10
    while True:
        params = [random.randint(-3, 3) for _ in range(10)]
        norm2 = sum(x*x for x in params)**0.5
        norm1 = sum(abs(x) for x in params)
        if norm2 <= 5 and norm1 <= 10:
            return params

#C
names = [
    "Strength","Agility","Wisdom","Luck","Vitality",
    "Magic","Charm","Speed","Dexterity","Focus"
]

params = random_character()
character = {names[i]: params[i] for i in range(10)}
print(character)
