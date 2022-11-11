import os
import argparse
import sys

parser = argparse.ArgumentParser(prog='Estruturador de Pastas',
                                 description='Criação automática estrutura de pastas')

parser.add_argument('-d','--diretorio', type=str, help='Diretório que a estrutura será criada')
parser.add_argument('-p','--pasta_primarias', type=str, help='Nome das pastas primárias que serão criadas', nargs='+')
parser.add_argument('-s','--pasta_secundarias', type=str, help='Nome das pastas secundarias que serão criadas', nargs='+')

args = parser.parse_args()

def cria_pastas(diretorio, pastas_pri, pastas_sec):
    
    if len(sys.argv) == 1:
        print('Passe algum argumento para dar continudade.. --help -h para maiores info')
        sys.exit()
    else:
        pass
    size = len(pastas_pri)
    
    if pastas_sec == None:
        pastas_sec = ['00. Backup', '01. Input', '02. Output','03. Scripts', '04. Dashboards']
    else:
        pass
    
    for i in range(size):
        n_pasta = str(i).zfill(2)
        
        os.mkdir(diretorio+'/'+n_pasta+' - '+pastas_pri[i])
        
        for l in range(len(pastas_sec)):
            os.mkdir(diretorio+'/'+n_pasta+' - '+pastas_pri[i]+'/'+pastas_sec[l])
            


if __name__ == '__main__':

    cria_pastas(diretorio=args.diretorio, 
                pastas_pri=args.pasta_primarias,
                pastas_sec=args.pasta_secundarias)