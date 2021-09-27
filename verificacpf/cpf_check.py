# tratamento de erros
# checagem da quantidade de numero
# checar se há apenas numeros
meucpf = str(input("Digite aqui seu cpf ( apenas numeros)"))

check_a = meucpf[9]
check_b = meucpf[10]
soma_a, soma_b, n, m = 0

for n in range(9):
    mtp = n+1
    soma_a += ((mtp)*int(meucpf[n]))
    print(str(meucpf[n]) + " x " + str(mtp))
print(soma_a)
    

for m in range(10):
    mtp = m # varia de 11 a 2
    soma_b += ((mtp)*int(meucpf[m]))
    print(str(meucpf[m]) + " x " + str(mtp))
print(soma_b)

resto_a = "0" if (soma_a%11 == 10) else str(soma_a%11)
#resto_a = str(soma_a%11)

resto_b = "0" if (soma_b%11 == 10) else str(soma_b%11)
#resto_b = str(soma_b%11)

print(check_a + " = " + resto_a)
print(check_b + " = " + resto_b)