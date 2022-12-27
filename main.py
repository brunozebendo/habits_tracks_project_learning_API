"""o objetivo do código é criar uma API que irá postar um request junto ao site PIXELAR que cria
um quadro (parece um github) com uma graduação da cor de acordo com a quantidade de horas dedicadas
 a um hábito. Para isso é preciso seguir um total de seis passos descritos na documentação da API"""

import requests
from datetime import datetime
"""o primeiro passo é criar os parâmetros mínimos necessários, aqui passados como constantes, e abaixo
reproduzidos no user_params"""

USERNAME = "brunozebendo"
TOKEN = "yourtoken"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
"""o segundo paso é criar um gráfico individual, já passando os parâmetros"""
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
"""o terceiro paso é passar as configurações do gráfico, a identificação, o nome, a unidade de medida, o tipo
 da informação e a cor"""
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
"""a função da variável headers é passar o TOKEN através de variável abaixo, sintaxe exigida pela API, e 
depois passar o headers como Kwarg e como valor dentro da variável response. Isso se dá pois existem
3 maneiras de passar a key de uma API, uma delas, recomendada, é o headers, que camufla a chave no cabeçalho
da requisição"""
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
"""essa biblioteca pega a data de hoje"""
today = datetime.now()
# print(today.strftime("%Y%m%d"))
"""abaixo é o parâmetro que será passado (POST) para a API, a função strtime formata a data, no caso abaixo
sairá no formato yyyymmdd q é o exigido na documentação da API"""
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
"""o update_endpoint é a variável que vai guardar o endereço da informação que queremos modificar (como se
fosse um link), depois, as partes abaixo comentadas irão usar o put para inserir ou o delete para apagar a
 informação"""
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)