import random

num_simulacoes = 50000

def calculo_pity(pity_atual):
    if (pity_atual) <= 50: 
        return 0.02
    else:
        return ((pity_atual - 49) * 0.02)

def simular_pull():
    pegou_6 = False
    pity = 1
    while pegou_6 == False:
        if random.random() <= calculo_pity(pity):
            pegou_6 = True 
        else:
            pity += 1
    
    return pity 

numero_sagrado = sum(simular_pull() for _ in range(num_simulacoes))
media_numero = numero_sagrado/num_simulacoes

print (f"o pity medio obtido em {num_simulacoes} simulações foi : {media_numero}")


# 2%
# if pull > 50 
# + {2%}