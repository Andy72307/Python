
# Break
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        break

for i in range(1, 10):
    if i % 2 == 1:
        continue
    print(i)

print('Cadena Hola Mundo')
cadena = 'Hola Mundo'
voc = 0
for i in range(len(cadena)):
    if cadena[i] == 'a' or cadena[i] == 'e' or cadena[i] == 'i' or cadena[i] == 'o' or cadena[i] == 'u':
        voc += 1
print(voc)