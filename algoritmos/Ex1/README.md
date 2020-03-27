Foi criado um banco de dados denominado comercio que possui duas tabelas venda e produto.
Utilizando o MySQL Workbench foram desenvolvidas as tabelas abaixo:

1º Criando o banco

CREATE DATABASE comercio;

2º Criando a tabela produto

CREATE TABLE `produto` (
  `id_produto` int(10) NOT NULL,
  `codigo` int(10) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `valorUnitario` decimal(14,2) NOT NULL,
  `quantidade` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

3º Definindo id_produto como chave primária

ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`);
  
4º Definindo id_produto como auto-increment

ALTER TABLE `produto`
  MODIFY `id_produto` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
  
5º Criando a tabela venda
 
CREATE TABLE `venda` (
  `numero` int(10) NOT NULL,
  `dhVenda` datetime NOT NULL,
  `itensVendidos` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

6º Definindo numero como chave primária

ALTER TABLE `venda`
  ADD PRIMARY KEY (`numero`);

7º Definindo numero como auto_increment

ALTER TABLE `venda`
  MODIFY `numero` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

Utilizando a Linguagem Python como ferramenta para desenvolvimento orientado a objeto das classes e interfaces do sistema de comércio.
Foram criadas as classes BDProduto, BDVenda, Venda, Produto, TelaVenda, TelaCadastro, TelaMensagem, MenuPrincipal, Controller.
Utilizando algumas validações de banco para verificar se por exemplo um produto já estava cadastrado, verificar se um 
produto a ser vendido existia no sistema, e para cada caso específico mostrando uma mensagem de erro ou alerta para o usuário.
Passando a concluir a venda apenas quando todos os requisitos fossem atendidos, e os eventuais erros corrigidos.

Na classe TelaMenuPrincipal foram criados dois botões sendo um Vender e outro Cadastrar, onde pode-se alternar entre as janelas mantendo as mesmas abertas ao mesmo tempo.
Todo Cadastro é registrado na tabela cadastro do banco de dados comercio e armazena o código do produto, nome, valor unitário e a 
quantidade.
Para realização dos testes durante o desenvolvmento, foi necessário inserir alguns produtos como pode ser visto abaixo:


Exemplo de inserção:
INSERT INTO `produto` (`id_produto`, `codigo`, `nome`, `valorUnitario`, `quantidade`) VALUES
(1, 1, 'tv32', '1000.00', 900);


Toda venda realizada é salva na tabela venda, com os dados de hora e data da venda, e uma coluna itensVendidos do tipo longtext recebe
concatenado uma sequência de valores como observa-se abaixo:
O número da venda registrado é auto-incremento que varia a cada inserção, e é único cabendo no cenário deste sistema de comércio.
dhVenda = datetime.current()
itensVendidos += (codigo, quantidade, valor com desconto),...,(codigo, quantidade, valor com desconto),valor total

Exemplo de registro de venda:
INSERT INTO `venda` (`numero`, `dhVenda`, `itensVendidos`) VALUES
(1, '2019-10-07 14:02:00', '(1,20,2000.0),39600.00');

Para cada produto que é vendido a venda é registrada e o produto é dcrementado do estoque, sendo atualizado a tabela dos produtos a cada
venda realizada.
Para fins de testes rápido sem a necessidade do editor, disponibilizei também um arquivo executável o qual tem sua funcionalidade
idependente.

Na tela de venda foram despostos alguns campos para a entrada dos dados, sendo Codigo e Quantidade os únicos valores a serem digitados
para efetuação de uma venda, após a inserção dos valores nos campos o usuário clica no botão calcular, assim os campos são preenchidos
com os valores já cadastrados pertencentes ao código do produto digitado e a tela de venda também possui os campos para inserir os 
valores calculados com desconto para cada produto. Também estão dispostos dois campos que após calcular mostram o total de descontos 
obtidos e o valor total da venda. Após calcular o botão para finalização da compra se torna visível ao usuário e este pode concluir a 
venda.

A tela de Cadastro visa ser simples não incluíndo outras funcionalidades além do cadastro do produto no banco, sendo dispostos os 
para a entrada dos dados do produto e uma verificação de banco para saber de o produto à ser cadastrado já existe no sistema.

A tela mensagem aparece para finalizar as vendas e os cadastros, mostrando um mensagem de confirmação com um botão de ok.
Foram utilizadas as bibliotecas PyQt5 para as interfaces gráficas, a datetime, a sys, e pymysql para a comunicação entre o sistema e o
banco de dados.

A pasta do código está localizado neste repositório no formato .rar com nome Sistema de Comercio.rar
Como o arquivo executável possui um tamanho maior que o permitido no gitHub estou disponiblizando o link para download abaixo:
https://drive.google.com/open?id=19RK_JItINgPuK2bmYBnPcC6rWiDk3IBc
