from ClasseMamifero import Mamifero
class Elefante(Mamifero):

	def __init__(self):
		super().__init__()
		self.cor = 'cor'
		self.raca = 'raca'

	def inserirCor(self, cor):
		self.cor = cor

	def inserirRaca(self, raca):
		self.raca = raca

	def obterCor(self):
		return self.cor

	def obterRaca(self):
		return self.raca

	def emitirSom(self):
		return 'barrir'

