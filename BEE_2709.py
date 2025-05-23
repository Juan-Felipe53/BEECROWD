valueArray = []
result = 0
coins = 0
jump = 0

def es_primo(n):
    if n < 2:
        return False  # Los números menores que 2 no son primos
    if n == 2:
        return True  # 2 es el único número par primo
    if n % 2 == 0:
        return False  # Los números pares mayores que 2 no son primos
    for i in range(3, int(n**0.5) + 1, 2):  # Solo revisar los impares hasta la raíz cuadrada de n
        if n % i == 0:
            return False  # Si es divisible por algún número impar, no es primo
    return True  # Si no encontró divisores, es primo

while es_primo(result) == False:
    try:
        coins = int(input().strip())
        for i in range(coins):
            values = int(input().strip())
            valueArray.insert(i,values)
        jump = int(input().strip())
        valueArray.reverse()
    except EOFError:
        break  # Se detiene cuando no hay más entrada
    for i in range(0, len(valueArray), jump):
        result += int(valueArray[i])
        
    if es_primo(result) == False:
        print("Bad boy! I’ll hit you.")
        result = 0
        valueArray = []
        
    if es_primo(result) == True:
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")