
def datac(dia,mes,ano):
    meses=["Janeiro","Fevereiro","Março","Abril","Maio","junho","julho","agosto","Setembro","outubro","novembro","Dezembro"]

    if mes== 1:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[0]}/{ano}")
    elif mes== 2:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[1]}/{ano}")
    elif mes== 3:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[2]}/{ano}")
    elif mes== 4:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[3]}/{ano}")
    elif mes== 5:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[4]}/{ano}")
    elif mes== 6:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[5]}/{ano}")
    elif mes== 7:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[6]}/{ano}")
    elif mes== 8:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[7]}/{ano}")
    elif mes== 9:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[8]}/{ano}")
    elif mes== 10 :
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[9]}/{ano}")
    elif mes== 11:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[10]}/{ano}")
    elif mes== 12:
        print(f"A data inserida após formatação ficou desta forma {dia}/{meses[11]}/{ano}")



while True:
    print("Digite a data DD/MM/AAAA")
    dia=int(input("Dia: "))
    mes=int(input("mês: "))
    ano=int(input("ano: "))

    print(f" A a data escolhida está correta? {dia}/{mes}/{ano}")
    conf=str(input("sim ou não: ").lower())
    if conf == "sim":
        break
    else:
        print("Digite novamente!")

datac(dia,mes,ano)