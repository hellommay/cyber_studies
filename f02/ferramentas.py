def media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota

    resultado_media = soma / len(notas)
    return resultado_media


def classificar(nota):
    if nota >= 90:
        return "louvor"
    elif nota >= 70:
        return "aprovado"
    else:
        return "reprovado"
    
    
print(classificar(media([85, 92, 78])))
