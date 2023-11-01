from os import system
system('cls')

print('_______________________________________________________________')
print('                         Registro de Alunos                    ')
print('_______________________________________________________________')
print()
nome = input('Digite o nome do(a) aluno(a): ')
matematica = float(input('Nota da matéria matemática: '))
geografia = float(input('Nota da matéria geografia: '))
historia = float(input('Nota da matéria história: '))
media = (matematica+geografia+historia)/3
print('________________________________________________________________')
print()

notas = {nome: {'matematica': matematica, 'geografia': geografia, 'historia': historia, 'media': round(media, 2)}}

print(f'Aluno(a) {nome} cadastrado(a) com sucesso!')
print('*********************************************************************************************************')
print(notas)
print('*********************************************************************************************************')