f = open('HeroOOP.txt.docx', 'w')

import random
Supercharged = random.randint(0,3)

class Hero:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

Alva = Hero('Alva', 100, 'medium', '20', '35')

AlvaName = f"Name: {Alva.name}" 
AlvaHealth = f"Health: {Alva.HP}"
AlvaRange = f"Range: {Alva.Range}"
Alvadamage = f"damage: {Alva.damage}"
AlvaSize = f"Size: {Alva.size}"

Hela = Hero('Hela', 85, 'far', '50', '15')

HelaName = f"Name: {Hela.name}" 
HelaHealth = f"Health: {Hela.HP}"
HelaRange = f"Range: {Hela.Range}"
Heladamage = f"damage: {Hela.damage}"
HelaSize = f"Size: {Hela.size}"

f.write('What Hero would you like, Alva or Hela? ')
HeroChoice = input('What Hero would you like, Alva or Hela?')
print('')
if HeroChoice == 'Hela':
    f.write('You Chose Hela, here are her stats ')
    print('You Chose Hela, here are her stats')
    print(HelaName)
    print(HelaHealth)
    print(HelaRange)
    print(Heladamage)
    print(HelaSize)

elif HeroChoice == 'Alva':
    f.write('You Chose Alva, here are his stats ')
    print('You Chose Alva, here are his stats')
    print(AlvaName)
    print(AlvaHealth)
    print(AlvaRange)
    print(Alvadamage)
    print(AlvaSize)

import random

Supercharged1 = random.randint(0,3)


class BaseEnemy:
    def __init__(self, name, HP, Range, Supercharged, size):
        super().__init__(name, HP, Range, Supercharged, size)
        self.size = size
        self.HP = HP
        self.Range = Range
        self.size = size
print(' ')
f.write(' ')
print('There are a few other enemies you will have to battle, here they are:')
f.write('There are a few other enemies you will have to battle, here they are: ')
class BaseEnemy:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

orc = BaseEnemy('orc', 20, 'close', '15', '20')

orcName = f"Name: {orc.name}" 
orcHealth = f"Health: {orc.HP}"
orcRange = f"Range: {orc.Range}"
orcdamage = f"damage: {orc.damage}"
orcsize = f"Size: {orc.size}"
print(' ')

print(orcName)
print(orcHealth)
print(orcRange)
print(orcdamage)
print(orcsize)

f.write(' ')
f.write('Here is an Orc, this is a basic enemy and his stats are below: ')
f.write('Name: Orc')
f.write('Health: 20')
f.write('Range: close')
f.write('Damage: 15')
f.write('Size: 20')

class BaseEnemy:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

spitter = BaseEnemy('spitter', 10, 'far', '30', '25')

spitterName = f"Name: {spitter.name}" 
spitterHealth = f"Health: {spitter.HP}"
spitterRange = f"Range: {spitter.Range}"
spitterdamage = f"damage: {spitter.damage}"
spittersize = f"Size: {spitter.size}"
print(' ')

print(spitterName)
print(spitterHealth)
print(spitterRange)
print(spitterdamage)
print(spittersize)

f.write(' ')
f.write('This is a spitter, an ariel enemy, their stats are below: ')
f.write('Name: Spitter')
f.write('Health: 10')
f.write('Range: Far')
f.write('Damage: 30')
f.write('Size: 25')
f.write(' ')

class BaseEnemy:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

Firas = BaseEnemy('Firas', 50, 'close', '35', '90')

FirasName = f"Name: {Firas.name}" 
FirasHealth = f"Health: {Firas.HP}"
FirasRange = f"Range: {Firas.Range}"
Firasdamage = f"damage: {Firas.damage}"
Firassize = f"Size: {Firas.size}"
print(' ')

print(FirasName)
print(FirasHealth)
print(FirasRange)
print(Firasdamage)
print(spittersize)

f.write(' ')
f.write('This is a Firas, they are a base enemy and their stats are below: ')
f.write('Name: Firas')
f.write('Health: 50')
f.write('Range: Close')
f.write('Damage: 35')
f.write('Size: 90')
f.write(' ')

class BossEnemy:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

Usyk = BossEnemy('Usyk', 200, 'close', '80', '65')

UsykName = f"Name: {Usyk.name}" 
UsykHealth = f"Health: {Usyk.HP}"
UsykRange = f"Range: {Usyk.Range}"
Usykdamage = f"damage: {Usyk.damage}"
Usyksize = f"Size: {Usyk.size}"
print(' ')
print('Your BossEnemy is Usyk, here are his stats')
print(' ')

f.write(' ')
f.write('Your BossEnemy is Usyk, here are his stats ')
f.write(' ')

f.write('Name: Usyk')
f.write('Health: 200')
f.write('Range: Close')
f.write('Damage: 80')
f.write('Size: 65')

print(UsykName)
print(UsykHealth)
print(UsykRange)
print(Usykdamage)
print(Usyksize)

class BossEnemy:
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

Odesa = BossEnemy('Odesa', 50, 'Very Far', '150', '25')


OdesaName = f"Name: {Odesa.name}" 
OdesaHealth = f"Health: {Odesa.HP}"
OdesaRange = f"Range: {Odesa.Range}"
Odesadamage = f"damage: {Odesa.damage}"
Odesasize = f"Size: {Odesa.size}"
print(' ')
print('Your second BossEnemy is Odesa, here are her stats ')
print(' ')

f.write(' ')
f.write('Name: Odesa')
f.write('Health: 50')
f.write('Range: Close')
f.write('Damage: 80')
f.write('Size: 65')

print(OdesaName)
print(OdesaHealth)
print(OdesaRange)
print(Odesadamage)
print(Odesasize)

class MegaBoss(BossEnemy):
    def __init__(self, name, HP, Range, damage, size,):
        self.name = name
        self.HP = HP
        self.Range = Range
        self.damage = damage
        self.size = size

f.write('Name: Holloway')
f.write('Health: 400')
f.write('Range: Far')
f.write('Damage: 250')
f.write('Size: 301')

Holloway = BossEnemy('Holloway', 400, 'far', '250', '301')


HollowayName = f"Name: {Holloway.name}" 
HollowayHealth = f"Health: {Holloway.HP}"
HollowayRange = f"Range: {Holloway.Range}"
Hollowaydamage = f"damage: {Holloway.damage}"
Hollowaysize = f"Size: {Holloway.size}"
print(' ')
print('Your MegaBoss is Holloway,Good luck... the end of days is near')
print(' ')

print(HollowayName)
print(HollowayHealth)
print(HollowayRange)
print(Hollowaydamage)
print(Hollowaysize)

f.close()


