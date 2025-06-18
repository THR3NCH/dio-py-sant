MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")

if idade >= 18:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode Fazer as Aulas Teoricas, mas não pode fazer as praticas!")
else:
    print("Ainda não pode tirar a CNH.")