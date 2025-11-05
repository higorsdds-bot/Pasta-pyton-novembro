import customtkinter as ctk

ctk.set_appearance_mode('dark')

def login_valido():
    
    usuario = entry_usuario.get() #estou declarando minha variavel de usuário
    senha = entry_senha.get() #estou declarando minha variavel de senha
    if usuario == 'Mestre' and senha == '1234': # utilizo meu If para verificar se o login é verdadeiro 
        resultado_login.configure(text='Login feito com sucesso!', text_color='green') 
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

app = ctk.CTk() #comando para criar interface da aplicação 
app.title('~ Sistema de login ~') # Nome que irá aparecer no executavel 
app.geometry('800x650') # determino o diametro da janela que vai abrir 
# criação de campos
# label (titulo para digitar o usuário)
label_usuario = ctk.CTkLabel(app, text=' | Usuário |') # area para implementar o login do do name  
label_usuario.pack(pady=10)
# Entry (campo para inserir o usuario)
entry_usuario = ctk.CTkEntry(app, placeholder_text='')
entry_usuario.pack(pady=10) # inseri o usuário aqui 
# label senha
label_senha = ctk.CTkLabel(app, text='| Senha |')  # area para implementar o login da senha 
label_senha.pack(pady=10) # <- inseri a senha aqui
# Entry (campo para inserir a senha)
entry_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
entry_senha.pack(pady=10)
# button botao para login
button = ctk.CTkButton(app, text='Login', command=login_valido) # comando para chamar a função e realizar login
button.pack(pady=10)
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)
app.mainloop()