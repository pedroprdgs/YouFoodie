from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from utils.functions import *

app = Flask(__name__)
app.secret_key = "seila"

@app.route('/')
def index():
    return render_template('index.html', pratos=get_pratos(), restaurantes=get_restaurantes(), get_restaurante_by_prato=get_restaurante_by_prato)

@app.route('/restaurante')
def restaurante():
    id_restaurante = request.args.get('id')
    restaurante = get_restaurante_by_id(id_restaurante)
    endereco = get_restaurante_endereco(id_restaurante)
    pratos = get_restaurante_pratos(id_restaurante)

    return render_template('restaurante.html', restaurante=restaurante, endereco=endereco, pratos=pratos)

@app.route('/restaurantes')
def restaurantes():
    return render_template('restaurantes.html', restaurantes=get_restaurantes())

@app.route('/pratos')
def pratos():
    return render_template('pratos.html', pratos=get_pratos(), categorias=get_categorias(), get_restaurante_by_prato=get_restaurante_by_prato)

@app.route('/carrinho')
def carrinho():
    itens = session.get('carrinho', [])
    pratos = []
    total = 0

    for item in itens:
        prato = get_prato_by_id(item['id_prato']) if item['id_prato'] else None
        if prato is None: 
            continue

        subtotal = prato['preco'] * item['quantidade']
        pratos.append({"prato": prato, "quantidade": item['quantidade'], "subtotal": subtotal})
        total += subtotal

    return render_template('carrinho.html', pratos=pratos, total=total)

@app.route('/carrinho/adicionar', methods=['POST'])
def adicionar_carrinho():
    id_prato = request.json.get('id_prato')
    
    carrinho = session.get('carrinho', [])
    for item in carrinho:
        if item['id_prato'] == id_prato:
            item['quantidade'] += 1
            break
    else:
        carrinho.append({
            "id_prato": id_prato,
            "quantidade": 1
        })
    session['carrinho'] = carrinho
    return {"success": True}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = auth_user(email, senha)

        if usuario:
            session['usuario_id'] = usuario['id']
            session['usuario_email'] = usuario['email']
            print(session)
            
            return redirect(url_for('index'))
        else:
            flash("Email ou senha inválidos.", "danger")
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        endereco = {
            'pais': request.form.get('pais'),
            'cep': request.form.get('cep'),
            'estado': request.form.get('estado'),
            'cidade': request.form.get('cidade'),
            'rua': request.form.get('rua'),
            'numero': request.form.get('numero')
        }

        usuario = {
            'email': request.form.get('email'),
            'senha': request.form.get('senha'),
            'cpf': request.form.get('cpf'),
            'primeiro_nome': request.form.get('primeiro_nome'),
            'ultimo_nome': request.form.get('ultimo_nome') if request.form.get('ultimo_nome') else None
        }

        create_usuario(usuario['email'], usuario['senha'], usuario['cpf'], usuario['primeiro_nome'], usuario['ultimo_nome'], **endereco)
        flash('Conta criada com sucesso!', 'success')
        return redirect('/login')
    return render_template('cadastro.html')

@app.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    usuario = get_usuario_by_id(session['usuario_id'])
    endereco = get_usuario_endereco(session['usuario_id'])

    return render_template('perfil.html', usuario=usuario, endereco=endereco)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
