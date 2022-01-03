list=[]
while True:
    num=int(input("Digite uma nota para a lista:"))
    list.append(num)
    if num ==-1:
        list.pop()
        break
    elif num!=-1:
        print("Número adcionado com sucesso:")
    else:
        print("Inserção de notas finalizadas!")
print(list)
print(f"A quantidade de elementos na lista é {len(list)} ")
print(20*"--")

#x.append(list.remove(";"))
print(f"a ordem que foram informados{list}")
print(20*"--")
list.sort(reverse=True)
for elem in list:
    list1=[]
    list1.append(elem)
    print(f"     {elem}")
print(20*"--")
#--------------------------------------------
soma=0
for j in list:
    soma = soma + j


x=len(list)
media= soma / x
print(f" A média aritmética de todos os itens da lista é {media} ")
print(20*"--")
list.sort(reverse=True)
for elem in list:
    print(elem)
    if elem>media:
        print(f"Este elemento é maior que a media {elem}")
    elif elem<media:
        print(f"Este elemento é menor que a media{elem}")


