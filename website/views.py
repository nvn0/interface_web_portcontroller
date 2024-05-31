from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json
import random
from string import ascii_uppercase

#from unixSocketConn import *
#from teams_dm_req import *
#from discord_dm import *

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

        teamsid = request.form.get('teams_id')
        discordid = request.form.get('discord_id')
        
        print(protocol)
        print(int_port)
        print(int_ip)
        print(teamsid)
        print(discordid)
        #pedidos[len(pedidos)+2] = [protocol, int_port, int_ip]
        pedidos[count+1] = [protocol, int_port, int_ip, teamsid, discordid]
        print(pedidos)
        count += 1

        flash('Pedido efetuado com sucesso', category='success')
        return redirect(url_for('views.req_for_port', user=current_user))

    return render_template('reqforport.html', user=current_user)



def notificar(chave):
    try:
        Send_dm_teams(pedidos[chave][4])
        Send_dm_discord(pedidos[chave][5])
    except:
        print("Erro - Nao foi possivel enviar notificação")



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



@views.route('/nat', methods=['GET', 'POST']) # funcional para interagir com a função hostnat do unixsocket
@login_required
def nat():

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
            notificar(int(chave))
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
        return redirect(url_for('views.nat', dicionario=pedidos , user=current_user))

    return render_template('nat.html', dicionario=pedidos , user=current_user)







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





