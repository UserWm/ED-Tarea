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
#print(matriz)

nota=[
    [9,7,6],
        [9,5,8],
            [10,5,7],
                [7,9,2],
]
promedio= [sum(notas)/len(notas) for notas in nota]
print(promedio)