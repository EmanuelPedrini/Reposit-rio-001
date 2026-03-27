cidade = [
    [1, 0, 2, 0, 1],  
    [0, 9, 2, 1, 3],  
    [1, 0, 1, 9, 2],  
    [9, 3, 0, 2, 1],  
    [0, 1, 2, 0, 9] 
]
vazio=0
casa=0
hospital=0
gerador=0
dest=0
lin=0
col=0
for i in cidade:
    col=0
    lin+=1
    for n in i:
        col+=1
        if n ==0:
            vazio+=1
        if n ==1:
            casa+=1
        if n==2:
            hospital+=1
            print(f"hospital em ({lin},{col}):")
        if n==3:
            gerador+=1
        if n==9:
            dest+=1
print(vazio)
print(casa)
for i in list(range(len(cidade))):
    for n in range(len(cidade[i])):
        if cidade[i][n]==2:
            if cidade[i][n-1]==9 or cidade[i][n+1]==9:
                print(f"Hospital em ({i},{n}): EM PERIGO!!")
            if i < len(cidade)-1:
                if cidade[i-1][n]==9 or cidade[i+1][n]==9:
                    print(f"Hospital em ({i},{n}): EM PERIGO!!")

for i in list(range(len(cidade))):
    for n in range(len(cidade[i])):
        if (cidade[i][n]) == 3:
            for