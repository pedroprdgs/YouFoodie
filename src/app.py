from flask import Flask, render_template, request, redirect, url_for, session
from utils.functions import *

app = Flask(__name__)
app.secret_key = "seila"

@app.route('/')
def index():
    return render_template('index.html', pratos=get_pratos(), restaurantes=get_restaurantes(), get_restaurante_by_prato=get_restaurante_by_prato)

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
    return render_template('login.html')

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
