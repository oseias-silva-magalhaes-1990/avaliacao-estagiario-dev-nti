from ClasseMamifero import Mamifero
class Gato(Mamifero):

	def __init__(self):
		super().__init__()
		self.tipoPelo = 'tipoPelo'
		self.corPelo = 'corPelo'
		self.raca = 'raca'

	def inserirCorPelo(self,corPelo):
		self.corPelo = corPelo

	def inserirRaca(self,raca):
		self.raca = raca

	def inserirTipoPelo(self,tipoPelo):
		self.tipoPelo = tipoPelo

	def obterTipoPelo(self):
		return self.tipoPelo

	def obterCorPelo(self):
		return self.corPelo

	def obterRaca(self):
		return self.raca

	def emitirSom(self):
		return 'miando'

	def farejar(self):
		return 'estou farejando'
