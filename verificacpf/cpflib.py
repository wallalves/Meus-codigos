def check_cpf(cpf):

    soma_a = soma_b = 0

    # multiplicação termo a termo e somatorio do primeiro digito
    for n in range(9):
        soma_a += ((n+1)*int(cpf[n]))

    # calculando primeiro digito verificador
    resto_a = "0" if (soma_a%11 == 10) else str(soma_a%11)
    
    # verificando se o primeiro digito está correto
    if(resto_a != cpf[9]):
        return False
    
    # multiplicação termo a termo e somatorio do segundo digito
    for m in range(10):
        soma_b += ((m)*int(cpf[m]))

    # calculando primeiro digito verificador
    resto_b = "0" if (soma_b%11 == 10) else str(soma_b%11)
    # verificando se o segundo digito está correto
    if(resto_a != cpf[10]):
        return False
        
    return True
