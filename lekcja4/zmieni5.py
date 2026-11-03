koszty = [123.45,67,67,67,67,667,123467]

suma = sum(koszty)

print("suma:" ,suma)

print(max(koszty))

 
for i in koszty:
    suma = suma + i


print("suma", suma)

print(*range(67))



todo = ["spszątanie","odkurznie","mucie","ścieranie","nouka","zmywarka","dmuhanie"]
status = []

for i in todo:
    odp = input(f"Czy {i} zrobione?")
    status.append(odp)

for i in range(len(todo)):
    print(f"{todo[i]}: {status[i]}")