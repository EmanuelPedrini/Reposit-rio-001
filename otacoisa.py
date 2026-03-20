lista = [3,7,10,15,22,30]

for i in lista:
    if i <= 10:
        continue
    print(i)
    i +=1

numparesnalista3=0
lista2 = [5, 8, 12, 20]
somalista2 = sum(lista2)
print(somalista2)

lista3=[1,2,3,4,5,6,7]
for i in lista3:
    if i%2==0:
        numparesnalista3 +=1
        continue

print(numparesnalista3)

lista4=[1,2,2,3,3,3,4]
contagem1=0
contagem2=0
contagem3=0
contagem4=0

for c in lista4:
    if c==1:
        contagem1+=1
for c in lista4:
    if c==2:
        contagem2+=1
for c in lista4:
    if c==3:
        contagem3+=1
for c in lista4:
    if c==4:
        contagem4+=1

lista5={
    1:contagem1,
    2:contagem2,
    3:contagem3,
    4:contagem4
}
print(lista5)

#jeitochato
valores=[10,25,7,99,3]
valoresbunitinemrodi=sorted(valores)
maior=(valoresbunitinemrodi[len(valoresbunitinemrodi)-1])
print(maior)