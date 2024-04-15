from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
import random
from string import ascii_uppercase

#from unixSocket import *

views = Blueprint('views', __name__)








@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    
  

    if request.method == 'POST':
        cname = request.form.get('nome')
        type = request.form.get('type')
        
        #print(cname)
        #print(type)
        
        
        # dados = GetInfo(cname, type)
        #response = json.loads(dados)
        
        #estado = response["Estado"]
        #portas = response["Ports"]
        
        estado = "Ligado"
        portas = "23,45"

        #print(jsonify({'status': 'success', 'message': 'Dados recebidos com sucesso!'}))
    
        return render_template('home.html', nome=cname, estado=estado, portas=portas, user=current_user)
    
 
    

    #return render_template("home.html", user=current_user)
    return render_template('home.html', user=current_user)



@views.route('/ports', methods=['GET', 'POST'])
@login_required
def ports():

    if request.method == 'POST':
        name = request.form.get('name')
        type = request.form.get('type')
        action = request.form.get('action')
        fw = request.form.get('fw')
        protocol= request.form.get('protocol')
        port = request.form.get('port')
        
        
        
        print(name)
        print(type)
        print(action)
        print(fw)
        print(protocol)
        print(port)
        
        #sendPort(name, type, action, fw, protocol, port)

    return render_template('ports.html', user=current_user)







