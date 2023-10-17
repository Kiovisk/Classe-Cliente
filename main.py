from Cliente import *
nome = input("Nome: ")
idade = int(input("Idade: "))
email = input("Email: ")
telefone = int(input("Telefone: "))
assinante = input("Assinante (S/N): ")

if assinante.lower() == "s":
  assinante = "SIM"
else:
    assinante = "Não"

cliente = Cliente(nome, idade, email, telefone, assinante)

exibir_cliente=input("\nExibir cadastro (S/N):")
if exibir_cliente.lower() == "s":
    cliente.exibir_dados()
elif exibir_cliente.lower() == "n":
  print('Cadastro encerrado')
