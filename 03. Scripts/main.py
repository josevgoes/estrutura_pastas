
class EstruturaPastas:
    
    def cria_pastas(diretorio, lista_pastas):
        
        import os
        
        size = len(lista_pastas)
        
        for i in range(size):
            
            n_pasta = str(i).zfill(2)
            
            os.mkdir(diretorio+'/'+n_pasta+' - '+lista_pastas[i])
            
            lista_sub_pasta = ['00. Backup', '01. Input', '02. Output','03. Scripts', '04. Dashboards']
            
            for l in range(len(lista_sub_pasta)):
                
                os.mkdir(diretorio+'/'+n_pasta+' - '+lista_pastas[i]+'/'+lista_sub_pasta[l])
            


EstruturaPastas.cria_pastas(diretorio='C:/Users/jose.goes/desktop', 
                            lista_pastas=['Pasta Qualquer'])