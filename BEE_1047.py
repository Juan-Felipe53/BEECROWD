from datetime import datetime, timedelta

lista = input().split(" ")
x = []
for i in range(len(lista)):
    x.append(int(lista[i]))
acumuladoh = 0


# Crear objetos datetime para la hora de inicio y la hora de finalización
inicio = datetime(2023, 1, 1, x[0], x[1])
fin = datetime(2023, 1, 1, x[2], x[3])

# Si la hora de finalización es menor o igual a la de inicio, se asume que terminó al día siguiente
if fin <= inicio:
    fin += timedelta(days=1)

# Calcular la duración
duracion = fin - inicio

# Extraer horas y minutos de la duración
total_minutos = duracion.total_seconds() // 60  # Convertir duración a minutos totales
duracion_horas = int(total_minutos // 60)       # Obtener las horas completas
duracion_minutos = int(total_minutos % 60)      # Obtener los minutos restantes

# Mostrar el resultado
print(f"O JOGO DUROU {duracion_horas} HORA(S) E {duracion_minutos} MINUTO(S)")


    
