matriz=[
[
    [9,2,5],
    [4,6,2],
    [0,4,5],
    [9,5,3]
],
[
    [9,2,5],
    [4,6,2],
    [0,4,5]
],
[
    [9,2,5],
    [4,6,2],
    [0,4,5]
]
]
# print(matriz)

nota=[
    [9,2,5,9,2,5],
    [4,6,2,9,2,5],
    [0,4,5,9,2,5] 

]

promedio=[sum(notas)/len(notas) for notas in nota]
print(promedio)