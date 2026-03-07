#INPUT
TdeVic = int(input("Insira seu Número de Vitórias"))
TdeLos = int(input("Insira seu Número de Derrotas"))

#CALCULA A PORCENTAGEM DE TG
Tg = int((TdeVic) + (TdeLos))
VicPercent = (TdeVic * 100 / Tg)

#MOSTRA OS RESULTADOS AO USUÁRIO
print("Você jogou " + str(Tg) + " Partidas")
print("Ganhando " + str(VicPercent) + "% das Partidas")
