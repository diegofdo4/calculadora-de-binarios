import time # importamos librerias de tiempo para mostrar los resultados con un delay

# funcion para realizar la suma de los numeros en binario 

def plus(bin2,bin3):
    bin4 = [] #guarda el resultado
    save = 0 # guarda el residuo de la suma de binarios
    size = 0 # guarda el tamaño de la tabla mas grande
    
    # verificar numero binario mayor
    
    if len(bin3)<len(bin2):
       size = len(bin2)
       t=len(bin2)-len(bin3)
       
       # rellenar la tabla del numero menor con ceros para poder realizar la operación 
       
       for l in range(t):
           bin3.append(0)
    elif len(bin3)>len(bin2):
        size = len(bin3) 
        t=len(bin3)-len(bin2)
        for l in range(t):
           bin2.append(0)
    else:
        size = len(bin2)
        
    # ciclo para recorrer el tamaño de la tabla y realizar la suma en cada posición 
    
    for i in range(size):
        if save == 0:
            
            # condiciones para a tener en cuenta para el resultado en la posición i de la lista 
            
            if bin2[i] == 1 and bin3[i] == 1:
                bin4.append(0)
                save = 1
            elif bin2[i] == 1 and bin3[i]==0:
                bin4.append(1)
            elif bin2[i] == 0 and bin3[i]==1:
                bin4.append(1)
            elif bin2[i]==0 and bin3[i]==0:
                bin4.append(0)
        elif save == 1 and bin2[i] == 1 and bin3[i]==0:
                bin4.append(0)
        elif save == 1 and bin2[i] == 0 and bin3[i]==1:
            bin4.append(0)
        elif save == 1 and bin2[i]==0 and bin3[i]==0:
            save =0
            bin4.append(1)
        elif save == 1 and bin2[i]==1 and bin3[i]==1:
            bin4.append(1)
            
    # si queda un residuo 1 al final de la operacion se agrega al resultado
    
    if save == 1:
        bin4.append(save)
    return bin4

# menu del programa

def run():
    
    # entradas decimales
    
    dec = int(input('ingrese su numero decimal: '))
    dec2 = int(input('ingrese segundo valor decimal: '))
    dec3 = dec+dec2
    bin = []
    bin0 = []
    bin1 = []
    
    # converción decimal a binario
    
    while dec!=0:
        conv = int(dec%2)
        dec = int(dec/2)
        bin.append(conv)
        
    while dec2!=0:   
        conv2 = int(dec2%2)
        dec2 = int(dec2/2)
        bin1.append(conv2)
        
    # mostrar converción
    
    bin0 = bin[::-1]
    time.sleep(1)
    print('\n primer numero decimal', bin0)
    bin0 = bin1[::-1]
    time.sleep(1)
    print('\n segundo numero decimal', bin0)
    
    # llamar funcion suma y enviar parametros (numeros convertidos a binarios)
    
    sum = plus(bin, bin1)
    time.sleep(1)
    print('\n suma de binarios', sum[::-1], 'equivale a ',dec3,'\n')
    print('\n ')
    

if __name__=='__main__':
    run()