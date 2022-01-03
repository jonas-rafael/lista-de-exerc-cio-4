def media_a(n1,n2,n3,n4,n5):
    media=(n1+n2+n3+n4+n5)/5
    return media

while True:
    atleta=str(input("Digite o nome do atleta ou (fim) para finalizar o programa: "))



    media1=0

    if atleta=="fim":
        break
    else:
        salto1 = float(input("Digite a distancia do primeiro salto"))
        salto2 = float(input("Digite a distancia do segundo salto"))
        salto3 = float(input("Digite a distancia do terceiro salto"))
        salto4 = float(input("Digite a distancia do quarto salto"))
        salto5 = float(input("Digite a distancia do quinto salto"))
        media = media_a(salto1, salto2, salto3, salto4, salto5)
        if salto1>salto1:

            salto1=salto1

        elif salto2>salto2:
            salto2=salto2

        elif salto3>salto3:

            salto3=salto3

        elif salto4 > salto4:
            salto4 = salto4

        elif salto5 > salto5:
            salto5 = salto5

        elif media>media1:
            media1=media
            atleta1=atleta

print(atleta1)
print(f"Saltos {salto1},{salto2},{salto3},{salto4},{salto5}")
print(f"A media de saltos é{media}")