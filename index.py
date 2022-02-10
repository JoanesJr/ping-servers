import subprocess

def startStop(initial):
    response = input(initial).upper()
    if response == 'Y':
        print(end = '\n \n')
        print("INICIANDO VERIFICAÇÃO, AGUARDE".center(60, '='))
        ping()
    else:
        print()
        print("PROGRAMA ENCERRADO".center(60, '*'))

    return

def ping():
    mask = '172.29.10.'
    ips = {
        "AD" : mask + '10',
        "SERV005" : mask + '16',
        "ESPELHO AD" : mask + '11',
        "TS34" : mask + '134',
        "TS36" : mask + '136'
    }

    log = {}
    for server, ip in ips.items():
        call = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE)
        if call.returncode == 0:
            log[server] = [ip, 'Sucesso']
        else:
            log[server] = [ip, 'Falha']
    print()
    
    for server, result in sorted(log.items()):
        print(f"{server} [{result[0]}] = {result[1]}")

    msg = "Deseja realizar a verificação novamente? [y/n]"
    return startStop(msg);
    
    
initial = "Deseja iniciar a verificação? [y/n]"
startStop(initial)

