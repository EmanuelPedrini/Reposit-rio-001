num=int(input("num"))
i=0
numpares=0
for i in range(i, num + 1):
   if i%2==0:
      numpares +=1
      continue
   print(i)
print(f"existem {numpares} numeros pares")