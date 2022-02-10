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
    mask = 'xxx.xxx.xxx.' #exemplo mask = '172.29.10.'
    ips = {
        "exemple1" : mask + '10', # "AD" : mask + '10',
        "exemple2" : mask + '16', # "FILES SERVER - CPD" : mask + '15',
        "exmple3" : mask + '12' #the last item not need finally ","
    }

    log = {}
    for server, ip in ips.items():
        command = ['ping', '-n', '1', ip]
        call = subprocess.run(command, stdout=subprocess.PIPE)
        if call.returncode == 0:
            log[server] = [ip, 'Sucesso']
        else:
            log[server] = [ip, 'Falha']
    print()
    
    for server, result in sorted(log.items()):
        print("{:<30} {:<20} {:<1}".format(server, result[0], result[1]))

    print()
    msg = "Deseja realizar a verificação novamente? [y/n]"
    return startStop(msg);
    
    
initial = "Deseja iniciar a verificação? [y/n]"
startStop(initial)

