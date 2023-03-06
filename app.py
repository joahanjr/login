from flask import Flask, render_template,request, redirect,url_for
from flask_mysqldb import MySQL
from flask_login import logout_user, login_required

from config import config

from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)
db = MySQL(app)

@app.route('/')
def index_():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        #print(request.form['username'])
        #print(request.form['password'])
        user = User(0,request.form['username'], request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('index'))
            else:
                """ flash('contaseña incorrecta...') """
            return render_template('auth/login.html')
        else: 
            """ flash('usuario no encontrado...') """
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/servicios.html')
def servicios():
    return render_template('servicios.html')

@app.route('/quienesSomos.html')
def quienesSomos():
    return render_template('quienesSomos.html')

@app.route('/especialidades.html')
def especialidades():
    return render_template('especialidades.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/cita.html')
def cita():
    return redirect(url_for('login'))

if __name__=='__main__':
    app.config.from_object(config['developmet'])
    app.run()