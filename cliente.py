class Cliente:
  def __init__(self, nome, idade, email, telefone, assinante):
      self.nome = nome
      self.idade = idade
      self.email = email
      self.telefone = telefone
      self.assinante = assinante

  def exibir_dados(self):
      print("Dados do cliente:")
      print("Nome:", self.nome)
      print("Idade:", self.idade)
      print("Email:", self.email)
      print("Telefone:", self.telefone)
      print("Assinante:", self.assinante)
