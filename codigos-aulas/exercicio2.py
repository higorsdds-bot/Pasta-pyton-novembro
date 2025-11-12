name = []
salario: int = []
while True:
    names = input("\n Informe o nome do usuário \n -> ") 
    salarios = int (input(f" Informe o salario do {names} \n -> "))
    button = input (" Deseja 'sair' ou continuar " )
    name.append(name)   
    salario.append(salarios) 
    if button=="sair":
        print (" Funcionários_registrados")
        break 
for i in range(1):
  print  (" Informe -> sair <- para finalizar o programa ")
  print (f" O total de funcionários cadastrados {len(name)}" )
  print (f" A média sálarial {sum(salario)/len(salario)}")
    
 
 
   