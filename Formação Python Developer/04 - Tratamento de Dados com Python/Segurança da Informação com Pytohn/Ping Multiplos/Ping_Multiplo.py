import os
import time

with open('hosts.txt') as file: # Abrindo o arquivo para leitura
    dump = file.read() # ///
    dump = dump.splitlines() # Colocando o cada ip em linha unica
    
    for ip in dump: # Fazendo um for para cada ip verificando e mostrando
        print(f'''Verificando o ip: {ip} 
{"-"*60}''') 
        os.system(f'ping {ip}')
        time.sleep(5)