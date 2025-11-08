# Append () - metodo que serve para adicionar um novo elemento ao final da lista
#Remove () - metodo para remover um elemento da lista
paises =[" Brasil"," Portugol"," irã"]
print (paises)
paises.append(input(" Informe um pais "))
print (paises)
paises.remove(input("  Qual pais deseja tira do brics "))
print(paises)

if paises in paises: 
 paises.remove(paises)
 print (f" Pais removido { paises }")
else:
 print (" Pais nao encontrado ")