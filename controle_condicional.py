# Variável de nota de um aluno
nota = 83

# Mapeando a nota para conceito
if nota >= 90:
    conceito = "A"  # conceito A se nota >= 90
elif nota >= 75:
    conceito = "B"  # conceito B se nota entre 75 e 89
elif nota >= 60:
    conceito = "C"  # conceito C se nota entre 60 e 74
else:
    conceito = "D"  # conceito D se nota < 60

print("Nota:", nota)
print("Conceito:", conceito)

# Exemplo de operador lógico
# Considera aprovado se a nota for >= 60 e o conceito não for D
aprovado = nota >= 60 and conceito != "D"
print("Aprovado?", aprovado)