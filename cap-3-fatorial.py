# FATORIAL COM RECURSÃO
#
# O fatorial de um número é ele multiplicado por todos os números menores até 1:
#   fatorial de 3 = 3 × 2 × 1 = 6
#
# Truque usado aqui: o fatorial de 3 é 3 vezes o fatorial de 2,
# e o fatorial de 2 é 2 vezes o fatorial de 1.
# Por isso a função chama a si mesma (isso se chama RECURSÃO).
#
# CALL STACK (pilha de chamadas)
# Pense numa pilha de bilhetes em cima da mesa:
#   - cada vez que uma função é chamada, um bilhete novo vai em cima da pilha,
#     com as anotações daquela chamada (ex.: "aqui o x vale 3");
#   - só se trabalha no bilhete de cima;
#   - quando a função termina, o bilhete dela é jogado fora e o trabalho volta
#     para o bilhete de baixo, exatamente de onde tinha parado.
#
# PASSO A PASSO DO fat(3)
# Subindo a pilha (as chamadas):
#   1. fat(3): x = 3. Não é 1, quer calcular 3 * fat(2). Pausa e chama fat(2).
#   2. fat(2): x = 2. Não é 1, quer calcular 2 * fat(1). Pausa e chama fat(1).
#   3. fat(1): x = 1. É o caso base: devolve 1 sem chamar mais ninguém.
#
#   Nesse momento a pilha está assim (o de cima é o mais recente):
#     ┌──────────────────────────────┐
#     │ fat(1): x = 1  → devolve 1   │  ← topo
#     ├──────────────────────────────┤
#     │ fat(2): x = 2  → esperando…  │
#     ├──────────────────────────────┤
#     │ fat(3): x = 3  → esperando…  │
#     └──────────────────────────────┘
#
# Descendo a pilha (as respostas):
#   4. fat(1) sai da pilha e entrega 1.
#   5. fat(2) continua de onde parou: 2 * 1 = 2. Entrega 2 e sai da pilha.
#   6. fat(3) continua de onde parou: 3 * 2 = 6. Entrega 6 e sai da pilha.
#   7. A pilha fica vazia e o print mostra 6.
#
# PONTO IMPORTANTE
# Cada bilhete tem o seu próprio x. O fat(3) não perde o seu 3 enquanto espera:
# ele fica guardado no bilhete dele, embaixo da pilha.
#
# E SE NÃO TIVESSE O CASO BASE?
# A função chamaria a si mesma para sempre e a pilha cresceria até não caber mais.
# O Python avisa com um RecursionError (o famoso "stack overflow").
# Isso acontece aqui se você chamar fat(0): o número vai para -1, -2, -3...
# e nunca chega no 1.

def fat(x):
    if x == 1:
        return 1  # caso base: aqui a função para de chamar a si mesma
    else:
        return x * fat(x-1)  # caso recursivo: pausa, chama fat com um número menor e espera a resposta

print(fat(3))
