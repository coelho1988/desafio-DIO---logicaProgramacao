vitorias = int(input('Numero de vitorias: '))
derrotas = int(input('Numero de derrotas: '))
saldo = 0
nivel = 'default'

def calculadora (vitorias, derrotas):
    saldo = (vitorias - derrotas)
    return saldo

saldo = calculadora(vitorias, derrotas)

if saldo <= 10:
    nivel = 'Ferro'
elif saldo > 10 and saldo <= 20:
    nivel = 'Bronze'
elif saldo > 20 and saldo <= 50:
    nivel = 'Prata'
elif saldo > 50 and saldo <= 70:
    nivel = 'Ouro'
elif saldo > 70 and saldo <= 80:
    nivel = 'Platina'
elif saldo > 80 and saldo <= 90:
    nivel = 'Ascendente'
elif saldo > 90 and saldo <= 100:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'
    
print("O Herói tem saldo de {} vitorias e está no nível de {}".format(saldo, nivel))