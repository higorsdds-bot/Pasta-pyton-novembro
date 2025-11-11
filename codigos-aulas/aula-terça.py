#exemplo-tupla----#
numeros =() #criação de tupla  com  o  nome numeros que irá  guarda numero fornecidos pelo usuário

while True:
    number =int(input ( "  Informe um número [ou -1 para sair]  " ))
    if number == -1:
     break 
    numeros+=(number,)
if len(numeros)>0:
        print ("\t Resultados ----- \n ")
        print(f" Numeros digitados: {numeros} ")
        print(f" quantidade: {len(numeros)}") 
        print(f"soma: {sum(numeros)}")
        print(f"Maior número: {max(numeros)}") 
        print(f" Menor numeros: {min(numeros)}")
 
        media =sum(numeros)/len(numeros)
        if media >=50:
                print (" media {media:.2f} - > alta ")
        else:
                print (" media {media:.2f} - > baixa ")    

else:
 print (" nenhum número foi adicionado ")


 
 