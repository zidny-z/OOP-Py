class fight:
    def __init__(self, )    



import random
weaponpower  = 10
heropower = 10
critrate = 16
critdamage = 21
enemyarmor = 14

def serang():
    totalDamage = weaponpower + heropower + (random.randint(0,critrate)) + (random.randint(0,critdamage)) - enemyarmor
    if totalDamage>=31:
        print('Anda melakukan Critical Attack sebesar', totalDamage)
    elif totalDamage<=12:
        print('Immune')
    else:
        print(totalDamage,'Hit')

for i in range(100):
    serang()