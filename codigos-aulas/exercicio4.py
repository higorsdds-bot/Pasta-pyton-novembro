alunos = ()
def chamada_pietra(alunos):
    lista_alunos = list(alunos)
    while True:
     valuer = int(input("Informe a numeração desejada (-1 para encerrar): "))
     if valuer == -1:
      print("Adição encerrada. Obrigado por usar o sistema HG-retz")
      break
    lista_alunos.append(valuer)
    alunos = tuple(lista_alunos)
    print(alunos)
    print (f"{max(alunos)}")
    print (f"{min(alunos)}")
    
chamada_pietra(alunos)
    
 