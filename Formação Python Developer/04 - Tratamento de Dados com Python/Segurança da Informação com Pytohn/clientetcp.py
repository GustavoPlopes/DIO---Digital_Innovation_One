import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou")
        print(f"Erro: {error}")
        sys.exit()
    
    print("Socket criado com sucesso")
    
    HostAlvo = input("Digite o Host ou Ip as ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com Sucesso no Host: {HostAlvo} e na porta: {PortaAlvo}")
        s.shutdown(2)
    except socket.error as error:
        print("A conexão falhou")
        print(f'Erro: {error}')
        sys.exit()
        
if __name__ == "__main__":
    main()