n = int(input())

for l in range(n):
    a, b = input().split()
    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")