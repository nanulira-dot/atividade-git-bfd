# Trabalhando com listas
frutas = ["maçã", "banana", "laranja"]  # criando uma lista de frutas

# Adicionando um elemento ao final da lista
frutas.append("uva")  
print("Lista após append:", frutas)

# Atualizando um elemento pelo índice
frutas[1] = "pera"  
print("Lista após atualização:", frutas)

# Removendo um elemento da lista
frutas.remove("laranja")  
print("Lista após remoção:", frutas)


# Trabalhando com dicionários
aluno = {"nome": "Naiumy", "idade": 18}  # criando um dicionário

# Adicionando uma nova chave
aluno["nota"] = 10  
print("Dicionário após adicionar nota:", aluno)

# Atualizando valor de uma chave existente
aluno["idade"] = 19  
print("Dicionário após atualizar idade:", aluno)

# Removendo uma chave
del aluno["nota"]  
print("Dicionário após remover nota:", aluno)