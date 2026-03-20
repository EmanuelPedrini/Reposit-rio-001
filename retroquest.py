import random
import sys
start=input("Wanna to start retroquest? yep or exit  ")
if start=="yep":
    gamerunning=1
    print("ok")
elif start=="exit":
    sys.exit()

def rolld20():
    return random.randint(1,20)

