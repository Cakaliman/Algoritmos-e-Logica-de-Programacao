def tamanho(n):
    ac = 1
    while n>10:
        n = n//10
        ac = ac + 1
    print(ac)

x = int(input('Digite um númmero: '))
tamanho(x)
print('--FIM--')