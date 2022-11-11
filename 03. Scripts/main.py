import os
import argparse

parser = argparse.ArgumentParser(description='Criação automática de pasta de estrutura de pastas')

parser.add_argument('-d','--diretorio', type=str, help='Diretório que a estrutura será criada')
parser.add_argument('-l','--lista_pastas_primarias', type=str, help='Nome das pastas primárias que serão criadas', nargs='+')

args = parser.parse_args()

def cria_pastas(diretorio, lista_pastas):
  
    size = len(lista_pastas)
    
    for i in range(size):
        
        n_pasta = str(i).zfill(2)
        
        os.mkdir(diretorio+'/'+n_pasta+' - '+lista_pastas[i])
        
        lista_sub_pasta = ['00. Backup', '01. Input', '02. Output','03. Scripts', '04. Dashboards']
        
        for l in range(len(lista_sub_pasta)):
            
            os.mkdir(diretorio+'/'+n_pasta+' - '+lista_pastas[i]+'/'+lista_sub_pasta[l])
            


if __name__ == '__main__':

    cria_pastas(diretorio=args.diretorio, 
                                lista_pastas=args.lista_pastas_primarias)