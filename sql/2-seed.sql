use youfoodie;

insert into endereco_restaurante(pais, cep, estado, cidade, rua, numero, complemento) values
('Brasil', '12245-000', 'São Paulo', 'São José dos Campos', 'Av. Andrômeda', 1200, 'Loja 12'),
('Brasil', '12246-767', 'São Paulo', 'São José dos Campos', 'Rua dos Chads', 67, null);

insert into restaurante(id_endereco, nome, categoria, imagem, preco_entrega, avaliacao, tempo_medio_entrega_min) values
(1, 'Chud Burger', 'Hamburgi', 'chudburger.png', 10, 2.4, null),
(2, 'Mogador Burguer', 'Hambúrgueres e Lanches', 'mogadorburguer.png', 0, 5, 15);

insert into prato(id_restaurante, nome, descricao, categoria, imagem, preco) values
(1, 'Chud-Burger', 'Hambúrguer artesanal com queijo e molho especial', 'Lanches', 'xburger.png', 12.67),
(1, 'Betata Frita', 'Porção média de batata frita crocante', 'Porções', 'batata.png', 14.5),
(1, 'Refrigerante', 'Lata 350ml', 'Bebidas', 'refri.png', 6),
(2, 'Cheese Burguer', 'Um delicioso hamburguer com queijo prato e hamburguer artesanal', 'Lanches', 'cheeseburguer.png', 18),
(2, 'Smash Burguer', 'Um delicioso lanche esmagador com um hamburguer artesanal', 'Lanches', 'smashburguer.png', 22),
(2, 'Duplo Cheddar', 'Um delicioso hamburguer com queijo cheddar', 'Lanches', 'duplocheddar.png', 25),
(2, 'Batata Frita', 'Porção deliciosa de batata frita crocante', 'Porções', 'batatasmash.png', 14),
(2, 'Onion Rings', 'Porção deliciosa de aneis de cebola', 'Porções', 'onionrings.png', 18),
(2, 'Mini Churros', 'Sobremesa deliciosa de caramelo', 'Sobremesas', 'minichurros.png', 20),
(2, 'Petit Gateau', 'Sobremesa deliciosa com massa de bolo, chocolate e sorvete', 'Sobremesas', 'petitgateau.png', 24),
(2, 'Macarons', 'Sobremesa francesa deliciosa', 'Sobremesas', 'macaron.png', 22);

insert into endereco_usuario(pais, cep, estado, cidade, rua, numero) values
('Brasil', '12246-600', 'São Paulo', 'São José dos Campos', 'Rua dos Admins', 404);

insert into usuario(id_endereco, email, senha, cpf, primeiro_nome, ultimo_nome) values
(1, 'admin@admin.com', 'admin', '12345678900', 'Admin', null);

insert into pedido(id_usuario, id_restaurante, preco_total, estado) values
(1, 1, 50.40, 'cancelado');

insert into item_pedido(id_prato, id_pedido, preco_unitario, quantidade) values
(1, 1, 29.90, 1),
(2, 1, 14.50, 1),
(3, 1, 6.00, 1);
