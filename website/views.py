from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
import random
from string import ascii_uppercase

#from unixSocket import *

views = Blueprint('views', __name__)

pedidos = {}
count = 0

@views.route('/requestforport', methods=['GET', 'POST'])
def req_for_port():
    global count


    if request.method == 'POST':
        protocol = request.form.get('protocol')
        int_port = request.form.get('int_port')
        int_ip = request.form.get('int_ip')
        
        print(protocol)
        print(int_port)
        print(int_ip)

        #pedidos[len(pedidos)+2] = [protocol, int_port, int_ip]
        pedidos[count+1] = [protocol, int_port, int_ip]
        count += 1

        flash('Pedido efetuado com sucesso', category='success')
        return redirect(url_for('views.req_for_port', user=current_user))

    return render_template('reqforport.html', user=current_user)



def remove_item(chave):
    print(pedidos)
    try:
        if chave in pedidos.keys():
            del pedidos[chave]
        print(pedidos)
    except:
        print("Erro - Nao foi possivel remover o pedido")




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
    
        return redirect(url_for('views.home.', nome=cname, estado=estado, portas=portas, user=current_user))
    
 
    

    #return render_template("home.html", user=current_user)
    return render_template('home.html', user=current_user)



@views.route('/ports', methods=['GET', 'POST']) # funcional para interagir com a função hostnat do unixsocket
@login_required
def ports():

    if request.method == 'POST':
        
        action = request.form.get('action')
        fw = request.form.get('fw')
        protocol= request.form.get('protocol')
        ext_port = request.form.get('ext_port')
        ext_ip = request.form.get('ext_ip')
        int_port = request.form.get('int_port')
        int_ip = request.form.get('int_ip')
        chave = request.form.get('key_to_remove')
        
        
        try:
            remove_item(int(chave))
        except:
            print("Erro não foi recebido nenhum valor para remover da lista de pedidos")


        print(action)
        print(fw)
        print(protocol)
        print(ext_port)
        print(ext_ip)
        print(int_port)
        print(int_ip)
        
        #hostnat(action, fw, protocol, ext_port, ext_ip, int_ip, int_port)
        return redirect(url_for('views.ports', dicionario=pedidos , user=current_user))

    return render_template('ports.html', dicionario=pedidos , user=current_user)







@views.route('/firewall', methods=['GET', 'POST']) # funcional para interagir com a função hostnat do unixsocket
@login_required
def firewall():

    if request.method == 'POST':
        
        action = request.form.get('action')
        fw = request.form.get('fw')
        protocol= request.form.get('protocol')
        port = request.form.get('port')
       
    
        
        

       

        print(action)
        print(fw)
        print(protocol)
        print(port)
        print(type(port))
       
        #hostfw(action, fw, protocol, port)
    
        return redirect(url_for('views.firewall', user=current_user))
        

    return render_template('firewall.html', user=current_user)





