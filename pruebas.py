import math

a = 50
b = 2
print(a % b)

def es_primo(n:int)->bool:

    cota_sup = math.floor(n ** (1/2)) + 1


    for divisor in range(3, 30, 2):
        print(divisor)
        if n % divisor == 0:
            return False
        
    return True

print(es_primo(10))