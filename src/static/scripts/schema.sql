create database if not exists youfoodie;

use youfoodie;

create table endereco_restaurante(
	id int auto_increment primary key,
    pais varchar(30) not null,
    cep varchar(9) not null,
    estado varchar(45) not null,
    cidade varchar(60) not null,
    rua varchar(60) not null,
    numero int(5) not null,
    complemento varchar(100)
);

create table restaurante(
	id int auto_increment primary key,
    id_endereco int not null,
    nome varchar(45) not null,
    foreign key(id_endereco) references endereco_restaurante(id)
);

create table prato(
	id int auto_increment primary key,
    id_restaurante int not null,
    nome varchar(60) not null,
    descricao varchar(255) not null,
    categoria varchar(45) not null,
    imagem varchar(255),
    preco decimal(6,2),
    foreign key(id_restaurante) references restaurante(id)
);

create table endereco_usuario(
	id int auto_increment primary key,
    pais varchar(30) not null,
    cep varchar(9) not null,
    estado varchar(45) not null,
    cidade varchar(60) not null,
    rua varchar(60) not null,
    numero int(5) not null,
    complemento varchar(100)
);

create table usuario(
	id int auto_increment primary key,
    id_endereco int not null,
    email varchar(255) not null unique,
    senha varchar(255) not null,
    cpf char(11) not null unique,
    primeiro_nome varchar(30) not null,
    ultimo_nome varchar(45) not null,
    foreign key(id_endereco) references endereco_usuario(id)
);

create table pedido(
	id int auto_increment primary key,
    id_usuario int not null,
    id_restaurante int not null,
    preco_total decimal(10,2) not null,
    estado enum('pendente', 'confirmado', 'preparando','em_entrega', 'entregue', 'cancelado') default 'pendente',
    data_hora_pedido datetime default current_timestamp,
    foreign key(id_usuario) references usuario(id),
    foreign key(id_restaurante) references restaurante(id)
);

create table item_pedido(
	id int auto_increment primary key,
    id_prato int not null,
    id_pedido int not null,
    preco_unitario decimal(6,2) not null,
    quantidade int not null default 1,
    foreign key(id_prato) references prato(id),
    foreign key(id_pedido) references pedido(id)
);