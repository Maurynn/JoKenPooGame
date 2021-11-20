'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
from random import randint
from termcolor import colored

print('{:=^69}' .format(colored('PEDRA_PAPEL_TESOURA','green')))
p = 0
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
while True:
	p += 1
	print(colored('SUAS OPÇÕES:','yellow'))
	print(colored('[ 0 ] PEDRA','yellow'))
	print(colored('[ 1 ] PAPEL','yellow'))
	print(colored('[ 2 ] TESOURA','yellow'))
	jogador = int(input('QUAL A SUA JOGADA? '))
	print(colored('JO','green'))
	sleep(1)
	print(colored('KEN','yellow'))
	sleep(1)
	print(colored('PÔOO!!!','red'))
	print('<>'*13)
	print(colored(f'O COMPUTADOR JOGOU: {itens [computador]}','yellow'))
	print(colored(f'O JOGADOR JOGOU: {itens [jogador]}','yellow'))
	print('<>'*13)
	if computador == 0:
			if jogador == 0:
				print('EMPATE')
			elif jogador == 1:
				print('JOGADOR VENCEU..')
			elif jogador == 2:
			  print('COMPUTADOR VENCEU.')
			else:
				print('OPÇÃO INVÁLIDA')
	elif computador == 1:
			if jogador == 0:
				print('COMPUTADOR VENCEU')
			elif jogador == 1:
				print('EMPATE')
			elif jogador == 2:
				print('JOGADOR VENCEU')
			else:
			    print('OPÇÃO INVÁLIDA')
	elif computador == 2:
			if jogador == 0:
				print('JOGADOR VENCEU')
			elif jogador == 1:
				print('COMPUTADOR VENCEU')
			elif jogador == 2:
				print('EMPATE')
			else:
				print('OPÇÃO INVÁLIDA')
	sair = str(input('DESEJA JOGAR NOVAMENTE? [S / N]')) .upper()
	if sair == 'N':
			break
print(colored('VEZES JOGADAS: %i' % p,'green'))
print(colored('FIM DE JOGO','green'))
				

		
		

		
	
