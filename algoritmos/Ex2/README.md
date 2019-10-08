O exercicio 2 trata da utilização de desenvolvimento orientado a objeto, e consiste na utilização de superclasses para à resolução do 
problema apresentado.
A ideia básica na utilização de superclasses é a abstração de código, onde classes podem herdar atributos, métodos e funções de outras 
classes. Mas para que isto funcione as classes dependentes devem possuir características que abrangam grandes grupos de outras classes,
como é apresentada a questão.
Temos a classe Animal que engloba Mamiferos e Aves.
Já a classe Mamifero engloba outras classes que são Cao, Gato, Elefante e Cavalo.
E a classe Ave engloba outras classes que são Andorinha, Pato e Galinha.

A classe Animal possui carrega características que os animais em sua maioria possuem como por exemplo peso e quantidade de patas.
Já a classe Mamifero possui características especificas de animais mamiferos, como possuir pêlos, amamentar, possuir dentes.
E esta abstração aconteçe por fim nas classe dos animais que por sua vez possuem características mais únicas em que se diferenciam 
dos outros animais.
Esta mesma idéia de generalização das características ocorrem nas Aves e isto pode ser visto com maiores riquezas de detalhes no código.

Dificuldade:
  Para a resolução deste exercício foi apenas a definição da superclasse com a linguagem python, o que não foi dificíl resolver.
  import SuperClasse
  
    def __init__(self):
		  super().__init__()
    
  Como já havia implementado outras vezes o mesmo exercicio em C e Java não tive dificuldades na compreensão do problema.
  O programa é executado mostrando alguns atibutos e algumas ações que os animais instanciados possuem, sendo uma execução de cada animal.
