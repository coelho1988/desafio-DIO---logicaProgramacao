class Heroi:
    def __init__ (self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def ataque(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'            
        print('o {} atacou usando {}'.format(self.tipo, ataque))

nome = input("Digite o nome do herói: ")
idade = input("Digite a idade do herói: ")
tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ")

heroi = Heroi(nome, idade, tipo)
heroi.ataque()
