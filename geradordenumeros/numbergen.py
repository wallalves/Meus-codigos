def numbgen(arqName, m):
    f = open(arqName,'w')

    valor_max = 10**m
    print(valor_max)

    for n in range(valor_max):
        nb_line = str(n).zfill(m) + "\n"
        print(nb_line)
        f.write(nb_line)
    f.close()
    print("Concluido com sucesso")

# parametros = (nome_do_arquivo.txt, casas_decimais)
numbgen("numeros11.txt", 11 )