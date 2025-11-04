def informacoes(**informacao):
     for chave,valor in informacao.itens():
              print (f"{chave}:{informacao}")
informacoes (nome= "lucas", idade=20, canal= "EletricGames", naturalidade= "Brasileiro ", cpf=17692744726 )
  