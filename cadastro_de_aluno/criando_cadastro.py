
arquivo = open('bancodedados.csv', 'a')

while True:
 nome = input ('Digite seu nome:')
 idade = input ('Digite sua idade:')
 graduação = input ('Digite sua gradução?')
 dataAniversario = input('digite sua data de nascimento:')
 planoAcademia = input ('Digite o seu plano: ')
 


 dados_alunos = [nome, idade, graduação, dataAniversario, planoAcademia, '\n'] 
    
 arquivo.write("," .join(dados_alunos))

 novoCadastro = input ('Deseja adicionar novo cadastro?')

 if novoCadastro.lower() != 'sim':
  break