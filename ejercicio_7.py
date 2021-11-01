import statistics

lista_num = []

for i in range(0, 3):
    num = int(input('Introduce numero: '))
    lista_num.append(num)

media = statistics.mean(lista_num)
mediana = statistics.median(lista_num)
varianza = statistics.variance(lista_num)

print(f"--------------------------------\n>> Media {media}\n>> Mediana {mediana}\n>> Varianza {varianza}\n--------------------------------")
