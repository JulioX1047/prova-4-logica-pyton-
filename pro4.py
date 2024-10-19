comeco=int(input("Informe o começo do intervalo"))
final=int(input("Informe o final do intervalo"))
soma= 0
for numero in range(comeco,final +1):
    if numero%2==0:
        soma+=numero

if soma!=0:
    print(f" A soma dos numeros pares no intervalo de {comeco} a {final} é = {soma}")
else:
    print("Não a numeros pares no intervalo ")    