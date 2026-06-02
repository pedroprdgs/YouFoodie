from utils.db import *

def get_restaurantes():
    query = "SELECT * FROM restaurante ORDER BY avaliacao DESC"

    restaurantes = fetch_data(query)
    return restaurantes

def get_restaurante_endereco(id_restaurante):
    query = "SELECT * FROM endereco_restaurante WHERE id = %s"
    
    endereco = fetch_data(query, (id_restaurante,))
    return endereco[0]

def get_restaurante_by_id(id_restaurante):
    query = "SELECT * FROM restaurante WHERE id = %s"

    restaurante = fetch_data(query, (id_restaurante,))
    return restaurante[0]

def get_restaurante_by_prato(id_prato):
    query = """
        SELECT r.* FROM restaurante r
        INNER JOIN prato p on p.id_restaurante = r.id
        WHERE p.id = %s"""

    restaurante = fetch_data(query, (id_prato,))
    return restaurante[0]

def get_restaurante_pratos(id_restaurante):
    query = "SELECT * FROM prato WHERE id_restaurante = %s"

    pratos = fetch_data(query, (id_restaurante,))
    return pratos

def get_pratos():
    query = "SELECT * FROM prato"

    pratos = fetch_data(query)
    return pratos

def get_prato_by_id(id_prato):
    query = "SELECT * FROM prato WHERE id = %s"

    prato = fetch_data(query, (id_prato,))
    return prato[0]

def get_categorias():
    query = "SELECT categoria FROM prato GROUP BY categoria"

    pratos = fetch_data(query)
    return pratos

def get_usuario_endereco(id_usuario):
    query = "SELECT * FROM endereco_usuario WHERE id = %s"
    
    endereco = fetch_data(query, (id_usuario,))
    return endereco[0]

def get_usuario_by_id(id_usuario):
    query = "SELECT * FROM usuario WHERE id = %s"

    usuario = fetch_data(query, (id_usuario,))
    return usuario[0]

def auth_user(email, senha):
    query = "SELECT * FROM usuario WHERE email = %s AND senha = %s"

    usuario = fetch_data(query, (email, senha))
    return usuario[0] if usuario else None

def create_usuario(email, senha, cpf, primeiro_nome, ultimo_nome=None, **endereco):
    query = """
        INSERT INTO endereco_usuario(pais, cep, estado, cidade, rua, numero) VALUES
        (%s, %s, %s, %s, %s, %s)
    """
    id_endereco = execute_query(query, (endereco['pais'], endereco['cep'], endereco['estado'], endereco['cidade'], endereco['rua'], endereco['numero']), return_lastrowid=True)

    query = """
        INSERT INTO usuario(id_endereco, email, senha, cpf, primeiro_nome, ultimo_nome) VALUES
        (%s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (id_endereco, email, senha, cpf, primeiro_nome, ultimo_nome))

def create_pedido(id_usuario, id_restaurante, itens):
    preco_total = 0

    itens_pedido = []

    for item in itens:
        prato = get_prato_by_id(item['id_prato'])
        preco_unitario = float(prato['preco'])
        preco_total += preco_unitario * item['quantidade']
        itens_pedido.append((item['id_prato'], preco_unitario, item['quantidade']))
    
    query = """
        INSERT INTO pedido(id_usuario, id_restaurante, preco_total) VALUES
        (%s, %s, %s)
    """

    id_pedido = execute_query(query, (id_usuario, id_restaurante, preco_total), return_lastrowid=True)

    query = """
        INSERT INTO item_pedido(id_prato, id_pedido, preco_unitario, quantidade) VALUES
        (%s, %s, %s, %s)
    """

    for id_prato, preco_unitario, quantidade in itens_pedido:
        execute_query(query, (id_prato, id_pedido, preco_unitario, quantidade))

def get_pedidos_usuario(id_usuario):
    query = """
        SELECT p.id, p.data_hora_pedido, p.preco_total, r.nome AS restaurante_nome FROM pedido p
        INNER JOIN restaurante r ON p.id_restaurante = r.id
        WHERE p.id_usuario = %s
        ORDER BY p.data_hora_pedido DESC
    """

    pedidos = fetch_data(query, (id_usuario,))
    return pedidos
