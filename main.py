def contar_as(string):
    return string.lower().count('a')

# Solicita que o usuário insira uma string
texto = input("Digite uma palavra para contar quantas vezes a letra 'a' aparece: ")
quantidade_as = contar_as(texto)

print(f"A letra 'a' aparece {quantidade_as} vezes na string.")
