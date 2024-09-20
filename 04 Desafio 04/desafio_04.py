def extrair_anos(datas):
    from datetime import datetime
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    lista_anos = []
    mascara = "%Y-%m-%d"
    for uma_data in lista_datas:
        lista_anos.append(str(datetime.strptime(uma_data, mascara).year))

    print(lista_anos)
    anos = lista_anos
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


#entrada = input()
entrada = "2022-12-31, 2021-01-01, 2020-05-25"
# TODO: Chame a função para imprimir o resultado:

saida = extrair_anos(entrada)
print(saida)