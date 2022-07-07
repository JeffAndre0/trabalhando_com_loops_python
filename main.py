from lib2to3.pgen2.token import RPAR
from threading import currentThread


curso = {
    "nome": "Programando em python",
    "conteudos": [
        "Conceitos básicos da linguagem",
        "Biblioteca-padrão",
        "Coleções",
        "Estruturas de controle",
        "Funções e módulos",
        "Parâmetros default, variáveis e nomeados",
        "Programação funcional",
        "Classes e Objetos",
        "Herança e Polimorfismo",
        "Armazenamento de dados em arquivos",
        "Acesso a banco de dados",
        "Manipulação de API Rest",
        "Testes unitários"
                  ],
    "instrutor": {
        "Nome": "Júlio Pereira",
        "Contato": "33 99154-2651"
    },
    "alunos": [
        "Aldair Ribeiro",
        "André de Castro",
        "Danilo Pereira",
        "Elton Lima",
        "Fabio Ferraz",
        "Gideão Sudario",
        "Jefferson André",
        "Jeova Vieira",
        "Lucas Pires",
        "Marcelo São Pedro",
        "Meggy Mendes",
        "Michael Rochumback",
        "Nilza Ferreira",
        "Paulo Sergio"
    ]
}

# ========= USANDO  APENAS METHODOS, IF OU LIST COMPREENSHIONS

# CRIAR OS CONJUNTOS

# 1 - Lista de todas as keys do curso
list_keys = [x for x in curso.keys()]
print("\n","*"*15,"Exercicio1","*"*15)
print (list_keys)

# 2 - Lista de tuplas para criar 5 relacionamento entre os alunos
print("\n","*"*15,"Exercicio2","*"*15)
list_tuple = [(curso["alunos"][count],curso["alunos"][count + 1]) for count in range(5)]
print(list_tuple)

# 3 - Lista com os nomes dos alunos
print("\n","*"*15,"Exercicio3","*"*15)
list_alunos = [x for x in curso["alunos"]]
print(list_alunos)

# 4 - Lista com os nomes dos alunos MOSTRANDO APENAS AS TRÊS PRIMEIRAS LETRAS
print("\n","*"*15,"Exercicio4","*"*15)
list_alunos_3_letras = [x[0:3] for x in curso["alunos"]]
print(list_alunos_3_letras)

# 5 - Lista de conteudos que COMECA COM A LETRA A
print("\n","*"*15,"Exercicio5","*"*15)
list_conteudos_com_a = [x for x in curso["conteudos"] if x[0].lower() == "a"]
print(list_conteudos_com_a)

# ========= USANDO APENAS METHODOS, IF OU WHILE

conteudo_while = []

# 1 - Preencher o conjunto conteudo_while com uma lista de dicionarios dos conteudos conforme o exemplo:
print("\n","*"*15,"Exercicios com While","*"*15)

print("\n","*"*15,"Exercicio1","*"*15)
# Exemplo: [{nome: "Conceitos básicos da linguagem", active: True}]
count = 0
while count < len(curso["conteudos"]):
    conteudo_while.append({"nome":curso["conteudos"][count],"active":True}) 
    count = count + 1   
    
print(conteudo_while)

# ========= USANDO APENAS METHODOS, IF OU FOR

curso_for = {}
alunos_for = []
conteudos_for = []
instrutor_for = {}
print("\n","*"*15,"Exercicios com listas","*"*15)

# 1 - preenche a coleção curso_for com os dados do curso e acrecenta o atributo active com valor true
print("\n","*"*15,"Exercicio1","*"*15)
curso_for = [{"nome":x, "active":True } for x in curso.items()]
print(curso_for)

# 2 - preenche a coleção alunos_for com os nomes dos alunos.
print("\n","*"*15,"Exercicio2","*"*15)
alunos_for = [x for x in curso["alunos"]]
print(alunos_for)

# 3 - preenche a coleção conteudos_for com os dados dos conteudos.
print("\n","*"*15,"Exercicio3","*"*15)
conteudos_for = [x for x in curso["conteudos"]]
print(conteudos_for)

# 4 - preenche a coleção instrutor_for com os dados dos instrutor e acrecentar os meios de contatos
print("\n","*"*15,"Exercicio4","*"*15)
instrutor_for = {x for x in curso["instrutor"].items()}
print(instrutor_for)

# 5 - faça uma busca na coleção curso_for e imprime apenas os dados do instrutor
print("\n","*"*15,"Exercicio5","*"*15)
for lists in curso_for:
    for tuples in lists.values():
        if (tuples != True and "instrutor" in tuples):
                print(tuples)
                
# 6 - faça uma busca na coleção alunos e imprime o aluno com index 5
print("\n","*"*15,"Exercicio6","*"*15)
for x in range(len(alunos_for)):
    if (x == 5):
        print(alunos_for[x])
        
# 7 - Faça uma leitura na coleção conteudos_for ALTERANDO todos conteudos a partir do index 6 para "NÃO APLICADO"
print("\n","*"*15,"Exercicio7","*"*15)
for x in range(len(conteudos_for)):
    if (x >= 6):
        conteudos_for[x] = "NÃO APLICADO"
print(conteudos_for)
