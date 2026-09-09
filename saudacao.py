from datetime import date

nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"\nOlá, {nome}! Seja muito bem-vindo(a) à jornada Python!")
print(f"Em {ano_atual}, você tem (ou vai completar) aproximadamente {idade} anos.")
