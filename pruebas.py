import math

a = 6
b = 2
print(a % b)

def es_primo(n:int)->bool:

    cota_sup = math.floor(n ** (1/2)) + 1


    for divisor in range(2, cota_sup):
        if n % divisor == 0:
            return False

    return True

print(es_primo(10))