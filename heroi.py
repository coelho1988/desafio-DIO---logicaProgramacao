nome = input('seu nome de herói: ')
xp = int(input('quantidade de experiencia acumulada: '))
nivel = 'default'

if xp <= 1000:
    nivel = 'Ferro'
elif xp > 1000 and xp <= 2000:
    nivel = 'Bronze'
elif xp > 2000 and xp <= 5000:
    nivel = 'Prata'
elif xp > 5000 and xp <= 7000:
    nivel = 'Ouro'
elif xp > 7000 and xp <= 8000:
    nivel = 'Platina'
elif xp > 8000 and xp <= 9000:
    nivel = 'Ascendente'
elif xp > 9000 and xp <= 10000:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'
    
print("O Herói de nome {} está no nível de {}".format(nome, nivel))