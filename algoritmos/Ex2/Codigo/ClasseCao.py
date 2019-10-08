from ClasseMamifero import Mamifero

class Cao(Mamifero):

	def __init__(self):
		super().__init__()
		self.tipoPelo = 'tipoPelo'
		self.corPelo = 'corPelo'
		self.raca = 'raca'

	def inserirCorPelo(self, corPelo):
		self.corPelo = corPelo

	def inserirRaca(self, raca):
		self.raca = raca

	def inserirTipoPelo(self,tipoPelo):
		self.tipoPelo = tipoPelo

	def obterCorPelo(self):
		return self.corPelo

	def obterRaca(self):
		return self.raca

	def obterTipoPelo(self):
		return self.tipoPelo

	def emitirSom(self):
		return 'latindo'

	def atacar(self):
		return 'estou atacando'

	def farejar(self):
		return 'estou farejando'

