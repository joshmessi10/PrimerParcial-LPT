import time

start_time1 = time.time()
suma1 = 0
for i in range(1,99999):
	suma1 += i
end_time1 = time.time()

start_time2 = time.time()
suma2 = 0
for i in range(1,999999):
        suma2 += i
end_time2 = time.time()

start_time3 = time.time()
suma3 = 0
for i in range(1,9999999):
        suma3 += i
end_time3 = time.time()

print(f"Tiempo de ejecución en Python de la suma de 1 a 99999: {end_time1 - start_time1:.6f} segundos")
print(f"Tiempo de ejecución en Python de la suma de 1 a 999999: {end_time2 - start_time2:.6f} segundos")
print(f"Tiempo de ejecución en Python de la suma de 1 a 9999999: {end_time3 - start_time3:.6f} segundos")

