notas = [7.5, 8.0, 6.5, 9.0]
print(notas)
soma = sum(notas)
numdenotas = len(notas)
média = (soma/numdenotas)
print(média)
notas.append(5.0)
print(notas)
notas.pop(2)
print(notas)
notasemordem = sorted(notas)
print(notasemordem)
print(list(reversed(notasemordem)))
umatuple = (1, 2, 3, 4)
print(umatuple)
list(umatuple)
print(umatuple)
t1 = [1, 2]
t2 = [3, 4]
novatuple = (t1 + t2)
print(novatuple)
fakesett = [1, 3, 3, 6, 5]
print(set(fakesett))
sett = {1, 3, 3, 6, 5}p
sett.add(2)
sett.remove(6)
print(sett)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1, s2)
print(s1 & s2)
print(s1 | s2)
print(s2 - s1)

otatuple = (22, 25, 27, 21)
if max(otatuple) > 26:
    print("tá quente")

otoset = {2, 4, 6, 8}
print(otoset)
digitado = int(input("digite um número"))
if digitado in otoset:
    print("já tem")
else:
    otoset.add(digitado)
    print(otoset)

dict = {"nome": "João", 
        "Grr": 122334, 
        "Nota": 100
        }
if dict["Nota"] < 40:
    situação = "reprovado"
elif dict["Nota"] >= 40 and dict["Nota"] < 70:
    situação = "exame"
else: 
    situação = "aprovado"

print(dict["nome"], dict["Grr"], situação)
