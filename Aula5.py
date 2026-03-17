numfinal=int(input("qual o número final?"))
lista = range(0,(numfinal+1),1)
n=0
while n<len(lista):
    print(lista[n])
    n+=1
if n == len(lista):
    print(f"Soma = {sum(lista)}")

    #ou

num=int(input("Digite um número"))
i = 0
soma = 0
for i in range(1, num+1):
    soma += i

print(f"soma ={soma}")