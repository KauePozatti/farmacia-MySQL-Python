create database farmacia;
use farmacia;

set sql_safe_updates=0;

create table clientes
(
id_cliente int auto_increment primary key,
nome varchar(255) not null,
telefone varchar(11) unique not null,
email varchar(255) unique not null,
endereco text not null
);

create table produtos
(
id_produto int auto_increment primary key,
nome varchar(255) not null,
descricao text not null,
preco decimal(10, 2) not null,
quantidade_estoque int, 
data_validade date not null
);

create table vendas
(
id_venda int auto_increment primary key,
data_venda date not null,
total decimal(10, 2) not null,
cliente_id int not null,
foreign key (cliente_id) references clientes (id_cliente)
);

create table itens_venda 
(
id_itens int auto_increment primary key,
quantidade int,
preco_unitario decimal(10, 2) not null,
subtotal decimal(10, 2) not null,
venda_id int not null,
produto_id int not null,
foreign key (venda_id) references vendas (id_venda),
foreign key (produto_id) references produtos (id_produto)
);

create table fornecedores
(
id_fornecedor int auto_increment primary key,
nome varchar(255) not null,
cnpj varchar(14) unique not null,
telefone varchar(11) not null,
email varchar(255) unique not null
);

create table compras
(
id_compra int auto_increment primary key,
data_compra date not null,
total decimal(10, 2) not null,
fornecedor_id int not null,
foreign key (fornecedor_id) references fornecedores (id_fornecedor)
);

create table itens_compra
(
id_itens_compra int auto_increment primary key,
quantidade int not null,
preco_unitario decimal(10, 2) not null,
subtotal decimal(10, 2) not null,
compra_id int not null,
produto_id int not null,
foreign key (compra_id) references compras (id_compra),
foreign key (produto_id) references produtos (id_produto)
);

create view vendas_vw as 
select * from clientes C 
inner join vendas V
on C.id_cliente = V.id_venda;

select * from vendas_vw;


