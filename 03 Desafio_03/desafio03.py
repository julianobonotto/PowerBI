def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista

    visuais = lista_visuais.split(", ")
    lista_padronizada = []
    for palavra in visuais:
        lista_padronizada.append(palavra.title())

    # TODO: Normalize e remova duplicatas usando um conjunto    
    set_remove_duplicados = set(lista_padronizada)

    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final = []
    lista_final = sorted(set_remove_duplicados)

    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()
#entrada_usuario = "Gráfico de Barras, Gráfico de Barras, Tabela, Gráfico de Pizza, gráfico de barras"

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)