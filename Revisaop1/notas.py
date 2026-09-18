notas = [4, 7, 9]
selecionadas = []
for nota in notas:
    if nota >= 7:
        selecionadas.append(nota)
print(selecionadas)

selecionadas = [nota for nota in notas if nota >= 7]