import os # Biblioteca os integra os programas e recursos do sistema operacional

ip_ou_host = input(f"""{"="*37}
Digite o Ip ou host a ser verificado: """)
print("=" * 37)

os.system(f'ping -n 6 {ip_ou_host}') # Chamando system da biblioteca os - comando: ping -n num de pacotes que serão 6 
print("="*60)