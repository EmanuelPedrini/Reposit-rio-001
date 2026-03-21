import random; import sys
gamerunning=2

start=input("Wanna to start retroquest? yep or exit  ")
if start=="yep":
    gamerunning=1
    print("ok")
elif start=="exit":
    gamerunning=0
def rolld20():
    return random.randint(1,20)

personagem={
    "name" : "guerreiro",
    "acthealth" : 3,
    "maxhealth": 3
    }
print(personagem["name"])
