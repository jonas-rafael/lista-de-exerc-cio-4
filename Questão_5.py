#Faça um programa que receba um endereço IP e informe se tal IP tem formato válido ou não. Use
#uma função para realizar a validação, a função receberá o IP e retornará um valor lógico indicando
#se o IP é válido ou não. No seu programa, o usuário poderá digitar quantos endereços IP quiser
#validar, até que ele digite a palavra “sair”.
import ipaddress


def confir(ip):
   if ipaddress.ip_address(ip):
       print("True")
   else:
       print("Ip não existe!")


while True:
    ip=(input("Digite um ip ex: "))
    confir(ip)