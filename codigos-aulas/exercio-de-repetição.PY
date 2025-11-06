

usuario_cadastrado=input(" Informe um usuário: ")

while True: 
  senha_cadastrada=input(" Cadastre uma senha: ")
  if len(senha_cadastrada)<=8:
   print(" senha cadastrada " )
   break
  else:
      print("  Senha muito longa.. Tente novamente\n -> ")
      
while True:
     usuario=input (" ~ Informe seu usuário ~\n ->")
     senha=input( " ^^ Informe sua senha ^^\n -> " )      
     if usuario_cadastrado==usuario and senha_cadastrada==senha:
        print ("  Login realizado com sucesso ")
        break 
     else:
       print (" Tente novamente...Senha e usuario incorretos ! ")       
  

    