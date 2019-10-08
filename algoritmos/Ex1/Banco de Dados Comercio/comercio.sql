-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 07-Out-2019 às 19:24
-- Versão do servidor: 10.1.35-MariaDB
-- versão do PHP: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `comercio`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE `produto` (
  `id_produto` int(10) NOT NULL,
  `codigo` int(10) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `valorUnitario` decimal(14,2) NOT NULL,
  `quantidade` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `produto`
--

INSERT INTO `produto` (`id_produto`, `codigo`, `nome`, `valorUnitario`, `quantidade`) VALUES
(1, 1, 'tv32', '1000.00', 935),
(2, 2, 'tv42', '2000.00', 946),
(3, 3, 'tv50pol', '3000.00', 990),
(4, 4, 'tv20pol', '4000.00', 990),
(5, 5, 'tv29', '5000.00', 990),
(6, 6, 'tv46', '25250.00', 25630),
(7, 7, 'somPortátil', '125.00', 560),
(8, 10, 'radio', '256.25', 9);

-- --------------------------------------------------------

--
-- Estrutura da tabela `venda`
--

CREATE TABLE `venda` (
  `numero` int(10) NOT NULL,
  `dhVenda` datetime NOT NULL,
  `itensVendidos` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `venda`
--

INSERT INTO `venda` (`numero`, `dhVenda`, `itensVendidos`) VALUES
(1, '2019-10-07 14:02:00', '(1,2,2000.0),2000.0'),
(2, '2019-10-07 14:03:00', '(2,10,20000.0),(1,5,5000.0),25000.0'),
(3, '2019-10-07 14:04:00', '(1,10,10000.0),(2,5,10000.0),20000.0'),
(4, '2019-10-07 14:11:00', '(10,1,256.25),256.25'),
(5, '2019-10-07 14:22:00', '(1,2,2000.0),2000.0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`);

--
-- Indexes for table `venda`
--
ALTER TABLE `venda`
  ADD PRIMARY KEY (`numero`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `produto`
--
ALTER TABLE `produto`
  MODIFY `id_produto` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `venda`
--
ALTER TABLE `venda`
  MODIFY `numero` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
