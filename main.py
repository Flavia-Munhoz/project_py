print("Boa tarde! Digite uma nota para verificar a condição\nde aprovado ou não.")
print("numeros aceitos são de 0 até 10.\nDigite a nota:")

nota =float(input(""))

if nota <6.0 and nota >=0:
    print("Você tirou nota F ")
elif nota >=6.0 and nota <7.0:
    print("Você tirou nota D")
elif nota >=7.0 and nota <8.0:
    print("Você tirou nota C")
elif nota >=8.0 and nota <9.0:
    print("Você tirou nota B")
elif nota >=9.0 and nota <= 10.0:
    print("Você tirou nota A")
else:
    print("Você nao digitou um valor válido")
    print("Você nao digitou um número válido...")    