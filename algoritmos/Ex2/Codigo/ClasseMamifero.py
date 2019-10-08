from ReinoAnimal import Animal

class Mamifero(Animal):

	def __init__(self):
		super().__init__()

	def mamar(self):
		return 'estou bebendo leite'

	def beber(self):
		return 'esou bebendo'

	def cocarPelos(self):
		return 'estou coçando meus pelos'

	def morder(self):
		return 'estou mordendo'
