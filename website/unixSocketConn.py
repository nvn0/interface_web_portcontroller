import socket
import os
import json
import time


print(os.getcwd())


# Caminho do ficheiro do socket
socket_path = "/tmp/socket_proj"

def socketPath():
    return "/tmp/socket_proj"

# Verificar se o ficheiro do socket existe
if not os.path.exists(socket_path):
    print("O ficheiro do socket não existe.")
    exit()



def host_nat_ip_ports(action, external_ip):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Type": "host",
            "Action": action,
            "External_ip": external_ip
        }
        
        client_socket.send(json.dumps(json_data).encode())




        #------------------- funçoes de formatação ---------------------------

        def receive_full_response(client_socket):
            buffer_size = 1024
            response_bytes = bytearray()

            while True:
                part = client_socket.recv(buffer_size)
                response_bytes.extend(part)
                if len(part) < buffer_size:
                    break

            return response_bytes.decode()






        def display_response(response):
            if isinstance(response, dict):
                if "ports" in response:
                    for port in response["ports"]:
                        print(f"Description: {port.get('description', '')}")
                        print(f"Protocol: {port.get('protocol', '')}")
                        print(f"Listen Port: {port.get('listen_port', '')}")
                        print(f"Target Port: {port.get('target_port', '')}")
                        print(f"Target Address: {port.get('target_address', '')}")

                if "listen_address" in response:
                    print(f"Listen Address: {response.get('listen_address', '')}")

                if "location" in response:
                    print(f"Location: {response.get('location', '')}")

            elif isinstance(response, list):
                for item in response:
                    if isinstance(item, dict):
                        print(json.dumps(item, indent=2))
                    else:
                        print(f"Unexpected item in list: {item}")
            else:
                print("Unexpected response format:", response)


        #----------------------------------------------------------------------




        time.sleep(1.7)
        # Receber a resposta do servidor
        #response_json = client_socket.recv(1024).decode()
        #response_json_full = receive_full_response(response_json)
        
        response_json_full = receive_full_response(client_socket)
        response = json.loads(response_json_full)

        

        # mosrar a resposta do servidor
        #print("Status:", response["Status"])
        #print(response)
        display_response(response)
        
        # Fechar o socket do cliente
        client_socket.close()
        
        return response

    except Exception as e:
        print("Ocorreu um erro:", e)









def hostfw(action, firewall, protocol, porta):

    socket_path = socketPath()

    try:
        # Criar uma Unix socket
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar a Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Type": "host",
            "Action": action,
            "Fw": firewall,
            "Protocol": protocol,
            "Port": porta
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.5)
        # Receber a resposta do servidor
        #response_json = client_socket.recv(1024).decode()
        #response = json.loads(response_json)

        # mostrar a resposta do servidor
        #print("Status:", response["Status"])
        #print("Mensagem:", response["Mensagem"])

        # Fechar o socket do cliente
        client_socket.close()

    except Exception as e:
        print("Ocorreu um erro:", e)


def hostnat(action, firewall, protocol, porta, external_ip, cont_ip, cont_port):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Type": "host",
            "Action": action,
            "Fw": firewall,
            "Protocol": protocol,
            "Port": porta,
            "External_ip": external_ip,
            "Container_internal_ip": cont_ip,
            "Container_internal_port": cont_port
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.7)
        # Receber a resposta do servidor
        #response_json = client_socket.recv(1024).decode()
        #response = json.loads(response_json)

        # mosrar a resposta do servidor
        #print("Status:", response["Status"])
        #print("Mensagem:", response["Mensagem"])

        # Fechar o socket do cliente
        client_socket.close()

    except Exception as e:
        print("Ocorreu um erro:", e)

########################## containers ###################################   


def contPort(container, tipo, action, firewall, protocol, porta):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Container": container,
            "Type": tipo,
            "Action": action,
            "Fw": firewall,
            "Protocol": protocol,
            "Port": porta
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.5)
        # Receber a resposta do servidor
        #response_json = client_socket.recv(1024).decode()
        #response = json.loads(response_json)

        # mosrar a resposta do servidor
        #print("Status:", response["Status"])
        #print("Mensagem:", response["Mensagem"])

        # Fechar o socket do cliente
        client_socket.close()

    except Exception as e:
        print("Ocorreu um erro:", e)




def GetInfo(container, tipo):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Container": container,
            "Type": tipo,
            "Action": "GetInfo"
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.5)
        # Receber a resposta do servidor
        response_json = client_socket.recv(1024).decode()
        response = json.loads(response_json)

        # mostrar a resposta do servidor
        print("Status:", response["Status"])
        print("Estado:", response["Estado"])
        print("Ports:", response["Ports"])
        
        
        
        # Fechar o socket do cliente
        client_socket.close()
        
        return response

    except Exception as e:
        print("Ocorreu um erro:", e)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
