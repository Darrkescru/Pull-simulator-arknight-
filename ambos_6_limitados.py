import random

# Parametros da simulação, você pode alterar como quiser a quantia de pulls e a quantia de simulações que vai rodar.
# Tenha em mente que se o numero de pulls for muito baixo, e o numero de simulações tambem, provavelmente a porcentagem retornada vai ser 0%
# Em media são feitos 34 pulls para pegar uma unidade de 6 estrelas qualquer

NUM_SIMULACAO = 20000
NUM_PULLS = 100

def calculo_pity(pulls_sem_6):
    if pulls_sem_6 < 50:
        return 0.02
    else:
        return ((pulls_sem_6 - 49) * 0.02)

def simular_pull():
    pity = 0
    pegou_limitado = False
    pegou_nlimitado = False 
    for _ in range(NUM_PULLS):
        chance_6 = calculo_pity(pity)
        if random.random() <= chance_6 :
            pity = 0
            Escolhido = random.random()
            if Escolhido < 0.35 :
                pegou_limitado = True
            elif Escolhido < 0.70 :
                pegou_nlimitado = True
        else:
            pity += 1

        if pegou_nlimitado and pegou_limitado:
            return True
        
    return pegou_nlimitado and pegou_limitado

sucessos = sum(simular_pull() for _ in range(NUM_SIMULACAO))

porcentagem = (sucessos / NUM_SIMULACAO) * 100
print (f"Porcentagem de vezes que ambos foram pegos : {porcentagem:.2f}%")

