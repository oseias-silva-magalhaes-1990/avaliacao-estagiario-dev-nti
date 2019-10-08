from ClasseCao import Cao
from ClasseGato import Gato
from ClasseElefante import Elefante
from ClasseCavalo import Cavalo
from ClasseAndorinha import Andorinha
from ClassePato import Pato
from ClasseGalinha import Galinha

class Iniciar(object):

	def __init__(self):
		pass
		
	#Iniciando Mamiferos
	def iniciarCao(self):
		#Instancia Animal
		cao = Cao()
		#Inseir Entradas
		cao.inserirQtdPatas(4)
		cao.inserirPeso(5)
		cao.inserirTipoPelo('longo')
		cao.inserirCorPelo('preto')
		cao.inserirRaca('poodle')

		#Imprime saídas
		print('\nEu sou um cão')
		print('Possuo '+str(cao.obterQtdPatas())+' patas')
		print('Tenho '+str(cao.obterPeso())+'Kg')
		print('O meu pelo é '+ cao.obterTipoPelo())
		print('Sou da raça '+ cao.obterRaca())
		#Ação
		print('E '+cao.atacar())

	def iniciarGato(self):
		#Instancia Animal
		gato = Gato()
		#Inseir Entradas
		gato.inserirQtdPatas(4)
		gato.inserirPeso(1.5)
		gato.inserirRaca('persa')
		#Imprime saídas
		print('\nEu sou um gato')
		print('Possuo '+str(gato.obterQtdPatas())+' patas')
		print('Tenho '+str(gato.obterPeso())+'Kg')
		print('Sou da raça '+ gato.obterRaca())
		#Ação
		print('Eu '+gato.emitirSom())
		print('E '+gato.mamar())

	def iniciarElefante(self):
		#Instancia Animal
		elefante = Elefante()
		#Inseir Entradas
		elefante.inserirQtdPatas(4)
		elefante.inserirPeso(6)
		elefante.inserirRaca('Elefante-da-savana')
		#Imprime saídas
		print('\nEu sou um '+ elefante.obterRaca())
		print('Possuo '+str(elefante.obterQtdPatas())+' patas')
		print('Tenho '+str(elefante.obterPeso())+' Toneladas')
		#Ação
		print('O som que eu emito é um '+elefante.emitirSom())
		print('Eu '+elefante.beber()+' água')

	def iniciarCavalo(self):
		#Instancia Animal
		cavalo = Cavalo()
		#Inseir Entradas
		cavalo.inserirPeso(350)
		cavalo.inserirRaca('Mangalarga')
		#Imprime Saidas
		print('\nEu sou um '+ cavalo.obterRaca())
		print('Tenho '+str(cavalo.obterPeso())+' Kg')
		#Ação
		print('Estou '+cavalo.emitirSom())
		print('Eu '+cavalo.correr())


	#Iniciando Aves
	def iniciarAndorinha(self):
		#Instancia Animal
		andorinha = Andorinha()
		andorinha.inserirPeso(100)
		andorinha.inserirQtdPatas(2)
		print('\nSou uma Andorinha ')
		print('Tenho '+str(andorinha.obterQtdPatas())+' patas')
		print('Eu peso '+str(andorinha.obterPeso())+'g')
		print('Eu '+andorinha.emitirSom()+ ' e também '+andorinha.voar())

	def inciarPato(self):
		#Instancia Animal
		pato = Pato()
		pato.inserirQtdPatas(2)
		print('\nEu sou um pato e '+pato.emitirSom())
		print('Também '+pato.nadar()+' com minhas '+str(pato.obterQtdPatas())+' patas nadadeiras')

	def iniciarGalinha(self):
		#Instancia Animal
		galinha = Galinha()
		print('\nEu sou uma galinha')
		print('Eu '+ galinha.bicar())
		print('Eu '+galinha.trocarPenas() + ' e também '+galinha.chocarOvos())


def main():
    run = Iniciar()
    #Mamiferos
    run.iniciarCao()
    run.iniciarGato()
    run.iniciarElefante()
    run.iniciarCavalo()
    #Aves
    run.iniciarAndorinha()
    run.inciarPato()
    run.iniciarGalinha()

if __name__ == '__main__':
    main()
